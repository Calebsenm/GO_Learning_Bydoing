package main

import (
	"database/sql"
	"fmt"
	"io"
	"net/http"

	_ "github.com/lib/pq"
)

const(
	DB_HOST = "localhost"
	DB_PORT = "5432"
	DB_USER = "caleb"
	DB_PASWORD = "12345"
	DB_NAME = "Test"
)

func posgresqlConnect()  (*sql.DB , error ) {

	postgresInfo :=  fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=%s",
								 DB_HOST,DB_PORT,DB_USER, DB_PASWORD,DB_NAME)

	db , err := sql.Open("postgresql", postgresInfo)

	if err != nil{
		panic(err)
	}

	err = db.Ping()
  	if err != nil {
    	panic(err)
  	}

	return db , err
}


// server XD
func main(){
	fmt.Println("Server is running in localhost 8080")
	// this is the golang server 
	http.HandleFunc("/", func(w http.ResponseWriter, peticion *http.Request) {
		io.WriteString(w, "Aqui Vamos  XD ")
	})
	
	//Server runing
	Server := http.Server{
		Addr: ":2080",
	}

	err1 := Server.ListenAndServe()

	if err1 != nil {
		panic(err1)
	}

}