package main

import (
	"database/sql"
	"net/http"
	"os"
	"github.com/rs/zerolog"
	_ "modernc.org/sqlite"
)

var logger = zerolog.New(zerolog.ConsoleWriter{Out: os.Stderr}).With().Timestamp().Logger();
var db *sql.DB;
var selfSignedHTTPSClient *http.Client;
var urls URLs;

func main() {
    db = initDB();
    createSchemas();
    urls = readYaml();
    selfSignedHTTPSClient = customHTTPClient();
    initServer();
     //Take note autoHC should never be before initDB because it 
     //assumes db is already initialised
    autoHC();

    defer db.Close();
    defer logger.Info().Msg("Database closed");
}

func initDB() *sql.DB{
    logger.Info().Msg("Database initialising...")

    if _, err := os.Stat("../database.db"); err != nil {
        if os.IsNotExist(err) { 
            logger.Info().Msg("Database file does not exist, will be created")
        } else {
            //Some error occured that isn't because of db file not existing
            logger.Panic().Err(err).Msg("Some other error occured")
        }
    }

	db, err := sql.Open("sqlite", "../database.db")
	if err != nil {
		logger.Panic().Err(err).Msg("Error opening/creating database file")
	}
    if err := db.Ping(); err != nil {
        logger.Panic().Err(err).Msg("Database unreachable")
    }
    logger.Info().Msg("Database successfully initialised")

    return db;
}

func initServer() {
    router := http.ServeMux{};
    fs := http.FileServer(http.Dir("../static"));
    router.Handle("/", fs);
    router.HandleFunc("/hc/new", getNewHC);
    router.HandleFunc("/hc/latest", getLatestHC);
    router.HandleFunc("/urls", getURLs);
    router.HandleFunc("/info", getInfoContent);
    logger.Info().Msg("Server started on 8080");
    go func() {
        http.ListenAndServe(":8080", &router);
    }()    
}
