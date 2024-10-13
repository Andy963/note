/**
 * File              : leetcode_326.go
 * Author            : Andy
 * Date              : 2022.08.26
 * Last Modified Date: 2022.08.26
 * Last Modified By  : Andy
 */

package isPowerOfThree

func isPowerOfThree(n int) bool {
	x := 1
	for x < n {
		x = x * 3
	}
	return x == n
}
