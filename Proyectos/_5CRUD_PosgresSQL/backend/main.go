package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"text/template"

	_ "github.com/lib/pq"
)

type entrega struct {
	Name  string
	Age   int
	Gmail string
}

// Codificar los datos de la variable  como JSON y enviarlos como respuesta
func getRoute(w http.ResponseWriter, r *http.Request) {

	var entregas []entrega = []entrega{
		{"Caleb", 18, "caleb@gmail.com"},
		{"Ana", 25, "ana@gmail.com"},
		{"Juan", 32, "juan@gmail.com"},
	}
	if r.Method != http.MethodGet {
		http.Error(w, "Metodo no permitido", http.StatusMethodNotAllowed)
		return
	}
	err := json.NewEncoder(w).Encode(entregas)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	// Cargar el archivo HTML en una plantilla
	tmpl, err := template.ParseFiles("../cliente/src2/index.html")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Ejecutar la plantilla con los datos necesarios
	data := struct{ Title string }{Title: "Página de inicio"}
	err = tmpl.Execute(w, data)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

// routes
func Routes() {
	http.HandleFunc("/api/datos", getRoute);



	
}

// server XD
func main() {
	fmt.Println("Server is running in localhost 2080")
	// this is the golang server
	fileServer := http.FileServer(http.Dir("../cliente/src1"))
	http.Handle("/", fileServer)

	http.HandleFunc("/home", homeHandler)
	// routes call
	Routes()

	//Server runing
	Server := http.Server{
		Addr: ":4080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}


 
}
