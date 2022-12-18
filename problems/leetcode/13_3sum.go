package main

import "sort"

func threeSum(nums []int) [][]int {
	var ans [][]int

	sort.Ints(nums) //Create a sorted array

	for i := 0; i < len(nums)-2; i++ { // iterate through the array
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		// create 2 pointers j and y
		for j := i + 1; j < len(nums)-1; j++ {
			y := len(nums) - 1 // second pointer from the beginning

			for j < y {
				if (nums[i] + nums[j] + nums[y]) == 0 {
					ans = append(ans, []int{nums[i], nums[j], nums[y]})

					for j < y && nums[j] == nums[j+1] {
						j++
					}

					for y > j && nums[y] == nums[y-1] {
						y--
					}
				}

				y--
			}
		}
	}

	return ans
}
