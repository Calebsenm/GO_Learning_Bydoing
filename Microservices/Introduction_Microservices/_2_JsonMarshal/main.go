package main 

import(
    "fmt"
    "net/http"
    "log"
    "encoding/json"
)

type helloWorldResponse struct {
	Message string  `json:"message"`
}

func main() {
    port := 8080
    
    http.HandleFunc("/helloworld", helloWorldHandler)   
    log.Printf("Server starting on port %v\n", 8080)
    log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", port), nil))
}

func helloWorldHandler(w http.ResponseWriter, r *http.Request) {
	response := helloWorldResponse{Message: "HelloWorld"}
	data, err := json.Marshal(response)

	if err != nil {
		panic("Ooops");
	}
	fmt.Fprint(w, string(data))
}



