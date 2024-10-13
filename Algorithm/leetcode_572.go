/**
 * File              : leetcode_572.go
 * Author            : Andy
 * Date              : 2022.08.25
 * Last Modified Date: 2022.08.25
 * Last Modified By  : Andy
 */

package isSubtree

func isSame(left *TreeNode, right *TreeNode) bool {
	if left == nil && right == nil {
		return true
	}

	if left == nil || right == nil {
		return false
	}

	return left.Val == right.Val && isSame(left.Left, right.Left) && isSame(left.Right, right.Right)

}

func isSubtree(root *TreeNode, subtree *TreeNode) bool {
	if root == nil && subtree == nil {
		return true
	}

	if root == nil || subtree == nil {
		return false
	}

	return isSame(root, subtree) || isSubtree(root.Left, subtree) || isSubtree(root.Right, subtree)
}
