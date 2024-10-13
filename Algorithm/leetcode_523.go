/**
 * File              : leetcode_523.go
 * Author            : Andy
 * Date              : 31.07.2022
 * Last Modified Date: 31.07.2022
 * Last Modified By  : Andy
 */


func checkSubarraySum(nums []int, k int) bool {
    hash := map[int]int{0:-1}
    sum := 0
             for i, val := range nums {
                 sum += val
                     if k != 0{
                         sum = sum % k
                     }
                 if _, ok := hash[sum];ok{
                     if i - hash[sum] >= 2{
                         return true
                     }
                 }else{
                     hash[sum] = i
                 }
             }
             return false
}
