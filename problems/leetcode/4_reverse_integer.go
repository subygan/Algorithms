package main

func reverse(x int) int {

	var r int
	num := x
	if x < 0 {
		num = -num
	}
	for {
		rem := num % 10
		res := num / 10
		r = r*10 + rem
		num = res
		if res < 1 {
			break
		}
	}

	r = r
	if !checkInt32(r) {
		return 0
	}
	if x < 0 {
		return -r
	}

	return r
}

func checkInt32(i int) bool {

	if i > 2147483648 {
		return false
	}
	return true
}
