package main

import (
	"time"
)

func autoHC() {
	ticker := time.NewTicker(time.Hour * 5)

	for range ticker.C {
		hcResult := healthcheck()
		jsonResult := toJson(hcResult)
		postResults(jsonResult)
	}
}
