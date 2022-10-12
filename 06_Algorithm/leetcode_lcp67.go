/**
 * File              : leetcode_lcp67.go
 * Author            : Andy
 * Date              : 2022.10.12
 * Last Modified Date: 2022.10.12
 * Last Modified By  : Andy
 */
package expandBinaryTree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func expandBinaryTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	var dfs func(node *TreeNode) *TreeNode

	dfs = func(node *TreeNode) *TreeNode {
		if node == nil {
			return nil
		}
		if node.Left != nil {
			// 注意这里后面是结构体，要用{}
			// 并且是用指针
			Left := &TreeNode{Val: -1, Left: node.Left}
			node.Left = Left
			dfs(node.Left.Left)
		}

		if node.Right != nil {
			Right := &TreeNode{Val: -1, Right: node.Right}
			node.Right = Right
			dfs(node.Right.Right)
		}
		return node
	}
	return dfs(root)
}
