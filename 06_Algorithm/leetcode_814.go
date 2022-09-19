/**
 * File              : leetcode_814.go
 * Author            : Andy
 * Date              : 2022.09.19
 * Last Modified Date: 2022.09.19
 * Last Modified By  : Andy
 */

package pruneTree

func dfs(node *TreeNode) *TreeNode {
	if node == nil {
		return nil
	}

	Left := dfs(node.Left)
	node.Left = Left
	Right := dfs(node.Right)
	node.Right = Right

	if node.Left == nil && node.Right == nil {
		if node.Val == 1 {
			return node
		} else {
			return nil
		}
	}

	return node
}
func pruneTree(root *TreeNode) *TreeNode {

	return dfs(root)
}
