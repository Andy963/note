/**
 * File              : leetcode_1305.go
 * Author            : Andy
 * Date              : 2022.09.21
 * Last Modified Date: 2022.09.21
 * Last Modified By  : Andy
 */

package getAllElements

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	ans := []int{}

	var dfs func(*TreeNode)

	dfs = func(node *TreeNode) {
		if node != nil {
			dfs(node.Left)
			ans = append(ans, node.Val)
			dfs(node.Right)
		}
	}
	dfs(root1)
	dfs(root2)
	sort.Ints(ans)
	return ans
}
