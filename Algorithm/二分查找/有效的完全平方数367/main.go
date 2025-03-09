/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-07 22:03:05
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-08 08:07:45
 */

package main

import "fmt"

func solve(num int) bool {
	if (num == 1) {
		return true
	}
	left, right := 0, num
	for (left <= right) {
		mid := left + (right-left) / 2
		square := mid * mid
		if num > square{
			left = mid + 1
		} else if num < square {
			right = mid - 1
		} else {
			return true
		}
	}
	return false
}

func main() {
	num := 5 
	rs := solve(num)
	if rs == true {
		fmt.Println(true)
	}else{
		fmt.Println(false)
	}
}
