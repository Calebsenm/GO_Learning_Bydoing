package main

import (
	"fmt"
	"os"
	"strconv"

	"database/sql"

	_ "github.com/go-sql-driver/mysql"
)

var(

	// thisMap map[string]int  = map[string]int{}

	hola  [1000000]  string
)



func main(){

	// create a database object which can be used
    // to connect with database.
	db, err :=  sql.Open("mysql", "root:password@tcp(0.0.0.0:3306)/words")
	   
    // Now its  time to connect with oru database,
    // database object has a method Ping.
    // Ping returns error, if unable connect to database.
    err = db.Ping()
     
    // handle error
    if err != nil {
        panic(err)
    }


	// database object has a method called Query,
    // It can execute a SQL query and return rows
    // as result. Here we insert a row into  the  table,
    // no row returned as result for this operation.

     
    fmt.Print("Successfully  Inserted\n")

	f, err := os.Open("index.txt")

	if err != nil{
		fmt.Println("Error ", err)

	}


	iop := 0
	for{

		
		value__ := " "
		_,err := fmt.Fscan(f, &value__)

		if err != nil{
			break
		}
		hola[iop] = value__ 
		iop ++
	}

	// this is for iterate the map
	io := 1

	for i := 0; i < len( hola); i++ {
		io ++
		fmt.Println(io," ",i ," ", hola[i])

		_, err = db.Query("INSERT INTO cats ( wordsTest, Translation) VALUES   ( '" + strconv.Itoa(i)+" ', '"+  hola[i] +"');")
     
		
		// // handle error
		// if err != nil {
	
		// 	continue
		// 	panic(err)
			
		// }
	
	}

	// database object has  a method Close,
    // which is used to free the resource.
    // Free the resource when the function
    // is returned.
	defer db.Close()
	


}




