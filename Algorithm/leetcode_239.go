/**
 * File              : leetcode_239.go
 * Author            : Andy
 * Date              : 06.08.2022
 * Last Modified Date: 2022.08.06
 * Last Modified By  : Andy
 */


func  maxSlidingWindow(nums []int, k int) []int{
	result := []
	q := make([]int,0)
	for  i:=0; i < len(nums); i++{
		// 窗口左侧的元素不要
		for q && q[0] <= i-k{
			q = q[1:]
		}
		// 将队列中元素比当前元素小的移除
		for q && nums[q[len(q)-1]] <= nums[i]{
			q = q[:len(q)-1]
		}
		// 最终剩下的元素入栈
		q = append(q, i)

		// 当遍历到下一个窗口开始时,将当前窗口中的最大值入栈
		if i >= k-1{
			result = append(result, nums[q[0]])
		}
	}
    return result
}
