GoInstallBinaries/**
 * File              : leetcode_974.go
 * Author            : Andy
 * Date              : 01.08.2022
 * Last Modified Date: 01.08.2022
 * Last Modified By  : Andy
 */


func subarrayDivByK(nums []int, k int) int {
    count, preSum := 0, 0
    dic := map[int]int{0:1} // 初始化记录余数出现的次数
    for i:=0; i < len(nums); i++{
        preSum += nums[i]
        res := (preSum % k + k) % k
        if dic[res] > 0{
            dic[res] ++
        }else{
            dic[res] = 1
        }
    }
    for _, val := range dic{
        if val > 1{
            count += val(val -1) / 2
        }
    }
    return count
}
