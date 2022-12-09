package main

import "fmt"

func Roman123(s string) int {

	var prev int
	tot := 0
	dict := map[string]int{
		"I":1,"V": 5, "X":10, "L":50, "C": 100, "D":500, "M":1000,
	}
	prev = 10000
	for _,v := range s {
		st:= fmt.Sprintf("%c", v)
		val := dict[st]

		if prev >= val {
			tot += val
		} else {
			tot += val - 2*prev
		}
		prev = val

	}
	return tot
}