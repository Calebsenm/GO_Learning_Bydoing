package main

import "fmt"

// when you have two similars type of date you can  put one int only
// for example func add(a ,y int ) in{ }


func add(x int, y int ) int {
	return x + y 
}

func main(){

	fmt.Println(add(42,13))
}



