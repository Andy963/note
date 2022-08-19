/**
 * File              : leetcode_94.go
 * Author            : Andy
 * Date              : 2022.08.19
 * Last Modified Date: 2022.08.19
 * Last Modified By  : Andy
 */

package inorderTraversal

func inorderTraversal(root *TreeNode) []int {
	ans := make([]int, 0)
	finder(root, &ans)
	return ans
}

func finder(root *TreeNode, ans *[]int) {
	if root == nil {
		return
	}
	finder(root.Left, ans)
	*ans = append(*ans, root.Val)
	finder(root.Right, ans)
}
