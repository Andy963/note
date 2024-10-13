/**
 * File              : leetcode_054.go
 * Author            : Andy
 * Date              : 2022.10.01
 * Last Modified Date: 2022.10.01
 * Last Modified By  : Andy
 */

package convertBST

func convertBST(root *TreeNode) *TreeNode {
	total := 0
	var dfs func(*TreeNode, *int) *TreeNode
	dfs = func(node *TreeNode, total *int) *TreeNode {
		if node == nil {
			return nil
		}

		dfs(node.Right, total)
		*total += node.val
		node.Val = *total
		dfs(node.Left, total)
		return node
	}
	return dfs(root, &total)
}
