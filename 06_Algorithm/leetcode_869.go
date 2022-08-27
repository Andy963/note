/**
 * File              : leetcode_869.go
 * Author            : Andy
 * Date              : 2022.08.27
 * Last Modified Date: 2022.08.27
 * Last Modified By  : Andy
 */

package sortStrings

import (
	"sort"
	"strings"
)

func sortString(x int) string {
	// 先将数字转字符串，再转成数组
	arr := strings.Split(strconv.Itoa(x), "")
	// 排序
	sort.Strings(arr)
	// 连成字符串
	return strings.Join(arr, "")
}

func reoderedPowerOf2(n int) bool {
	str := sortStrings(n)
	for i := 0; i < 32; i++ {
		// go中 2的n次方通过移位的方式，如下面 2**i
		// 表示为 1 << i  = 1 * 2 ** i
		if sortStrings(1<<i) == str {
			return true
		}
	}
	return false
}
