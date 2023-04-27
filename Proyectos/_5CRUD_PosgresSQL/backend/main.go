package main

import (
	"backend/db"
	"encoding/json"
	"fmt"
	"net/http"
	"text/template"
  "strings"
  "io/ioutil"
  "strconv"
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

	//llamado a la base de datos
	dataBase, _ := db.ConnectPostgres()
	defer dataBase.Close()

	data, err := dataBase.Query("SELECT * FROM persona")

	if err != nil {
		fmt.Println("Eerror -> ", err)
	}

  
  var Users []entrega
  
  for data.Next() {
		var entregas entrega
		data.Scan(&entregas.Id, &entregas.Name, &entregas.Age, &entregas.Gmail)
		
    Users = append(Users, entregas)
  
	}

	// renderizado
	err1 := json.NewEncoder(w).Encode(Users)
	if err1 != nil {
		http.Error(w, err1.Error(), http.StatusInternalServerError)
		return
	}

}

func getDataId( w http.ResponseWriter , r * http.Request){
   
  fmt.Println("Peticion Echa :X")

  // parsea la direccion  /api/datos/1
  url := strings.Split(r.URL.Path , "/")
  fmt.Println("ID: ", url[3])
  // hace un get a la api para luego convertirla en una estrucctura 
  resp , err := http.Get( "http://localhost:3080/api/datos")
  
  if err != nil{
    fmt.Println("Error al obtener la respuesta de la API:", err)
    return
  }
  defer resp.Body.Close()

  // le la entrega  y la pasa los datos a una estrucctura 
  body, err := ioutil.ReadAll(resp.Body)
  var  Usuarios []entrega 
  err = json.Unmarshal(body,&Usuarios)
  
  if err != nil{
    fmt.Println("Error al analizar el JSON:", err)
    return
  }

  id := url[3]
  num, _ := strconv.Atoi(id)


  for _, dato := range Usuarios {
    if dato.Id == num{
        fmt.Println(dato)
      	json.NewEncoder(w).Encode(dato)
    }
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

func putData ( w http.ResponseWriter , r *http.Request){

		if r.Method != http.MethodPost {
			http.Error(w, "Metodo no permitido", http.StatusMethodNotAllowed)
			return
		}
  
		var nuevaEntrega entrega
		err := json.NewDecoder(r.Body).Decode(&nuevaEntrega)

		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}

		fmt.Println("Datos recibidos Con exito!!! ")
		fmt.Println(nuevaEntrega)
		
		// Coneccion a la base De datos 

		//llamado a la base de datos
		dataBase, _ := db.ConnectPostgres()
		defer dataBase.Close()

		//comprueba si los datos fueron enviados a  la base de datos
		query := "SELECT id FROM persona WHERE id ='" + nuevaEntrega.Gmail + "'"

		var id int 
		err = dataBase.QueryRow(query).Scan(&id)

		if err != nil {

			insertQuery := "INSERT INTO persona(name, age, gmail) VALUES($1, $2, $3)"
			_, err = dataBase.Exec(insertQuery, nuevaEntrega.Name, nuevaEntrega.Age, nuevaEntrega.Gmail)
			
			if err != nil {
				fmt.Println("Error ", err)
			}else {
				fmt.Println("la entrega Guardada con exito")
				fmt.Println(nuevaEntrega)
			}
		}
}

func updateUser( w http.ResponseWriter , r * http.Request ){

  var data  entrega 
  json.NewDecoder(r.Body).Decode(&data)
  fmt.Println(data)

}


// server XD
func main() {
	fmt.Println("Server is running in localhost 3080")
	// this is the golang server

	http.Handle("/", http.FileServer(http.Dir("../cliente/src1")))
	http.HandleFunc("/home", homeHandler)
	// get
	http.HandleFunc("/api/datos", getRoute)
  http.HandleFunc("/api/datos/",getDataId)
	// post
	http.HandleFunc("/api/datos/new", putData)
  // put 
  http.HandleFunc("/api/datos{id}",updateUser)

	//Server runing
	Server := http.Server{
		Addr: ":3080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}
}


