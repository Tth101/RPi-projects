package main

import (
	"net/http"
	"encoding/json"
)

func getNewHC(w http.ResponseWriter, r *http.Request) {
    logger.Info().Msg("getNewHC handler called");
    hcResult := healthcheck();
    jsonResult := toJson(hcResult);
    postResults(jsonResult);

    w.Header().Set("Content-Type", "application/json");
    w.Write(jsonResult);  
    
    logger.Info().Msgf("getNewHC handler: %v", hcResult);
}

func getInfoContent(w http.ResponseWriter, r *http.Request) {
    logger.Info().Msg("getInfoContent handler called");
    infoResult := getContent();
    jsonResult := toJson(infoResult);
    w.Header().Set("Content-Type", "application/json");
    w.Write(jsonResult);  
    
    logger.Info().Msgf("getInfoContent handler: %v", infoResult);
}

func getLatestHC(w http.ResponseWriter, r *http.Request) {
    latestHcResult := getLastestResults();
    jsonResult := toJson(latestHcResult);

    w.Header().Set("Content-Type", "application/json");
    w.Write(jsonResult); 
    
    logger.Info().Msgf("getLatestHC handler: %v", latestHcResult);
}

func getURLs(w http.ResponseWriter, r *http.Request) {
    jsonResult := toJson(urls);
    
    if jsonResult == nil {  
        http.Error(w, "getURLs handler returns null", http.StatusInternalServerError);
    } else {
        w.Header().Set("Content-Type", "application/json");
        w.Write(jsonResult);
    }

    logger.Info().Msgf("getURLs handler: %v", urls);
}

func toJson(input any) []byte{
    output, err := json.Marshal(input);
    if err != nil {
        logger.Warn().Msgf("Error marshalling input to JSON: %v", err)
    } else {
        return output
    }
    return nil
}