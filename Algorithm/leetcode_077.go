/**
 * File              : leetcode_077.go
 * Author            : Andy
 * Date              : 2022.08.13
 * Last Modified Date: 2022.08.13
 * Last Modified By  : Andy
 */

func combine(n int, k int) [][]int {
	var result [][]int
	var path []int
	findpath(n, path, 1, k, &result)
	return result
}

func findpath(n int, path []int, index int, k int, result *[][]int) {
	// 剪枝，当长度超过了，或者把后面所有元素加起来长度仍不够时
	if len(path) > k || (len(path)+n-index+1) < k {
		return
	}
	if index == n+1 {
		if len(path) == k {
			tmp := make([]int, len(path))
			copy(tmp, path)
			*result = append(*result, tmp)
		}
		return
	}
	// 不选择
	findpath(n, path, index+1, k, result)
	// 选择
	path = append(path, index)
	findpath(n, path, index+1, k, result)
	// 恢复
	path = path[:len(path)-1]
}
