/**
 * File              : leetcode_053_v2.go
 * Author            : Andy
 * Date              : 03.08.2022
 * Last Modified Date: 03.08.2022
 * Last Modified By  : Andy
 */

func max(l []int) int {
	maxVal := l[0]
	for _, v := range l {
		if v > maxVal {
			maxVal = v
		}
	}
	return maxVal
}

func maxSubArray(nums []int) int {
	for i := 1; i < len(nums); i++ {
		if nums[i-1] > 0 {
			nums[i] += nums[i-1]
		}
	}
	return max(nums)
}
