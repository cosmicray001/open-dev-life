package main

import (
	"fmt"
	"math"
)

func isPrime(givenNumber int) bool {
	if givenNumber == 2 || givenNumber == 3 {
		return true
	}
	if givenNumber % 2 == 0 || givenNumber <= 1{
		return false
	}
	rangeLimit := int(math.Sqrt(float64(givenNumber)))
	for i:=3; i <= rangeLimit ; i+=2 {
		if givenNumber % i == 0{
			return false
		}
	}
	return true
}

func main(){
	var givenInput int
	fmt.Println("Please enter your number")
	_, err := fmt.Scanf("%d", &givenInput)
	if err != nil{
		fmt.Println(err)
	}
	result := isPrime(givenInput)
	if result {
		fmt.Println("Your Number is Prime")
	}else{
		fmt.Println("Your Number is not Prime")
	}
}