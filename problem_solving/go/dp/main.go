package main

import (
	"fmt"
)

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	fib := make([]int, n+1)
	fib[0], fib[1] = 0, 1

	for i := 2; i <= n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}

	return fib[n]
}

func main() {
	fmt.Println("Fibonacci Sequence:")
	for i := 0; i < 10; i++ {
		fmt.Printf("%d ", fibonacci(i))
	}
}
