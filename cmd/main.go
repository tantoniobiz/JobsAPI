package main

import (
	"github.com/tantoniobiz/JobsAPI/server"
	"net/http"
)

func main() {
	mux := http.NewServeMux()

	rh := http.RedirectHandler("http://example.org", 307)
	mux.Handle("/foo", rh)

	server.Server(mux)
}