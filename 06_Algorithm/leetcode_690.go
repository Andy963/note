/**
 * File              : leetcode_690.go
 * Author            : Andy
 * Date              : 2022.10.11
 * Last Modified Date: 2022.10.11
 * Last Modified By  : Andy
 */

package getImportance

func getImportance(employees []*Employee, id int) int {
	var hashmap map[int]*Employee
	total := 0
	stack := []int{id}
	for i := 0; i < len(employees); i++ {
		hashmap[employees[i].Id] = employees[i]
	}

	for len(stack) != 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		total += hashmap[cur].Importance
		for _, sub := range hashmap[cur].Subordinates {
			stack = append(stack, sub)
		}
	}
	return total
}
