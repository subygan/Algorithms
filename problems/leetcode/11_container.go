package main

func maxArea(height []int) int {
	n := len(height)

	var l, result int
	r := n - 1
	currArea := 0
	for l < r { // note: iteration for 2 pointer approach

		//Calculate the optimum current area
		if height[l] > height[r] {
			currArea = height[r] * (r - l)
		} else {
			currArea = height[l] * (r - l)
		}

		result = max(result, currArea) // update result

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return result
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}