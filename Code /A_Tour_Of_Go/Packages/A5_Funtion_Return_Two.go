// Multiple results
// A function can return any number of results.

// The Two function returns two strings.

package main

import (
	"fmt"
)


func Two(x, y string)(string, string){
	return y , x

}
func main(){

	a,b := Two("Hello","world")
	fmt.Print(a,b)
}

