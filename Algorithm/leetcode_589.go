/**
 * File              : leetcode_589.go
 * Author            : Andy
 * Date              : 2022.08.20
 * Last Modified Date: 2022.08.20
 * Last Modified By  : Andy
 */

package preorder

func preorder(root *Node) []int {
	ans := make([]int, 0)
	finder(root, &ans)
	return ans
}

func finder(root *Node, ans *[]int) {
	if root == nil {
		return
	}
	for _, node := range root.Children {
		finder(node, ans)
	}
}
