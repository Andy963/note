/**
 * File              : leetcode_011.go
 * Author            : Andy
 * Date              : 04.08.2022
 * Last Modified Date: 04.08.2022
 * Last Modified By  : Andy
 */


func max(x, y int) int{
	if x > y{
		return x
	}else{
		return y
	}
}

func min(x, y int) int{
	if x < y{
		return x
	}esle{
		return y
	}
}


func maxArea(height []int) int{
    ans := 0
	l, r := 0, len(height) - 1
	for l < r {
	     ans =  max(ans, min(height[l], height[r]) * (r -l))
		if height[l] < height[r]{
			l ++
		}else{
			r --
		}
	}
	return ans
}
