package main

import "fmt"

func subsets(nums []int) [][]int {
	var ans [][]int
	var path []int
	findPath(nums, path, 0, &ans)
	return ans
}

func findPath(nums []int, path []int, index int, result *[][]int) {
	if len(nums) == index {
		tmp := make([]int, len(path))
		copy(tmp, path)
		*result = append(*result, tmp)
		return
	}

	findPath(nums, path, index+1, result)
	path = append(path, nums[index])
	path = path[:len(path)-1]
}
