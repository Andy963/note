# BFS & DFS

```python
graph = {
    "A":["B","B"],
    "B":["A","C",'D'],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def BFS(graph,s):
    queue = []
    seen = set()
    seen.add(s)
    queue.append(s)
    while len(queue) >0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)

def DFS(graph,s):
    stack = []
    seen = set()
    seen.add(s)
    stack.append(s)
    while len(stack) >0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)

if __name__ == '__main__':
    BFS(graph,'E')
```