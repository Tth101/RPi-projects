package main

import (
	"io"
	"sync"
)

type infoEndpoint struct {
	Name string;
	Url  string;
	Content string;
	Err string; 
}

func getContent() []infoEndpoint {
	var mu sync.Mutex;
	var wg sync.WaitGroup;
	var countersMu sync.Mutex;
	results := []infoEndpoint{}

	for k, v := range urls.Information {
		wg.Add(1)
		go func(name, url string) {
			defer wg.Done()

			res, err := selfSignedHTTPSClient.Get(url)
			endpointObj := infoEndpoint{Name: name, Url: url}

			if err != nil {
				logger.Warn().
				Str("Endpoint", name).
				Err(err).
				Msgf("Error pinging endpoint");
				endpointObj.Err = err.Error()
			} else {
				defer res.Body.Close()
				countersMu.Lock()
				body, err := io.ReadAll(res.Body);
				if err != nil {
					logger.Warn().
					Err(err).
					Msgf("Error reading endpoint body");
					endpointObj.Content = "";
				} else {
					endpointObj.Content = string(body)
				}
				countersMu.Unlock()
			}

			mu.Lock()
			results = append(results, endpointObj)
			mu.Unlock()

		}(k, v)
	}

	wg.Wait()

	return results;
}