/**
 * File              : leetcode_049.go
 * Author            : Andy
 * Date              : 2022.08.10
 * Last Modified Date: 2022.08.10
 * Last Modified By  : Andy
 */

package main

import (
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs string) [][]string {
	mp := make(map[string][]string)
	for i := 0; i < len(strs); i++ {
		str := strs[i]
		// 单个字符串只能先用strings.Split,转成数组，再通过sort.Strings()排序
		// 再将它们组合成字符串，且必须用不同变量，因为变量类型不同，不能直接覆盖
		str_ := strings.Split(str, "")
		sort.Strings(str_)
		tmp := strings.Join(str_, "")
		// 判断是否有键，可能直接对如果有的值进行判断，因为如果值也不存在，而不一定非要用ok
		if len(mp[tmp]) > 0 {
			mp[tmp] = append(mp[tmp], str)
		} else {
			mp[tmp] = []string{str}
		}
	}
	values := [][]string{}
	// range 可遍历k,v
	for _, v := range mp {
		values = append(values, v)
	}
	return values

}
