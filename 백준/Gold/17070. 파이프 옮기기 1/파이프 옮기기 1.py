N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

memo = [[[-1]*3 for _ in range(N)] for _ in range(N)]

def dfs(r, c, d):

    # 도착
    if r == N-1 and c == N-1:
        return 1

    # 이미 계산된 상태
    if memo[r][c][d] != -1:
        return memo[r][c][d]

    ways = 0

    # 가로
    if d == 0:
        if c+1 < N and board[r][c+1] == 0:
            ways += dfs(r, c+1, 0)

        if r+1 < N and c+1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            ways += dfs(r+1, c+1, 2)

    # 세로
    elif d == 1:
        if r+1 < N and board[r+1][c] == 0:
            ways += dfs(r+1, c, 1)

        if r+1 < N and c+1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            ways += dfs(r+1, c+1, 2)

    # 대각선
    else:
        if c+1 < N and board[r][c+1] == 0:
            ways += dfs(r, c+1, 0)

        if r+1 < N and board[r+1][c] == 0:
            ways += dfs(r+1, c, 1)

        if r+1 < N and c+1 < N and board[r][c+1] == 0 and board[r+1][c] == 0 and board[r+1][c+1] == 0:
            ways += dfs(r+1, c+1, 2)

    memo[r][c][d] = ways
    return ways


print(dfs(0, 1, 0))