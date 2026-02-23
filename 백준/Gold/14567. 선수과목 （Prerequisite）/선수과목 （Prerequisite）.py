from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]   
indegree = [0] * (N + 1)             
semester = [0] * (N + 1)             

# 선수과목 관계 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 큐 초기화 (선수과목 없는 과목들)
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        semester[i] = 1              

# BFS
while q:
    now = q.popleft()

    for nxt in graph[now]:
        indegree[nxt] -= 1
        semester[nxt] = max(semester[nxt], semester[now] + 1)

        if indegree[nxt] == 0:
            q.append(nxt)

print(*semester[1:])