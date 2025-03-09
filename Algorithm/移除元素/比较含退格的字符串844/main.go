/*
 * File              : main.go
 * Author            : Andy963
 * Created time      : 2024-12-07 21:15:50
 * Last Modified by  : Andy963
 * Last Modified time: 2024-12-07 21:39:59
 */
package main

import "fmt"

func getStr(s string) string {
	rs := []rune{}
	for _, c := range s {
		if c != '#' {
			rs = append(rs, c)
		} else {
			if len(rs) > 0 {
				rs = rs[:len(rs)-1]
			}
		}
	}
	return string(rs)
}

func main() {
	s := "ab#c"
	t := "ad#c"
	if getStr(s) == getStr(t) {
		fmt.Println(true)
	} else {
		fmt.Println(false)
	}
}
