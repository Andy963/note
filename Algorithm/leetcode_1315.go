/**
 * File              : leetcode_1315.go
 * Author            : Andy
 * Date              : 2022.09.08
 * Last Modified Date: 2022.09.08
 * Last Modified By  : Andy
 */

package sumEvenGrandparent

func dfs(node *TreeNode, ans *int){
    if node == nil {
        return
    }

    if node.Val % 2 == 0 {
        if node.Left != nil {
            if node.Left.Left != nil{
                *ans += node.Left.Left.Val
            }

            if node.Left.Right != nil {
                *ans += node.Left.Right.Val
            }
        }

        if node.Right != nil {
            if node.Right.Left != nil{
                *ans += node.Right.Left.Val
            }

            if node.Right.Right !+ nil {
                *ans += node.Right.Right.val
            }

        }
    }

    dfs(node.Left)
    dfs(node.Right)
}
func sumEvenGrandparent(root *TreeNode) int {
	ans := 0
    dfs(root, &ans)
    return ans
}
