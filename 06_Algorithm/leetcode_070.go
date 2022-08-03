/**
 * File              : leetcode_070.go
 * Author            : Andy
 * Date              : 03.08.2022
 * Last Modified Date: 03.08.2022
 * Last Modified By  : Andy
 */

// 这题是否通过缓存lru_cache的方式来缩短计算时间呢？

func climbStairs(n int) int{
f := make([]int,n+1)
	   f[0] = f[1] = 1
	   for i:=2;i<=n;i++{
		   f[i] = f[i-1] + f[i-2]
	   }
   return f[n]
}
