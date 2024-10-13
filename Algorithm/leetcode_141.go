/**
 * File              : leetcode_141.go
 * Author            : Andy
 * Date              : 27.07.2022
 * Last Modified Date: 27.07.2022
 * Last Modified By  : Andy
 */

/*
主体思路：如果有环，两个指针在跑的时候会出现快的追上慢的情况，
边界问题是：fast不能为空，且fast.Nextb也不能为空
*/

func hasCycle(head *ListNode) bool {
	var fast = head
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		head = head.Next
		if fast == head {
			return true
		}
	}
	return false
}

func main() {
	hasCycle(head)
}
