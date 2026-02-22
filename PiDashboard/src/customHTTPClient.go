package main

import (
	"crypto/tls"
	"crypto/x509"
	"net/http"
	"os"
);

var CERT_PATH = "../certs/local.crt";

func loadCert() []byte {
	cert, err := os.ReadFile(CERT_PATH);
	if err != nil {
		logger.Panic().
		Err(err).
		Msg("Error reading CA certificate");	
	} else {
		logger.Info().Msg("CA certificate loaded");
	}
	return cert;
}

func customHTTPClient() *http.Client {
	logger.Info().Msg("Building HTTP client with self signed cert...");
	
	cert := loadCert();

    rootCAs, err := x509.SystemCertPool()
	if err != nil {
		logger.Panic().
		Err(err).
		Msg("Failed to load system root CA certificates");
	}

	if rootCAs == nil {
		rootCAs = x509.NewCertPool();
		logger.Info().Msg("Created new root CA pool");
	}

    if ok := rootCAs.AppendCertsFromPEM(cert); !ok {
		logger.Panic().
		Msg("Failed to append CA certificate");
    }

    config := &tls.Config{
        RootCAs: rootCAs,
    }

    tr := &http.Transport{TLSClientConfig: config}
	logger.Info().Msg("HTTP client with self signed cert successfully built");
    return &http.Client{Transport: tr}
}
