/**
 * File              : leetcode_222.go
 * Author            : Andy
 * Date              : 2022.09.24
 * Last Modified Date: 2022.09.24
 * Last Modified By  : Andy
 */

package countNodes

func countNodes(root *TreeNode) int {
	count := 0
	var dfs func(node *TreeNode, count *int)
	dfs = func(node *TreeNode, count *int) {
		if node == nil {
			return
		} else {
			*count++
			dfs(node.Left, count)
			dfs(node.Right, count)
		}
	}
	dfs(root, &count)
	return count
}
