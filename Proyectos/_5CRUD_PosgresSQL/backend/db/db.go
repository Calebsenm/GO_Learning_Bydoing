package db

import  (
	"database/sql"
	"fmt"
)

const(
	DB_HOST = "localhost"
	DB_PORT = "5432"
	DB_USER = "caleb"
	DB_PASWORD = "12345"
	DB_NAME = "test"
)


func ConnectPostgres()  (*sql.DB , error ) {

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