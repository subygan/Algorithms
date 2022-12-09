package main

func IsAlienSorted(words []string, order string) bool {

	newOrder := make([]int, 26)

	for i,v := range order{
		newOrder[int(v) - 97] = i
	}

	for i, word := range words[:len(words)-1]{

		for j, _ := range word{

			if j >= len(words[i+1]) {
				return false
			}
			if newOrder[int(words[i][j]) - 97] > newOrder[int(words[i+1][j]) - 97] {
				return false
			} else if newOrder[int(words[i][j]) - 97] < newOrder[int(words[i+1][j]) - 97] {
				break
			} else {
				continue
			}

		}

	}

	return true

}