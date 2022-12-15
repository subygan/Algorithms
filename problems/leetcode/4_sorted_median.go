package main

import "sort"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

	var m []int
	m = append(m, nums1...)
	m = append(m, nums2...)
	sort.Ints(m)
	mid := len(m) / 2
	if len(m)%2 == 1 {
		return float64(m[mid])
	}
	return float64(m[mid]+m[mid-1]) / 2
}
