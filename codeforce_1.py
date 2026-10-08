1

# import sys
# from collections import deque

# def solve():
#     data = sys.stdin.read().split()
#     n = int(data[0])
#     p = [int(x) for x in data[1:n + 1]]

#     children = [[] for _ in range(n + 1)]
#     roots = []

#     for i in range(1, n + 1):
#         parent = p[i - 1]
#         if parent == -1:
#             roots.append(i)
#         else:
#             children[parent].append(i)

#     max_depth = 0
#     for root in roots:
#         queue = deque([(root, 1)]) 
#         while queue:
#             v, depth = queue.popleft()
#             if depth > max_depth:
#                 max_depth = depth
#             for child in children[v]:
#                 queue.append((child, depth + 1))

#     print(max_depth)

# solve()

2

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    f = [0] + [int(x) for x in input_data[1:n+1]]
    
    for i in range(1, n + 1):
        first = f[i]
        second = f[first]
        third = f[second]
        
        if third == i:
            print("YES")
            return
            
    print("NO")

if __name__ == '__main__':
    solve()

3 

import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    cats = [0] + [int(x) for x in input_data[2:n+2]]
    
    adj = [[] for _ in range(n + 1)]
    idx = n + 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    queue = deque()
    queue.append((1, 0, cats[1]))
    
    valid_leaves = 0
    
    while queue:
        v, p, consec = queue.popleft()
        
        if consec > m:
            continue
            
        is_leaf = True
        for to in adj[v]:
            if to != p:
                is_leaf = False
                next_consec = consec + 1 if cats[to] == 1 else 0
                queue.append((to, v, next_consec))
                
        if is_leaf:
            valid_leaves += 1
            
    print(valid_leaves)

if __name__ == '__main__':
    solve()

4

import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
            
        color = [-1] * (n + 1)
        color[1] = 0
        
        queue = deque([1])
        
        while queue:
            v = queue.popleft()
            c = color[v]
            
            for to in adj[v]:
                if color[to] == -1:
                    color[to] = 1 - c
                    queue.append(to)
                    
        count0 = sum(1 for i in range(1, n + 1) if color[i] == 0)
        count1 = n - count0
        
        target_color = 0 if count0 <= count1 else 1
        
        ans = [str(i) for i in range(1, n + 1) if color[i] == target_color]
        
        out.append(str(len(ans)))
        out.append(" ".join(ans))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()

5 

import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        idx += 3
        
    INF = 10**18
    dist = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, v = heapq.heappop(pq)
        
        if d > dist[v]:
            continue
            
        if v == n:
            break
            
        for to, weight in adj[v]:
            if dist[v] + weight < dist[to]:
                dist[to] = dist[v] + weight
                parent[to] = v
                heapq.heappush(pq, (dist[to], to))
                
    if dist[n] == INF:
        print("-1")
    else:
        path = []
        curr = n
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        print(" ".join(map(str, path)))

if __name__ == '__main__':
    solve()