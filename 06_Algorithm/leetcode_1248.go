/**
 * File              : leetcode_1248.go
 * Author            : Andy
 * Date              : 30.07.2022
 * Last Modified Date: 30.07.2022
 * Last Modified By  : Andy
 */

// 这题与前面560，930不同之处在于需要对数据进行预先处理，将奇数转成1，偶数转成0
// 当然这个题也可以出成偶数的，道理是一样的

func numberOfSubarrays(nums []int, k int) int{
    count, sum := 0, 0
    hash := map[int]int{0:1}
    for i:=0;i<len(nums); i++{
        nums[i] = nums[i] % 2
        sum += nums[i]
        if hash[sum-k] > 0 {
            count += hash[sum-k]
        }
        hash[sum] ++
    }
    return count
}
