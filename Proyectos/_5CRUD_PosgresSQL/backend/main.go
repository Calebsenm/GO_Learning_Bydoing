package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"text/template"
	"backend/db"
)

type entrega struct {
	Id    int 
  Name  string
	Age   int
	Gmail string
}


// Codificar los datos de la variable  como JSON y enviarlos como respuesta
func getRoute(w http.ResponseWriter, r *http.Request) {

	if r.Method != http.MethodGet {
		http.Error(w, "Metodo no permitido", http.StatusMethodNotAllowed)
		return
	}

  fmt.Println("XD")
	//llamado a la base de datos
  dataBase , _ := db.ConnectPostgres();
	defer dataBase.Close();
  
  data , err := dataBase.Query("SELECT * FROM persona");
  if err != nil{
    fmt.Println("Eerror -> ", err);
  }

  fmt.Println(data)
	var Users [] entrega
	for data.Next(){
		var  entregas entrega;
    fmt.Println(data)
		data.Scan(&entregas.Id,&entregas.Name , &entregas.Age, &entregas.Gmail)
    
		Users = append(Users, entregas)
	}

	err1 := json.NewEncoder(w).Encode(Users)
	if err1 != nil {
		http.Error(w, err1.Error(), http.StatusInternalServerError)
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

	
// server XD
func main() {
	fmt.Println("Server is running in localhost 2080")
	// this is the golang server
	
	http.Handle("/", http.FileServer(http.Dir("../cliente/src1")))
	http.HandleFunc("/home", homeHandler)
	http.HandleFunc("/api/datos", getRoute);
	

	//Server runing
	Server := http.Server{
		Addr: ":2080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}


 
}
