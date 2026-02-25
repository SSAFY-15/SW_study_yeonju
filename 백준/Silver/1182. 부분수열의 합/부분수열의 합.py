# import sys
# sys.stdin = open('input.txt', 'r')

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def dfs(x, total):
    global cnt
    # 모든 원소에 대해 선택 여부 결정 완료
    if x == N:
        if total == S:
            cnt += 1
        return
    # 선택
    dfs(x + 1, total + arr[x])
    # 미선택
    dfs(x + 1, total)
dfs(0, 0)

# 공집합 제거
if S == 0:
    cnt -= 1

print(cnt)