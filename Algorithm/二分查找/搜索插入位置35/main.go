/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-08 08:10:28
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-08 08:24:35
 */
package main

import "fmt"

func solve(nums []int, target int) int {
	left, right := 0, len(nums)
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			return mid
		}
	}
	return left
}

func main() {
	nums := []int{1, 2, 3, 5, 6}
	target := 5
	expected := 3
	if solve(nums, target) == expected {
		fmt.Println(true)
	} else {
		fmt.Println(false)
	}

}
