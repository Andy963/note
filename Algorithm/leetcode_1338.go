/**
 * File              : leetcode_1338.go
 * Author            : Andy
 * Date              : 2022.08.30
 * Last Modified Date: 2022.08.30
 * Last Modified By  : Andy
 */

package minSetSize

import "sort"

func counter(arr []int) map[int]int {
	// 统计每个数字出现的次数
	result := make(map[int]int)
	for _, v := range arr {
		// 是否存在这个键，如果存在统计数据加1
		// range 可以得到索引和值
		if _, ok := result[v]; ok {
			result[v]++
		} else {
			result[v] = 1
		}
	}
	return result
}

func minSetSize(arr []int) int {
	counts := counter(arr)
	vals := make([]int, len(counts))
	for _, v := range counts {
		vals = append(vals, v)
	}

	// sort.Ints(vals)
	//倒序排序
	sort.Sort(sort.Reverse(sort.IntSlice(vals)))

	// 数组长度, 整除/
	length, half := len(arr), len(arr)/2
	removed := 0

	for v := range vals {
		length -= v
		removed++
		if length <= half {
			return removed
		}
	}
	return removed

}
