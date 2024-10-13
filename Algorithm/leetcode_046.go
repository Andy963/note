/**
 * File              : leetcode_046.go
 * Author            : Andy
 * Date              : 2022.08.15
 * Last Modified Date: 2022.08.15
 * Last Modified By  : Andy
 */


func permute(nums []int) [][]int {
    var result [][]int
    var path []int
    used := make([]bool, len(nums))
    find(nums, len(nums), path, used, &result)
    return result
}


func (nums []int, n int, path []int, used []bool, result *[][]int){
    // 终止条件
    if len(path) == n {
        p := make([]int, len(path))
        copy(p, path)
        *result = append(*result, p)
        return
    }

    for i:=0;i<n;i++{
        if used[i] == true{
            continue
        }
        path = append(path, nums[i])
        used[i] = true
        find(nums, n, path, used, result)
        // 还原
        path = path[:len(path)-1]
        used[i] = false
    }
}
