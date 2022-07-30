/**
 * File              : leetcode_930.go
 * Author            : Andy
 * Date              : 30.07.2022
 * Last Modified Date: 30.07.2022
 * Last Modified By  : Andy
 */


func numSubarraysWithSum(nums []int, goal int) int{
    count, sum := 0, 0
    hash := map[int]int{0:1}
    for i:=0;i<len(nums);i++{
        sum += nums[i]
            if hash[sum-goal] > 0 {
                count += hash[sum-goal]
            }
            hash[sum] ++
    }
    return count
}
