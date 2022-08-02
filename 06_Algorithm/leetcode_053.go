/**
 * File              : leetcode_053.go
 * Author            : Andy
 * Date              : 02.08.2022
 * Last Modified Date: 02.08.2022
 * Last Modified By  : Andy
 */

// 这种方法被称为贪心算法，虽然很早就听过这个算法，但总感觉没完全理解
// 简单点讲就是局部最优，但贪心算法虽然局部最优，但却不能保证整体最优

func maxSubArray(nums []int) int {
	pre := 0
	maxVal := -10001 // 题目指定了范围
	for i := 0; i < len(nums); i++ {
		pre += nums[i]
		if pre > maxVal {
			maxVal = pre
		}
		if pre < 0 {
			pre = 0
		}
	}
	return maxVal
}
