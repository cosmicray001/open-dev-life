package main

func maximum(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func minimum(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func maxArea(height []int) int {
	_max := -99999999
	left, right := 0, len(height)-1
	for {
		_max = maximum(_max, (right-left)*minimum(height[left], height[right]))
		if left == right {
			break
		}
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}
	return _max
}
