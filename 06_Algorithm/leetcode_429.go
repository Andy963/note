/**
 * File              : leetcode_429.go
 * Author            : Andy
 * Date              : 2022.08.21
 * Last Modified Date: 2022.08.21
 * Last Modified By  : Andy
 */

package levelOrder

func levelOrder(root *Node) [][]int {
	var result [][]int
	q := make([]*Node, 0)
	if root == nil {
		return result
	}
	q = append(q, root)
	for len(q) != 0 {
		// 用来存当前层的数据
		cur := make([]int, 0)
		size := len(q)
		for i := 0; i < size; i++ {
			// 从前面取出一个节点
			node := q[0]
			q = q[i:]
			cur = append(cur, node.Val)
			for _, child := range node.Children {
				q = append(q, child)
			}
		}
		result = append(result, cur)
	}
	return result
}
