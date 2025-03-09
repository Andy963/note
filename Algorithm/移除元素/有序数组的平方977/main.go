/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-15 16:12:44
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-15 16:35:10
 */
package main

import "fmt"

func solve(nums []int) []int {
	n := len(nums)
	left, right, pos := 0, n-1, n-1
	ans := make([]int, n)
	for left <= right {
		l_val, r_val := nums[left]*nums[left], nums[right]*nums[right]
		if l_val < r_val {
			ans[pos] = r_val
			right -= 1
		} else {
			ans[pos] = l_val
			left += 1
		}
		pos -= 1
	}
	return ans
}

func sliceEqual(a, b []int) bool {
	/*
		compare two slice
	*/
	if len(a) != len(b) {
		return false
	}
	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	nums := []int{-7, -3, 2, 3, 11}
	expected := []int{4, 9, 9, 49, 121}
	result := solve(nums)
	if sliceEqual(result, expected) {
		fmt.Println("correct.")
	}
}
