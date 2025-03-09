/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-07 21:45:18
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-07 21:56:47
 */
package main

import "fmt"

func solve(nums []int, val int) int {
	slow, fast := 0, 0
	for fast < len(nums) {
		if nums[fast] != val {
			nums[slow] = nums[fast]
			slow += 1
		}
		fast += 1
	}
	return slow
}

func main() {
	nums := []int{3, 2, 2, 3}
	val := 3
	expected := 2
	if expected == solve(nums, val) {
		fmt.Println(true)
	} else {
		fmt.Println(false)
	}
}
