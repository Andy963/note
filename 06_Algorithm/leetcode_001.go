/**
 * File              : leetcode_001.go
 * Author            : Andy
 * Date              : 2022.08.08
 * Last Modified Date: 2022.08.08
 * Last Modified By  : Andy
 */
;

func twoSum(nums []int, target int) []int{
	for i, x := range nums{
		for j:= i+1;j < len(nums); j++{
			if x + nums[j] == target{
				return []int{i, j}
			}
		}
	}
	return nil
}
