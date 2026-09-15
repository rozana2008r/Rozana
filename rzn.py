#3.2 Python Graph Representation ]
graph = {
    "Astana":[("karaganda",2),("Pavlodar",4)],
    "Karaganda":[("Balkhash",5),("Shymkent",8)],
    "Pavlodar" : [("Semey",3)],
    "Semey": [("Taldykorgan",4)],
    "Balkhash": [("Almaty",5)],
    "Taldykorgan": [("Almaty",2)],
    "Shymkent": [("Almaty",3)],
    "Almaty":[]
    }

#Practical task 1
def dfs(graph,start, goal):
    stack=[(start,[start])]
    visited=set()
    expanded=[]

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)
        if node == goal:
            return path, expanded
        for neighbour, cost in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour,path + [neighbour]))
    return None, expanded

#Practical task 2
from collections import deque
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
     expanded = []
    while queue:
        node, path = queue.popleft()
        expanded.append(node)
        if node == goal:
            return path, expanded
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

#Practical task 3
import heapq
def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    expanded = []
    while frontier:
        g, node, path = heapq.heappop(frontier)
        if g != best_cost.get(node):
            continue
        expanded.append(node)
        if node == goal:
            return path, g, expanded
        for neighbour, step_cost in graph[node]:
            new_g = g + step_cost
            if new_g < best_cost.get(neighbour, float("inf")):
                best_cost[neighbour] = new_g
                heapq.heappush(frontier,
                                (new_g, neighbour, path + [neighbour]))
 return None, float("inf"), expanded

#Practical task 5
heuristic = { 
    "Astana": 10, 
    "Karaganda": 9, 
    "Pavlodar": 9, 
    "Balkhash": 5, 
    "Shymkent": 3, 
    "Semey": 6, 
    "Taldykorgan": 2, 
    "Almaty": 0 
} 
 
def astar(graph, start, goal, h): 
    frontier = [(h[start], 0, start, [start])] 
    best_g = {start: 0} 
    expanded = [] 
 
    while frontier: 
        f, g, node, path = heapq.heappop(frontier) 
 
        if g != best_g.get(node): 
            continue 
 
        expanded.append(node) 
 
        if node == goal: 
            return path, g, expanded 
 
        for neighbour, step_cost in graph[node]: 
            new_g = g + step_cost 
 
            if new_g < best_g.get(neighbour, float("inf")): 
                best_g[neighbour] = new_g 
                new_f = new_g + h[neighbour] 
                heapq.heappush(frontier, 
                               (new_f, new_g, neighbour, 
                                path + [neighbour])) 
 
    return None, float("inf"), expanded 

