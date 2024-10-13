/**
 * File              : leetcode_155.go
 * Author            : Andy
 * Date              : 27.07.2022
 * Last Modified Date: 27.07.2022
 * Last Modified By  : Andy
 */


/**
主体思路：保存两个栈，一个正常存数据，另一个存最小前缀栈，即当前值是前面几个数中的最小值
getMin即是从这个最小前缀中取值即可
*/

type MinStack struct {
    stack []int 
    minStack []int
}

func Constructor() MinStack{
    return MinStack{
        stack: []int{},
        minStack: []int{math.MaxInt64},
    } 
}

func (this *MinStack) Push(val int){
    this.stack = append(this.stack, val)
    top := this.minStack[len(this.minStack)-1]
    this.minStack = append(this.minStack, min(val, top))
}

func (this *MinStack) Pop() {
    this.stack = this.stack[:len(this.stack)-1]
    this.minStack = this.minStack[:len(this.minStack)-1]
}

func (this *MinStack) top() {
    return this.stack[len(this.stack)-1]
}

func (this *MinStack) getTop(){
    return this.minStack[len(this.minStack)-1]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
