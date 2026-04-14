import sys
from itertools import combinations
from collections import deque
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 바이러스 M개를 활성화해서, 
# 모든 빈 칸(0)을 최소 시간에 퍼뜨려라

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
empty_cnt = 0

# 바이러스 위치 + 빈칸 개수
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            empty_cnt += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)
answer = INF


def bfs(selected):
    global answer

    visited = [[-1] * N for _ in range(N)]
    q = deque()

    for x, y in selected:
        q.append((x, y))
        visited[x][y] = 0

    filled = 0
    max_time = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    # 빈칸일 때만 시간 갱신
                    if lab[nx][ny] == 0:
                        filled += 1
                        max_time = visited[nx][ny]

                        # pruning (시간 초과 방지 핵심)
                        if max_time >= answer:
                            return INF

    # 모든 빈칸 채웠는지 확인
    if filled != empty_cnt:
        return INF

    return max_time


# # 예외: 빈칸이 아예 없는 경우
# if empty_cnt == 0:
#     print(0)
#     exit()

# 조합 + BFS
for comb in combinations(virus, M):
    result = bfs(comb)
    answer = min(answer, result)

print(answer if answer != INF else -1)
