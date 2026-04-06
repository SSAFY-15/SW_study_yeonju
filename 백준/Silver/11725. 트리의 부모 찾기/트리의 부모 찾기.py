import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

# 인접 리스트
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 저장 배열
parent = [0] * (N + 1)

# BFS
queue = deque([1])
parent[1] = -1  # 루트 표시

while queue:
    current = queue.popleft()
    
    for next_node in graph[current]:
        if parent[next_node] == 0:  # 방문 안 했으면
            parent[next_node] = current
            queue.append(next_node)

# 2번 노드부터 출력
for i in range(2, N + 1):
    print(parent[i])