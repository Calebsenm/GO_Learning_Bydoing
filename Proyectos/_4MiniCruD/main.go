package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main(){

	file , ferr := os.Open("Palabras.csv");
	if ferr != nil{
		fmt.Println(file)
	}
	scanner := bufio.NewScanner(file)


	iop := 1
	for scanner.Scan(){
		line := scanner.Text()
		items := strings.Split(line,",")


		fmt.Println(iop ," ",items)

		iop ++
	}


	

}