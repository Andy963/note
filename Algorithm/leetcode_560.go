/**
 * File              : leetcode_560.go
 * Author            : Andy
 * Date              : 30.07.2022
 * Last Modified Date: 30.07.2022
 * Last Modified By  : Andy
 */

// 主体思路：记录前缀和，以及前缀和中每个数字出现的次数
// 如果当前前缀和-k的值在map中，那么说明可能通过两个前缀和相减得到指定的k
// 而记录了这各前缀和的次数，变避免了遍历

func subarraySum(nums []int, k int) int{
    ans := 0
    val dict = make(map[int]int{0:1})
    sums := 0
    for let i:=0;i < len(nums);i++{
        // 前缀和相加
        sums += nums[i]
        _, ok := dict[sums-k]
        if ok {
            ans += val
        }
        s_val, s_ok := dict[sums]
            if s_ok{
                dict[sums] = s_val + 1
            }else{
                dict[sums] = 1
            }
    }
    return ans
}
