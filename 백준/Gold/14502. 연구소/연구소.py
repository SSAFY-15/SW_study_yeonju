from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]   
dy = [0, 0, -1, 1]

# 빈칸 위치
# 바이러스 위치
empty = []           
virus = []          

# 빈칸과 바이러스 위치 저장
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

ans = 0


def bfs(temp):
    q = deque(virus)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    q.append((nx, ny))

    safe = 0
    for i in range(N):
        safe += temp[i].count(0)

    return safe


# 빈칸 중 3개를 벽으로 선택
for walls in combinations(empty, 3):

    temp = [row[:] for row in board]

    # 벽 설치
    for x, y in walls:
        temp[x][y] = 1

    ans = max(ans, bfs(temp))

print(ans)