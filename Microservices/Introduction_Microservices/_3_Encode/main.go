
package main 

import(
    "fmt"
    "net/http"
    "log" 
    "encoding/json"
)

type HelloWorldResponse struct {
	Message string  `json:"message"`
}

func main() {
    port := 8080    
    http.HandleFunc("/helloworld", HelloWorldHandler)   
    log.Printf("Server starting on port %v\n", 8080)
    log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", port), nil))
}

func HelloWorldHandler(w http.ResponseWriter, r *http.Request) {
    response := HelloWorldResponse{Message: "HelloWorld"}
    encoder := json.NewEncoder(w)
    encoder.Encode(&response)
}


