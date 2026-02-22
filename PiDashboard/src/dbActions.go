package main

import (
	"fmt"
	_ "modernc.org/sqlite"
);

type HCResult struct {
	Id int
	JSON string
	Datetime string
}

var hcTable = "Healthcheck"
var jsonResultsCol = "JSONResult"
var datetimeCol = "DateTime"
var IdCol = "Id"

func createSchemas() {
	query := fmt.Sprintf(
	"CREATE TABLE IF NOT EXISTS %s (%s INTEGER PRIMARY KEY, --id\n %s TEXT, --jsonResults\n %s DATETIME --datetime\n); ", 
	hcTable,IdCol,jsonResultsCol,datetimeCol)
	_, err := db.Query(query);
	if err != nil {
		logger.Debug().Msgf("createSchemas query: %s", query)
		logger.Fatal().Msgf("createSchemas: %v", err);
	} 
	logger.Info().Msg("Schemas exist/initialised")
}

func getLastestResults() HCResult {
	resultObj := HCResult{};
	query := fmt.Sprintf("SELECT %s, %s FROM %s ORDER BY %s DESC LIMIT 1;", jsonResultsCol, datetimeCol, hcTable, IdCol)
	rows, err := db.Query(query);
	if err != nil {
		logger.Debug().Msgf("getLatestResults query: %s", query)
		logger.Error().Msgf("getLatestResults: %v", err);
	} else {
		var json string;
		var datetime string;
		if rows.Next() {
			//Types must be in same order as result's types
			rows.Scan(&json, &datetime)	
			resultObj.JSON = json;
			resultObj.Datetime = datetime;
		}
		rows.Close();
	}
	return resultObj;
}

func postResults(JSONResults []byte) {
	datetimeFormat := "'%d/%m/%Y, %l:%M:%S %P'"
	query := fmt.Sprintf("INSERT INTO %s (%s, %s) VALUES (?, strftime(%s, datetime('now', 'localtime')));", hcTable, jsonResultsCol, datetimeCol, datetimeFormat)
	res , err := db.Exec(query, JSONResults);
	if err != nil {
		logger.Debug().Str("query", query).Msg("postResults query")
		logger.Error().Err(err).Msg("postResults");
	} else {
		rowsAffected, err := res.RowsAffected();
		if err != nil {
			logger.Err(err).Msg("postResults.res.RowsAffected")
		}

		logger.Info().Int("Rows Affected", int(rowsAffected)).Msg("postResults");
	}
}

