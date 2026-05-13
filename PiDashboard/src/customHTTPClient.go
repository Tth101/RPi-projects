package main

import (
	"context"
	"crypto/tls"
	"crypto/x509"
	"net"
	"net/http"
	"os"
);

func loadCert() []byte {
	cert, err := os.ReadFile(CERT_PATH);
	if err != nil {
		logger.Panic().
		Err(err).
		Msg("Error reading CA certificate");	
	} else {
		logger.Info().Msg("CA certificate loaded");
	}

	return cert
}

func customHTTPClient() *http.Client {
	logger.Info().Msg("Building HTTP client with self signed cert...");

	//Loading cert
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

    tlsConfig := &tls.Config{
		InsecureSkipVerify: true, //See if can remove this
        RootCAs: rootCAs,
    }

	//Setting DNS resolver
	var (
		dnsResolverIP = "192.168.88.20:53"
		dnsResolverProtocol = "udp"
	)

	dialer := &net.Dialer{
		Resolver: &net.Resolver{
			PreferGo: true,
			Dial: func(ctx context.Context, network, address string) (net.Conn, error) {
				d := net.Dialer{}
				return d.DialContext(ctx, dnsResolverProtocol, dnsResolverIP)
			},
		},
	}
	
	dialContext := func(ctx context.Context, network, address string) (net.Conn, error) {
		return dialer.DialContext(ctx, network, address)
	}

	tr := &http.Transport{
		TLSClientConfig: tlsConfig,
		DialContext: dialContext,
	}

	logger.Info().Msg("HTTP client successfully built");

    return &http.Client{Transport: tr}
}
