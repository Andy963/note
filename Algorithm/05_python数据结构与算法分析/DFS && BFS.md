leetcode 1609  <https://leetcode.cn/problems/even-odd-tree/>


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
            
        if not root:
            return
        
        stack = [root]
        level = 0
        max_val = 0
        while stack:
            size = len(stack)
            cur_level = []
            next_level = []
            flag = level % 2
            for i in range(size):
                cur = stack[i]
                # 当层为偶时，则元素必为奇
                if cur.val % 2 == flag:
                    return False
                # 如果当前值已经存在了，则示严格单调
                if cur.val in cur_level:
                    return False 
                # 奇数层, 偶数，递减
                if flag:
                    if cur_level and cur.val >= cur_level[-1]:
                        return False
                
                # 偶数层，奇数，递增
                if not flag:
                    if cur_level and cur.val <= cur_level[-1]:
                       return False 
                cur_level.append(cur.val)
                
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
                size -= 1
            stack = next_level
            level += 1
        return True
```

总体思路仍是层序遍历，然后是考虑每层的元素是否符合条件，比如单调递增，奇偶性等。

与之类似的但相对更简单的是： #### [剑指 Offer 32 - I. 从上到下打印二叉树](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            size = len(stack)
            next_level = []
            for i in range(size):
                cur = stack[i]
                ans.append(cur.val)

                if cur.left:
                    next_level.append(cur.left)

                if cur.right:
                    next_level.append(cur.right)
            stack = next_level
        return ans
```

对层做了奇偶处理的还有：#### [剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        stack = [root]
        level = 0
        ans = []
        while stack:
            cur_level = []
            next_level = []
            size = len(stack)
            flag = level % 2 == 0
            for i in range(size):
                cur = stack[i]
                if flag:
                    cur_level.append(cur.val)
                else:
                    cur_level.insert(0, cur.val)

                if cur.left:
                    next_level.append(cur.left)

                if cur.right:
                    next_level.append(cur.right)
            level += 1
            ans.append(cur_level)
            stack = next_level
        return ans

```


#### [剑指 Offer II 056. 二叉搜索树中两个节点之和](https://leetcode.cn/problems/opLdQZ/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        flag = False
        ans = []
        def dfs(node):
            nonlocal ans, flag
            if not node:
                return
            val = node.val
            if k - val in ans:
                flag = True
            else:
                ans.append(val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return flag
        
```