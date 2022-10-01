package main

import "fmt"

func maximumSum(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func maxSubArray(nums []int) int {
	maxSum := nums[0]
	sum := 0
	for index := range nums {
		sum += nums[index]
		maxSum = maximumSum(sum, maxSum)
		if sum < 1 {
			sum = 0
		}
	}
	return maxSum
}

func main() {
	fmt.Println(maxSubArray([]int{-1}))
}
