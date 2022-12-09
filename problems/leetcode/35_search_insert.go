package main


func SearchInsert (nums []int, target int) int {

	left, right := 0, len(nums)-1

	for left <= right {
		mid := (left + right)/2
		n := nums[mid]

		if n == target{
			return mid
		} else if n > target {
			right = mid -1
		} else if n < target {
			left = mid + 1
		}

	}

	return right + 1
}

