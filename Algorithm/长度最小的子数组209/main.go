/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-15 17:12:52
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-15 17:28:10
 */
package main

import (
	"fmt"
)

func solve(nums []int, target int) int {
	n := len(nums)
	left, right := 0, 0
	cur_sum := 0
	min_length := n + 1
	for right < n {
		cur_sum += nums[right]
		for cur_sum >= target {
			cur_sum -= nums[left]
			min_length = min(min_length, right-left+1)
			left++
		}
		right++
	}
	if min_length < n+1 {
		return min_length
	} else {
		return 0
	}
}

func main() {
	nums := []int{2, 3, 1, 2, 4, 3}
	target := 7
	expected := 2
	if solve(nums, target) == expected {
		fmt.Println("correct")
	} else {
		fmt.Println("wrong")
	}
}
