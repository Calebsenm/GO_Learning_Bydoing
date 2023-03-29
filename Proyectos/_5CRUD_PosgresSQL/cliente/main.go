package main

import (
	"fmt"
)

type Book struct{

	Titulo    	      string
	Contenido 	      string
	Autor             string 
	NumeroArticulos   int 
}


var HojasPapel Book

func Create(){

}
func Read(){

}
func Update(){

}
func Delete(){

}

func main(){

	fmt.Println("Hello this is a simple Crud in go")
	
	var menu map[int]string = map[int]string{
		1 : "Create",
		2 : "Read",
		3 : "Update",
		4 : "Delete",
	}

	for a,b := range menu{
		fmt.Println(a , " -  ", b)
	}

	var option int 
	fmt.Println("Que deseas hacer por favor ingrese :  ")
	fmt.Scan(&option)

	switch option {
	case 1:
		Create()
	case 2:
		Read()
	case 3:
		Update()
	case 4: 
		Delete()
	}
	
}


