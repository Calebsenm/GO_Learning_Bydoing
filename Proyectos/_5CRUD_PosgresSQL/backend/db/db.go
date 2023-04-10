package db

import  (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"

)

const(
	DB_USER = "caleb"
	DB_PASSWORD = "12345"
	DB_NAME = "test"
)


func ConnectPostgres()  (*sql.DB , error ) {


	db, err := sql.Open("postgres", fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", "localhost", 5432, DB_USER, DB_PASSWORD, DB_NAME))


	if err != nil{
		fmt.Println("postgresql")
		panic(err)
	}

	err = db.Ping()
  	if err != nil {
    	panic(err)
  	}
	return db , err
}