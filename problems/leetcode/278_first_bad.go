package main

//https://leetcode.com/problems/first-bad-version/


func FirstBadVersion(n int) int {
	low, high, r := 0,n, -1

	for low <= high {
		mid := (low+ high)/2
		if isBadVersion(mid){
			r = mid
			high = mid -1
		} else {
			low = mid + 1
		}
	}
	return r
}


func isBadVersion(n int) bool {

	if n < 10{
		return false
	}
	return true
}