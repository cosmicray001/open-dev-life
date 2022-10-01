package main

import "fmt"

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxProfit(prices []int) int {
	var profit = -9999999999
	var previousStock = 99999999999
	for index := range prices {
		if prices[index] < previousStock {
			previousStock = prices[index]
		}
		profit = max(profit, prices[index]-previousStock)
	}
	return profit
}

func CallMaxProfit() {
	var data = []int{7, 6, 4, 3, 1}
	fmt.Println(maxProfit(data))
}

func main() {
	CallMaxProfit()
}
