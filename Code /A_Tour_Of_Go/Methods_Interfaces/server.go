
package main

import (
	"fmt"
	"net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hackeo De la naza exitoso :D ")
    })

	fmt.Print("Server runnig in 40000")
	
    http.ListenAndServe(":40000", nil)
	
}