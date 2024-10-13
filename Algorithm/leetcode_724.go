/**
 * File              : leetcode_724.go
 * Author            : Andy
 * Date              : 31.07.2022
 * Last Modified Date: 31.07.2022
 * Last Modified By  : Andy
 */

// 主体思路：左侧前缀和，计算左侧前缀和的值与整个数组的值减去当前前缀和的值
// 当两者相等时，返回当前索引

func pivotIndex(nums []int) int{
    sum, total := 0, 0
    for _, v := range nums {
        total += v
    }

    for i, val := range nums {
        sum += val
        if sum - nums[i] == total - sum {
            return i
        }
    }
    return -1
}
