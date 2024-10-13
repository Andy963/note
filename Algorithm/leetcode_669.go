/**
 * File              : leetcode_669.go
 * Author            : Andy
 * Date              : 2022.09.20
 * Last Modified Date: 2022.09.20
 * Last Modified By  : Andy
 */

package trimBST

func trimBST(root *TreeNode, low int, high int) *TreeNode {

	if root == nil {
		return nil
	}

	if root.Val < low {
		return trimBST(root.Right, low, high)
	}

	if root.Val > high {
		return trimBST(root.Left, low, high)
	}

	left := trimBST(root.Left, low, high)
	root.Left = left

	right := trimBST(root.Right, low, high)
	root.Right = right

	return root
}
