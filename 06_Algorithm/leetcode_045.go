/**
 * File              : leetcode_045.go
 * Author            : Andy
 * Date              : 2022.09.26
 * Last Modified Date: 2022.09.26
 * Last Modified By  : Andy
 */

 package findBottomLeftVal


 func findBootomLeftVal(root *TreeNode){
     var bfs(node *TreeNode) int
     bfs = func(node *TreeNode)int{
         if node == nil {
             return 0
         }else{
             stack := make([]*TreeNode, 0)

             if len(stack) != 0{
                 level := make([[]]*TreeNode, 0)
                 next_level := make([]*TreeNode, 0)

                 for _, s := range stack{
                     level = append(level, s)

                     if s.Left != nil{
                        next_level = append(next_level, s.Left)
                     }

                     if s.Right != nil {
                         next_level = append(next_level, s.Right)
                     }
                 }

                 if len(next_level) == 0{
                     return level[0].Val
                 }

                 stack := make([]*TreeNode,0)
                 for index := range next_level {
                     stack = append(stack, next_level[index])
                 }
             }
         }
     }
    return bfs(root)
 }
