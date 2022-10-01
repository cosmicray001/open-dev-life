package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	maps := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		maps[nums[i]] = i
	}

	var ans [][]int
	_len := len(nums)
	for i := 0; i < _len-2; i++ {
		for j := i + 1; j < _len-1; j++ {
			sum := -(nums[i] + nums[j])
			if value, ok := maps[sum]; ok && j < value {
				ans = append(ans, []int{nums[i], nums[j], sum})
			}
			for nums[j] == nums[j+1] {
				j++
				if j >= _len-1 {
					break
				}
			}
		}
		for nums[i] == nums[i+1] {
			i++
			if i >= _len-2 {
				break
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
	fmt.Println(threeSum([]int{0, 1, 1}))
	fmt.Println(threeSum([]int{1, 2, -2, -1}))
}
