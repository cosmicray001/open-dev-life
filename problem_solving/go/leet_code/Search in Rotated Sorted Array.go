package main

func search(nums []int, target int) int {
	left := 0
	length := len(nums) - 1
	right := length
	var mid int
	if length == 0 {
		if nums[0] == target {
			return 0
		}
		return -1
	}
	for left <= right {
		if right-left == 1 {
			if nums[left] == target {
				return left
			} else if nums[right] == target {
				return right
			}
			return -1
		}
		mid = (left + right) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[left] < nums[mid] && nums[mid] < nums[right] {
			if nums[left] <= target && nums[mid] >= target {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else if nums[left] < nums[mid] {
			if nums[left] <= target && nums[mid] >= target {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else {
			if nums[right] >= target && nums[mid] <= target {
				left = mid + 1
			} else {
				right = mid - 1
			}
		}
	}
	return -1
}

//func main() {
//	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 1), "corr: ", 5)
//	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 100), "corr: ", -1)
//	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 5), "corr: ", 1)
//	fmt.Println(search([]int{4, 5, 6, 7, 0, 1, 2}, 2), "corr: ", 6)
//	fmt.Println(search([]int{1}, 3), "corr: ", -1)
//	fmt.Println(search([]int{1}, 1), "corr: ", 0)
//	fmt.Println(search([]int{3, 1}, 1), "corr: ", 1)
//}
