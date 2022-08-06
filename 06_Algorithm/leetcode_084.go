/**
 * File              : leetcode_084.go
 * Author            : Andy
 * Date              : 06.08.2022
 * Last Modified Date: 06.08.2022
 * Last Modified By  : Andy
 */
package main


func max(x, y int) int {
	if x > y{ return x }
	return y
}

func maxRectangeArea(heights [int]) int{
	maxVal := 0
	stack := make([]int, len(heights)+1)
	stack[0] = 1
	// 1. 先得到一个单调递增的栈
	for i:=0; i < len(heights); i++{
		// 前面有比当前高度高的元素都要出栈
		for stack[0] != -1 && heights[i] <= heights[len(stack)-1]{
			// 获取栈顶元素,即当前高度
			top := stack[len(stack)-1]
			// 把栈顶元素出栈
			stack = stack[:len(stack)-1]
			// 当前最大值与 由当前高度与宽度组成的矩形的面积对比,更新
			maxVal = max(maxVal, heights[top] * (i - stack[len(stack) -1] -1))
		}
	}
	// 从这个单调递增栈中计算最大高度
	for stack[len(stack)-1] != -1{
			top := stack[len(stack) -1 ]
			stack = stack[:len(stack)-1]
			maxVal = max(maxVal, heights[top] * (i - stack[len(stack) -1] -1))
		}
    rerun maxVal	
}
