/**
 * File              : leetcode_560.go
 * Author            : Andy
 * Date              : 30.07.2022
 * Last Modified Date: 30.07.2022
 * Last Modified By  : Andy
 */

// 这个版本是看的别人的解题，觉得这个更简洁

func subarraySum(nums []int, k int) int{
    ans := 0
    val hash = make(map[int]int{0:1})
    sums := 0
    for let i:=0;i < len(nums);i++{
        // 前缀和相加
        sums += nums[i]
        // 这里可以用hash[sums-k] > 0 是因为如果它存在于hash中，则对应的值肯定大于0
            if hash[sums-k] > 0 {
                ans += hash[sums-k]
            }
            // 这里是我没想到的，这样直接++,是直接更新在hash上的
            hash[sums] ++
    }
    return ans
}
