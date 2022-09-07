/**
 * File              : leetcode_2265.go
 * Author            : Andy
 * Date              : 2022.09.07
 * Last Modified Date: 2022.09.07
 * Last Modified By  : Andy
 */

package averageOfSubtree

func dfs(node *TreeNode, ans *int) (int, int) {
	if node == nil {
		return 0, 0
	}

	left_t, left_c := dfs(node.Left)
	right_t, right_c := dfs(node.Right)

	total := left_t + right_t + node.Val
	count := left_c + right_c + 1

	if total/count == node.Val {
		*ans++
	}
	return total, count
}

func averageOfSubtree(root *TreeNode) int {
	ans := 0
	dfs(root, &ans)
	return ans
}
