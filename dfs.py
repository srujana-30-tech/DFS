from collections import deque
graph={
    1:[2,3,4],
    2:[5,6],
    3:[],
    4:[7],
    5:[],
    6:[],
    7:[]
    }
def dfs(start,goal):
    stack=[]
    stack.append((start,[start]))
    while stack:
        node,path = stack.pop()
        print(f"Visiting Node:{node}")
        if node==goal:
            print(f"Goal node {node} found!!")
            print(f"Path:","->".join(map(str,path)))
            return
        for neighbour in graph[node]:
            stack.append((neighbour,path+[neighbour]))
    print("Goal not found")
    return
print("DFS search with path:")
dfs(1,7)
    