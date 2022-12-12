package main

func removeElement(nums []int, val int) int {

	k := 0

	for _, v := range nums {
		if v != val {
			nums[k] = v
			k += 1
		}
	}

	return k
}
