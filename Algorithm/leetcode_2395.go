/**
 * File              : leetcode_2395.go
 * Author            : Andy
 * Date              : 2022.09.14
 * Last Modified Date: 2022.09.14
 * Last Modified By  : Andy
 */

package findSubarrays

func isContains(nums []int, n int) bool {
	for i := 0; i < len(nums); i++ {
		if n == nums[i] {
			return true
		}
	}
	return false
}

func findSubarrays(nums []int) bool {
	n := len(nums)
	seen := make([]int, 0)
	for i := 0; i < n-1; i++ {
		s := nums[i] + nums[i+1]
		if isContains(seen, s) {
			return true
		}
		seen = append(seen, s)
	}
	return false
}
