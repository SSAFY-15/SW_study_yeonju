import sys
import heapq
input = sys.stdin.readline

# n: 지역 수, m: 수색 범위, r: 길 개수
n, m, r = map(int, input().split())

# 각 지역 아이템 수
items = list(map(int, input().split()))

# 그래프
graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, now = heapq.heappop(pq)

        if current_dist > dist[now]:
            continue

        for nxt, cost in graph[now]:
            new_dist = current_dist + cost
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

    return dist


answer = 0

for i in range(n):
    dist = dijkstra(i)

    total = 0
    for j in range(n):
        if dist[j] <= m:
            total += items[j]

    answer = max(answer, total)

print(answer)