/**
 * File              : leetcode_offer044.go
 * Author            : Andy
 * Date              : 2022.10.11
 * Last Modified Date: 2022.10.11
 * Last Modified By  : Andy
 */

package largestValues


func max(arr []int) int{
    maxVal := arr[0]
    for i:=1; i < len(arr); i++{
        if arr[i] > maxVal{
            maxVal = arr[i]
        }
    }
    return maxVal
}

func largestValues(root []*TreeNode) []int {
	if root == nil {
		return
	}

    stack := []*TreeNode{root}
    ans := []int{}

    while len(stack) != 0{
        curLevel := make([]int, 0)
        nextLevel := make([]*TreeNode, 0)

        size := len(stack)

        for size != 0; size --{
            cur := stack[size-1]
            stack := stack[:size-1]
            curLevel = append(cur.Val)
            if cur.Left != nil{
                nextLevel = append(nextLevel, cur.Left)
            }

            if cur.Right != nil{
                nextLevel = append(nextLevel, cur.Right)
            }
        }
        ans = append(ans, max(curLevel))
        stack = nextLevel
    }
    return ans
}
