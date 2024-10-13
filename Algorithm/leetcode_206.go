/**
 * File              : leetcode_206.go
 * Author            : Andy
 * Date              : 24.07.2022
 * Last Modified Date: 24.07.2022
 * Last Modified By  : Andy
 */

// 主体思路：把每一个节点换个方向指
// 但要注意，不能直接改，要先把下一个节点通过中间节点保存起来，否则整个的断了
// 头节点指向空节点，
// 最后一个节点也向右移动
// 下一个节点向右移（事先保存好了）
// 这个go版本竟然打败100%，击败99.94

package main


import "fmt"

func reverseList(head *ListNode) *ListNode{
    var last *ListNode // 这里应该是使用了如果未赋初值会有默认值
        for head != nil{
            next_head := head.Next
            head.next = last
            last = head
            head = next_head
        }
        return last
}

func main() {
    reverseList(head)
}
