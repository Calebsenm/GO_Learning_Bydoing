package main

import (
	"fmt"
	"net/http"
	"io"
)

// server XD
func main(){
	fmt.Println("Server in localhost 8080")
	// this is the golang server 
	http.HandleFunc("/", func(w http.ResponseWriter, peticion *http.Request) {
		io.WriteString(w, "welcome")
	})

	//

	Server := http.Server{
		Addr: ":8080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}

}