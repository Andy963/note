/**
 * File              : leetcode_025.go
 * Author            : Andy
 * Date              : 26.07.2022
 * Last Modified Date: 26.07.2022
 * Last Modified By  : Andy
 */

package main

func getEnd(head *ListNode, k int) *ListNode {
	// 获取间隔k个元素后的end
	for head != nil {
		k--
		if k == 0 {
			break
		}
		// 右移
		head == head.next
	}
	return head
}

func reverseList(head *ListNode, end *ListNode) *ListNode {
	// TODO 不知道如果函数不返回值时这这里要怎么写
	// 所以这里随意的返回了一个head *ListNode类型
	if head == end {
		return head
	}
	last := head
	head = head.Next
	for head != end {
		// 保存下一个节点
		nextHead := head.Next
		// head.next 改变指向
		head.Next = last
		// last右移
		last = head
		// head 右移,事先保存好的nextHead
		head = nextHead
	}
	end.Next = last
	return end
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	// 创建个保护节点
	protect := ListNode(0, head)
	last := &protect
	for head != nil {
		end := getEnd(head, k)
		if end == nil {
			break
		}
		// 保存未反转前的下一组的开始，注意此时的下一组还未反转
		nextGroupHead := end.Next
		reverseList(head, end)
		// 反转后的end其实是当前组的开始位置
		last.Next = end
		// 反转后的head其实是当前组的结尾
		// 将当前组的结尾指向下一组的头部
		head.Next = nextGroupHead
		// last右移
		last = head
		// head右移
		head = nextGroupHead
	}
	return protect.Next
}

func main() {
	reverseKGroup
}
