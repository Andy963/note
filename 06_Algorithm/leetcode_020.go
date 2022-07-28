/**
 * File              : leetcode_020.go
 * Author            : Andy
 * Date              : 28.07.2022
 * Last Modified Date: 28.07.2022
 * Last Modified By  : Andy
 */

// 主体思路：如果是左括号就入栈，如果是右括号，那么先看它是否与栈顶元素能配对，如果不能配对，那么则无效
// 如果能与栈顶元素配对，将栈顶元素出栈，这里通过切片模拟
// 如果一开始不是左括号，且栈为空，那么显示一开始给了右括号，直接返回false,否则len(stack)-1会出界

func isValid(s string) bool {
	// 用[]模拟栈
	var stack = []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] == '[' || s[i] == '(' || s[i] == '{' {
			stack = append(stack, s[i])
		} else {
			if len(stack) == 0 {
				return false
			} else if s[i] == ')' && stack[len(stack)-1] != '(' {
				return false
			} else if s[i] == ']' && stack[len(stack)-1] != '[' {
				return false
			} else if s[i] == '}' && stack[len(stack)-1] != '{' {
				return false
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}
	return len(stack) == 0
}
