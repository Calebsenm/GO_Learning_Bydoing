package main

import (
	"fmt"
)


type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("Cannot  Sqrt  negative number: %v ", float64(e))
}

func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return x , nil
	}
	
	z := float64(0.1)

	for {
		z -= (z*z - x) / (2 * z)
		sqrtData := z * z
		fmt.Println(z, " = ", sqrtData)
		if sqrtData == x {
			return z , nil 
		}
	}

}

func main() {
	valor , err := Sqrt(2)
	
	if err != nil{
		fmt.Println(err)
	}
	fmt.Println(valor)
}
