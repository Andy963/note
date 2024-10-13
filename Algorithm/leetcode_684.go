/**
 * File              : leetcode_684.go
 * Author            : Andy
 * Date              : 2022.08.23
 * Last Modified Date: 2022.08.23
 * Last Modified By  : Andy
 */

// 链接：https://leetcode.cn/problems/redundant-connection/solution/684-rong-yu-lian-jie-bing-cha-ji-ji-chu-eartc/

package findredundantconnect

var (
	n      = 1001
	father = make([]int, 1001)
)

func initialize() {
	for i := 0; i < n; i++ {
		father[i] = i
	}
}

func find(u int) int {
	if u == father[u] {
		return u
	}
	father[u] = find(father[u])
	return father[u]
}

func join(u, v int) {
	u, v = find(u), find(v)
	if u == v {
		return
	}

	father[u] = v
}

func same(u, v int) bool {
	return find(u) == find(v)
}

func findRedundantConnection(edges [][]int) []int {
	initialize()

	for i := 0; i < len(edges); i++ {
		if same(edges[i][0], edges[i][1]) {
			return edges[i]
		} else {
			join(edges[i][0], edges[i][1])
		}
	}
	return []int{}
}
