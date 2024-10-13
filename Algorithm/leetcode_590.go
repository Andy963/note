/**
 * File              : leetcode_590.go
 * Author            : Andy
 * Date              : 2022.09.01
 * Last Modified Date: 2022.09.01
 * Last Modified By  : Andy
 */

package postorder

func reverseArr(arr *[]int) {
	length := len(*arr)
	for i := 0; i < length/2; i++ {
		// 可以使用中间变量，也可以像python那样直接交换
		// tmp := (*arr)[i]
		// (*arr)[i] = (*arr)[length-i-1]
		// (*arr)[length-i-1] = tmp
		(*arr)[length-i-1], (*arr)[i] = (*arr)[i], (*arr)[length-i-1]
	}
}

func postorder(root *Node) []int {
	res := make([]int, 0)
	if root == nil {
		return res
	}

	stack := make([]*Node, 0)
	stack = append(stack, root)
	for len(stack) > 0 {
		length := len(stack)
		// 先拿到最后一个值，再把它pop掉
		node := stack[:length-1]
		res = append(res, node.Val)
		for i := 0; i < len(node.Children); i++ {
			stack = append(stack, node.Children[i])
		}
	}

	reverserArr(&arr)
	return res

}
