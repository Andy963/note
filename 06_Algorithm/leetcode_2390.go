/**
 * File              : leetcode_2390.go
 * Author            : Andy
 * Date              : 2022.09.05
 * Last Modified Date: 2022.09.05
 * Last Modified By  : Andy
 */

package removeStarts

func removeStarts(s string) string {

	buf := make([]byte, 0)

	for i := 0; i < len(s); i++ {
		if s[i] == '*' {
			if len(buf) > 0 {
				buf = buf[:len(buf)-1]
			}
		} else {
			buf = append(buf, s[i])
		}
	}
	return string(buf)
}
