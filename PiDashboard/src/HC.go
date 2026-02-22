package main

import (
	"sync"
)

type hcEndpoint struct {
	Name string;
	Url  string;
	Health string;
	StatusCode int;
	Err string; 
}

func healthcheck() []hcEndpoint {
	logger.Info().Msg("Healthcheck start");
	hcEndpointsMappings := urls.Services;
	results := pingEndpoints(hcEndpointsMappings);
	logger.Info().Msg("Healthcheck end");
	return results;
}

func pingEndpoints(hcEndpoints map[string]string) []hcEndpoint {
	results := []hcEndpoint{}
	var mu sync.Mutex;
	var wg sync.WaitGroup;
	var upCounter, downCounter, errCounter int;
	var countersMu sync.Mutex;

	for k, v := range hcEndpoints {
		wg.Add(1)
		go func(name, url string) {
			defer wg.Done()

			res, err := selfSignedHTTPSClient.Get(url)
			endpointObj := hcEndpoint{Name: name, Url: url}

			if err != nil {
				logger.Warn().
				Str("Endpoint", name).
				Err(err).
				Msgf("Error pinging endpoint");
				
				endpointObj.Health = "Err"
				endpointObj.Err = err.Error()

				countersMu.Lock()
				errCounter++
				countersMu.Unlock()
			} else {
				endpointObj.StatusCode = res.StatusCode
				defer res.Body.Close()

				countersMu.Lock()
				if res.StatusCode == 200 {
					endpointObj.Health = "Up"
					upCounter++
				} else {
					endpointObj.Health = "Down"
					downCounter++
				}
				countersMu.Unlock()
			}

			mu.Lock()
			results = append(results, endpointObj)
			mu.Unlock()

		}(k, v)
	}

	wg.Wait()

	logger.Info().
	Int("Total", len(hcEndpoints)).
	Int("Up", upCounter).
	Int("Down", downCounter).
	Int("Error", errCounter).
	Msg("Healthcheck Results");

	return results;
}