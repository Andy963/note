/**
 * File              : leetcode_226.go
 * Author            : Andy
 * Date              : 2022.08.17
 * Last Modified Date: 2022.08.17
 * Last Modified By  : Andy
 */

package invertTree

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	root.Left, root.Right = root.Right, root.Left
	invertTree(root.Left)
	invertTree(root.Right)
	return root
}
