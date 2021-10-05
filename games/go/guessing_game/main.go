package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	var givenNumber int
	rand.Seed(time.Now().UnixNano())
	resultedNumber := rand.Intn(100) + 1
	totalTurn := 10
	hasWon := false
	fmt.Println("---------------- Welcome to Guessing Game --------------------\n" +
		"------------------You have 10 Turns to Guess the number between 1-100------------\n" +
		"---------------Best of Luck.-------------")
	for i := totalTurn; i > 0; i-- {
		fmt.Println("Please Input your Guess.")
		_, err := fmt.Scanf("%d", &givenNumber)
		if err != nil {
			fmt.Println(err)
		}
		if givenNumber == resultedNumber {
			hasWon = true
			break
		} else if givenNumber < resultedNumber {
			fmt.Printf("You guessed Wrong. Higher your guess. Total Turn Left %d\n", i-1)
		} else if givenNumber > resultedNumber {
			fmt.Printf("You guessed Wrong. Lower your guess. Total Turn Left %d\n", i-1)
		}
	}
	if hasWon {
		fmt.Println("Well Done!!! You have won against the computer")
	} else {
		fmt.Println("Sorry. The number was %d\nTry again\n", resultedNumber)
	}
}
