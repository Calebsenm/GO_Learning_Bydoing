
package main

import "fmt"

var c, python, java bool

func main(){
	var i int
	l := 1
	j := "hola"
	
	fmt.Println(i," ",c,python," ", java)
	fmt.Print(l ," ", j)
	


	var c,python,java = true, false,"no"
	fmt.Println(i, j, c, python, java)
	
	//Fuera de una función, cada declaración comienza con una palabra clave (var, func, etc.) y, por lo tanto, la construcción := no está disponible
	var ii,jj int = 1,2
	kk := 3

	c1,python1,java1 := true,false , "no!"
	fmt.Print(ii,jj,kk,c1,python1,java1)
}