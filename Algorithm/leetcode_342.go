/**
 * File              : leetcode_342.go
 * Author            : Andy
 * Date              : 2022.08.29
 * Last Modified Date: 2022.08.29
 * Last Modified By  : Andy
 */

package isPowerOfFour

import "math"

func isPowerOfFour(n int) bool {
	for i := 0; i < 16; i++ {
		if n == int(math.Pow(4, float64(i))) {
			return true
		}
	}
	return false
}
