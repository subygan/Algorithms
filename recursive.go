package main

import "fmt"

type tree struct {
	val   int
	left  *tree
	right *tree
}

func main() {
	list := []int{3, 4, 2, 7, 10, 6, 5, 1, 11}

	t := maketree(list)
	fmt.Println("!!!!!!!", t)
	fmt.Println(printTreeAsc(t))
	fmt.Println(printTreeDesc(t))
}

func maketree(data []int) *tree {

	root := &tree{
		val: data[0],
	}

	for _, v := range data[1:] {
		branch := &tree{
			val: v,
		}
		Addbranch(root, branch)

	}

	return root
}

func Addbranch(root *tree, branch *tree) {

	if root != nil && branch.val > root.val {
		if root.right != nil {
			Addbranch(root.right, branch)
		} else {
			root.right = branch
		}
	} else if root != nil && branch.val < root.val {
		if root.left != nil {
			Addbranch(root.left, branch)
		} else {
			root.left = branch
		}
	}

	return
}

func printTreeAsc(t *tree) string {
	fmt.Printf("%+v\n", t)
	if t == nil {
		return ""
	}
	if t.left != nil {
		return fmt.Sprintf("%v %v %v", printTreeAsc(t.left), t.val, printTreeAsc(t.right))
	} else if t.right != nil {
		return fmt.Sprintf("%v %v", t.val, printTreeAsc(t.right))
	}

	return fmt.Sprintf("%v", t.val)
}

func printTreeDesc(t *tree) string {

	if t == nil {
		return ""
	}
	if t.right != nil {
		return fmt.Sprintf("%v %v %v", printTreeDesc(t.right), t.val, printTreeDesc(t.left))
	} else if t.left != nil {
		return fmt.Sprintf("%v %v", t.val, printTreeDesc(t.left))
	}

	return fmt.Sprintf("%v", t.val)
}
