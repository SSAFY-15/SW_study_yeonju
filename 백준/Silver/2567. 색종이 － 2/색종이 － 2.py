N = int(input())

paper = [[0] * 102 for _ in range(102)]  # 테두리 여유

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

perimeter = 0

for i in range(1, 101):
    for j in range(1, 101):
        if paper[i][j] == 1:
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]

                if paper[ni][nj] == 0:
                    perimeter += 1

print(perimeter)
