package main

import "fmt"

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	head := &ListNode{}
	myNode := head
	prev := 0
	l1v, l2v := 0, 0
	for l1 != nil || l2 != nil {

		if l1 == nil {
			l1v = 0
		} else {
			l1v = l1.Val
		}
		if l2 == nil {
			l2v = 0
		} else {
			l2v = l2.Val
		}

		v := l1v + l2v + prev

		fmt.Println(v)
		if v > 9 {
			prev = 1
		} else {
			prev = 0
		}
		myNode.Next = &ListNode{
			Val: v % 10,
		}

		myNode = myNode.Next
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		fmt.Println(l1, l2)
		fmt.Println(l1 != nil && l2 != nil)
	}
	if prev > 0 {
		myNode.Next = &ListNode{
			Val: prev,
		}
	}

	return head.Next
}
