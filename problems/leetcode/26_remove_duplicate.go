package main

import "fmt"

/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same.
*/

func main() {
	fmt.Println(removeDuplicates([]int{1, 2, 3, 3, 4, 4, 4, 5, 5}))
}

func removeDuplicates(nums []int) int {

	pi := 0
	prev := nums[0]
	for _, v := range nums[0:] {
		if prev < v {
			nums[pi+1] = v
			prev = v
			pi += 1
		}
	}
	fmt.Println(nums)
	return pi + 1
}
