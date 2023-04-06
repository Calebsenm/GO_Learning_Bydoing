package main

import (
	"fmt"
	"net/http"
	"io"
)

func routes(){
	
}


// server XD
func main(){
	fmt.Println("Server is running in localhost 8080")
	// this is the golang server 
	http.HandleFunc("/", func(w http.ResponseWriter, peticion *http.Request) {
		io.WriteString(w, "welcome")
	})
	
	//Server runing
	Server := http.Server{
		Addr: ":8080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}

}