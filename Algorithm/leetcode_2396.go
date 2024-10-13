/**
 * File              : leetcode_2396.go
 * Author            : Andy
 * Date              : 2022.09.14
 * Last Modified Date: 2022.09.14
 * Last Modified By  : Andy
 */

package isStrictlyPalindromic

func convert(n, b int) int {
	rs := 0
	for n != 0 {
		rs += rs*b + n%b
		n /= b
	}
	return rs
}

func isStrictlyPalindromic(n int) bool {
	for i := 2; i < n; i++ {
		rs := convert(n, i)
		if rs != n {
			return false
		}
	}
	return true
}
