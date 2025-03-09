/**
 * File              : leetcode_026.go
 * Author            : Andy
 * Date              : 22.07.2022
 * Last Modified Date: 22.07.2022
 * Last Modified By  : Andy
 */

// 主体思路：考虑什么样的元素需要留下？
// 和前面的元素不一样的需要留下
// 再考虑边界，第一个元素肯定要放进去，
// 这恰好也解决了i-1越界的问题

package main

import "fmt"

func removeDuplicates(nums []int) int{
    n := 0
           for i:=0;i<len(nums);i++{
               if i == 0 || nums[i] != nums[i-1]{
                   nums[n] = nums[i]
                   n ++
               }
           }
    return n
}
func main() {
	fmt.Println("vim-go")
    removeDuplicates(nums)
}
