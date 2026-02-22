package main

import (
	"gopkg.in/yaml.v3"
	"os"
)

type URLs struct {
	//Capitalised for global scope
    Services    map[string]string 
    Dashboards  map[string]string 
    Information map[string]string
}

func readYaml() URLs {
	fileData, err := os.ReadFile("../URLs.yaml");
	if err != nil {
		logger.Panic().Err(err).Msg("Error reading YAML file");
	}

	if err := yaml.Unmarshal(fileData, &urls); err != nil {
		logger.Panic().Err(err).Msg("Unmarshal error");
	}
	
	logger.Info().Msgf("YAML file successfully read: %v", urls);
	
	return urls;
}