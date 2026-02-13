from collections import deque

N, M, V = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

def bfs(start):
    # 초기화
    dq = deque([start])
    visited = [0] * (N + 1)
    visited[start] = 1
    print(start, end=' ')

    while dq:
        now = dq.popleft()
        # visited[now] = 1

        for next_node in graph[now]:
            # 이미 방문한 노드라면 continue
            if visited[next_node]:
                continue

            print(next_node, end=' ')
            visited[next_node] = 1
            dq.append(next_node)

def dfs(node):
    print(node, end=' ')

    for next_node in graph[node]:
        if visited[next_node]:
            continue

        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

visited = [0] * (N + 1)
visited[V] = 1
dfs(V)
print()
bfs(V)
