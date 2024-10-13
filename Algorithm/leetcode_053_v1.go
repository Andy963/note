/**
 * File              : leetcode_053_v1.go
 * Author            : Andy
 * Date              : 02.08.2022
 * Last Modified Date: 02.08.2022
 * Last Modified By  : Andy
 */


// 自定义了max函数，比较两个数大小
// 这使用的是动态规划，这个也不是很理解，简单点讲就是大事化小，小事化了
// 【】取最大值 为空
// [a] 取最大值为a
// [a], b 取最大值时，我就需要比较b, 与b+a的最大值
// 通过for循环，将一端固定住，然后在这个范围内求最大值 
//TODO 一直没懂为什么go 没有max 这种内置函数 

func max(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func maxSubArray(nums []int) int {
	result := nums[0]
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		dp[i] = max(dp[i-1]+nums[i], nums[i])
		result = max(d[i], result)
	}
	return result
}
