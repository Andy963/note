/**
 * File              : leetcode_167.go
 * Author            : Andy
 * Date              : 03.08.2022
 * Last Modified Date: 03.08.2022
 * Last Modified By  : Andy
 */

func twoSum(numbers []int, target int) int {
	l, r := 0, len(numbers)-1
	ans := make([]int, 2)
	for l < r {
		tmp := numbers[l] + numbers[r]
		if tmp > target {
			r --
		}else if tmp < target{
			l ++
		}else if tmp == target{
			ans[0], ans[1] := l+1, r+1
			return ans
		}

	}
	return []int{}
}
