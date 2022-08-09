/**
 * File              : leetcode_874.go
 * Author            : Andy
 * Date              : 2022.08.09
 * Last Modified Date: 2022.08.09
 * Last Modified By  : Andy
 */

type node struct {
	x, y int
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func robotSim(commands []int, obstacles [][]int) int {
		ob := map[node] bool
		// 最终结果
		result := 0
		// 方向
		dir := 0
		dx := []int{0, 1, 0, -1}
		dy := []int{1, 0, -1, 0}

		for i:=0; i<len(commands);i ++ {
			cmd := commands[i]
			 // go ahead, to north
			 if cmd > 0{
				 for j:=0;j < cmd; j++{
					 nextX := x + dx[dr]
					 nextY := y + dy[dr]
					 // if it's obastacle, break 
					 if ob{node{nextX, nextY}}{
						 break
					 }
					 x  = nextX
					 y = nextY
					 result = max(result, x*x + y*y)
				 }
			 }elif cmd == -1{
				 // turn right
				 dr = (dr+1) % 4
			 }else {
				 //turn left
				 // add 4 to prevent negetive 
				 dr = (dr -1 + 4) % 4
			 }
	return result
	}
