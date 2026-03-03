import heapq

N = int(input())         
M = int(input())         
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))  
start_city, end_city = map(int, input().split())

# 거리 배열 초기화
INF = int(1e9)
distance = [INF] * (N + 1)

def recur(start):
    pq = []
    heapq.heappush(pq, (0, start))  
    distance[start] = 0

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # 이미 더 짧은 경로가 있으면 무시
        if current_cost > distance[current_node]:
            continue

        for next_node, next_cost in graph[current_node]:
            new_cost = current_cost + next_cost

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))

recur(start_city)
print(distance[end_city])