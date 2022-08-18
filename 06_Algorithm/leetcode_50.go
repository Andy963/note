/**
 * File              : leetcode_50.go
 * Author            : Andy
 * Date              : 2022.08.18
 * Last Modified Date: 2022.08.18
 * Last Modified By  : Andy
 */

package Pow

func myPow(x float64, n int) float64 {
	if n == 0 {
		return 1
	}

	if n < 0 {
		return 1 / myPow(x, -n)
	}

	if n%2 != 0 {
		return x * myPow(x, n-1)
	} else {
		return myPow(x*x, n/2)
	}
}
