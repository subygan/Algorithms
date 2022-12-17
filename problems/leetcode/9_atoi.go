package main

import "fmt"

// Not satisfied with this answer, should've used regex
func myAtoi(s string) int {

	b := true
	p := true
	res := 0
	pdone := false
	for _, v := range s {
		n := int(v)
		if b && (n == 48 || n == 32) {
			if n == 48 {
				pdone = true
				b = false
			}
			if pdone && n == 32 {
				return res
			}
			continue
		}
		if pdone && (n == 43 || n == 45 || n == 32) {
			if p {
				return res
			}
			return -res
		}
		if b && n == 43 {
			p = true
			pdone = true
			continue
		}
		if b && n == 45 {
			p = false
			pdone = true
			continue
		}
		if b && n == 46 {
			return 0
		}
		if !b && (n == 32 || n == 46) {
			break
		}
		b = false
		pdone = true

		if n > 47 && n < 58 {
			res = res*10 + (n - 48)
		}
		if n > 57 {
			break
		}
		if p && res > 2147483647 {
			return 2147483647
		}
		if !p && -res < -2147483648 {
			return -2147483648
		}

		fmt.Println(res)
	}
	fmt.Println("!!!", res)
	if p {

		return res
	}
	if -res < -2147483648 {
		return -2147483648
	}

	return -res

}
