package main;


import "fmt";

// the box

func box(A [9]string) string{

  fmt.Println("+---+---+---+")
  fmt.Println("| "+A[0]+" | " +A[1]+" | "+A[2]+" |")
  fmt.Println("+---+---+---+")
  fmt.Println("| "+A[3]+" | " +A[4]+" | "+A[5]+" |")
  fmt.Println("+---+---+---+")
  fmt.Println("| "+A[6]+" | " +A[7]+" | "+A[8]+" |")
  fmt.Println("+---+---+---+")  
  return ""

}

// the logic
func logic(Aa string,Bb string,A [9]string)string {
  fmt.Println(Bb + " Te corresponde la letra " + Aa)

  H := 0
  fmt.Print("Where do you want to play? -> ")
  fmt.Scan(&H)

  if H <= 9 && H >= 1{
    A[H-1] = Aa
  } else{
    fmt.Println("Error")
  }

  return ""
}



func main()  {
  
  fmt.Println(":::::::::::::::::::::::::::::::::");
  fmt.Println(":::::::::Welcome to my game::::::");
  fmt.Println(":::::::::::::::::::::::::::::::::");

  var Player_One string;
  var Player_Two string;


  counter := 0

  for{
    counter++

    fmt.Print("Please input the name of player one -> ")
    fmt.Scan(&Player_One)
    fmt.Print("Please input the name of player two -> ")
    fmt.Scan(&Player_Two)
    
    if Player_One == Player_Two{
      fmt.Println("The name is repeated")
    } else{
      break
    }
  }

  A := [9]string{" "," "," "," "," "," "," "," "," "}
  B := 0
  C := 0
  for{
    B++
    box(A)
    
    if C % 2 == 0{
      logic("X",Player_One,A)
    }   else{
      logic("O",Player_Two,A)
    }
    C++
  }
}
