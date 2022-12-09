package main

func main() {
	isValid("[][][][][]")
}

/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
*/

func isValid(s string) bool {

	mapping := map[rune]rune{
		'}': '{',
		')': '(',
		']': '[',
	}

	stack := []rune{}

	for _, l := range s {

		if val, ok := mapping[l]; ok {
			if len(stack) == 0 {
				return false
			}
			if stack[len(stack)-1] != val {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}

		} else {
			stack = append(stack, l)
		}
	}
	if len(stack) != 0 {
		return false
	}
	return true

}
