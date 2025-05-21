from collections import defaultdict
import sys

#topological sorting recursively
def topological(v, visited, Stack, adj):
    visited[v] = True

    ##recur all verticies to this vertex
    for i in adj[v]:
        if (not visited[i[0]]):
            topological(i[0], visited, Stack, adj)
    Stack.append(v)

#find longest path using topological sorting
def longest_path():
    data = sys.stdin.read().splitlines()

    if not data:
        print("Nothing received.")
        return

    #Parse the first line for N(nodes) and M(edges)
    first_line = data[0].strip()
    
    N, M = map(int, first_line.split())

    #adjacency list
    adj = defaultdict(list)
    for i in range(1, M+1):
        u, v, w = map(int, data[i].strip().split())
        adj[u].append((v, w))

    visited = [False] * (N + 1)
    Stack = []

    for i in range(1, N+1):
        if not visited[i]:
            topological(i, visited, Stack, adj)
    
    #distance and path counts
    distance = [-float('inf')] * (N + 1) #negative infinity, not yet reachable, creates array size n+1
    count = [0] * (N + 1)
    distance[1] = 0 #distance to source is currently 0
    count[1] = 1 

    while Stack:
        u = Stack.pop()
        for v, w, in adj[u]:
            if distance[v] < distance[u] + w:
                distance[v] = distance[u] + w
                count[v] = count[u] #update longest path
            elif distance[v] == distance[u] + w:
                count[v] += count[u] 

    #output
    if distance[N] == -float('inf'):
        print("longest path:", distance[N])
        print("number of longest paths:", count[N])
    else:
        print(f"longest path: {distance[N]}")
        print(f"Number of longest paths: {count[N]}")

if __name__ == '__main__':
    longest_path()