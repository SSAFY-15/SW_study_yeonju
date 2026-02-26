from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# N
N= int(input())
paper = [list(map(int, input().strip())) for _ in range(N)]
# 방문 체크 배열 
visited = [[0] * N for _ in range(N)]

# bfs (현재 그림 하나의 넓이 계산)
def bfs(x, y):
    q = deque()
    q.append((x, y))
    # 시작점 방문 처리
    visited[x][y] = 1
    # 현재 그림 넓이
    area = 1

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            #아직 방문 안했고 그림(1)인 경우
            if not visited[nx][ny] and paper[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                area += 1
    return area

# 전체 격자를 순회
#   만약 방문 안 한 1 발견하면
#     BFS/DFS 시작
#     → 해당 그림 넓이 계산
#     → 그림 개수 +1

cnt = 0
total_area = []

for i in range(N):
    for j in range(N):
        # 새로운 그림 발견
        if paper[i][j] == 1 and not visited[i][j]:
            cnt += 1
            # BFS로 넓이 계산
            total_area.append(bfs(i, j))

print(cnt)
total_area.sort()
for i in range(len(total_area)):
    print(total_area[i])