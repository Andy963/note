/**
 * File              : leetcode_283.go
 * Author            : Andy
 * Date              : 23.07.2022
 * Last Modified Date: 23.07.2022
 * Last Modified By  : Andy
 */

 // 主体思路：将什么样的元素留下？ 非0的元素留下，0的去掉，最后再在结尾补0
 // 88，26，283都是一样的，考虑什么样的元素需要保留

package main

import "fmt"

func moveZeroes(nums []int){
    n := 0
           for i:=0;i<len(nums);i++{
               if nums[i] != 0 {
                   nums[n] = nums[i]
                   n +=
               }
           }
       for n < len(nums){
           nums[n] = 0
           n ++
       }
}

func main() {
    moveZeroes(nums)
}
