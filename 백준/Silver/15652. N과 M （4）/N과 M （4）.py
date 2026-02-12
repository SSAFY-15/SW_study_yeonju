
N, M = map(int, input().split())

arr = list(range(1, N + 1))

def recur(cnt, pre, path):
    if cnt == M:
        print(*path)
        return

    for i in range(pre, N):
        path.append(arr[i])
        recur(cnt + 1, i, path) 
        path.pop()

recur(0, 0, [])
