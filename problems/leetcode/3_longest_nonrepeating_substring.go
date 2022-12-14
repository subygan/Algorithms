package main

func lengthOfLongestSubstring(s string) int {

	max := 0

	if len(s) < 1 {
		return 0
	}

	for i, v := range s {
		m := map[rune]bool{}
		for j, v1 := range s[i:] {
			if ok, v := m[v1]; ok && v == true {
				break
			} else {
				if j+1 > max {
					max = j + 1
				}
				m[v1] = true
			}
		}
		m[v] = false
	}

	return max
}
