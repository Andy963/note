/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-08 08:55:58
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-08 08:57:39
 */

package main

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] > target {
			right = mid - 1
		} else if nums[mid] < target {
			left = mid + 1
		} else {
			return mid
		}
	}
	return -1
}
