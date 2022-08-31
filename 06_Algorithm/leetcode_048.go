/**
 * File              : leetcode_048.go
 * Author            : Andy
 * Date              : 2022.08.31
 * Last Modified Date: 2022.08.31
 * Last Modified By  : Andy
 */

package rotate

func transpost(matrix *[][]int) {
	rows := len(*matrix)
	cols := len((*matrix)[0])
	for i := 0; i < rows; i++ {
		for j := i + 1; j < cols; j++ {
			item := (*matrix)
			item[i][j], item[j][i] = item[j][i], item[i][j]
		}
	}
}

func reverse(matrix, *[][]int) {
	rows := len((*matrix))
	for i := 0; i < rows; i++ {
		tmp := (*matrix)[i]
		// 倒置有点麻烦
		for m, n := 0, len(tmp)-1; m < n; m, n = m+1, n-1 {
			tmp[m], tmp[n] = tmp[n], tmp[m]
		}
	}
}

func rotate(matrix [][]int) {
	transpost(&matrix)
	reverse(&matrix)
}
