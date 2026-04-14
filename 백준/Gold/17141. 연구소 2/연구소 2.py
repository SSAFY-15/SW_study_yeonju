import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 최단 시간 > 조합 + BFS
# 모든 바이러스 동일하게 활성화
# 빈칸을 최소 시간으로 채우기

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 수집
virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
            
inf = int(1e9)
result = inf

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs로 최단 시간 구하기
def bfs(selected):
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    
    for x, y in selected:
        q.append((x, y))
        visited[x][y] = 0
    
    max_time = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N: 
                if visited[nx][ny] == -1 and lab[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    max_time = max(max_time, visited[nx][ny])
        
    # 모든 빈칸 확인
    for i in range(N):
        for j in range(N):
            if lab[i][j] != 1 and visited[i][j] == -1:
                return inf
                    
                    
    return max_time



# 조합으로 M개 선택
for comb in combinations(virus, M):
    time = bfs(comb)
    result = min(time, result)

# 결과
print(result if result != inf else -1)