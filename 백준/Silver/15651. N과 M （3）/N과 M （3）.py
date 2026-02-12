N, M = map(int, input().split())

arr = list(range(1, N + 1))

def recur(cnt, path):
    if cnt == M:
        print(*path)
        return

    for i in range(N):
        path.append(arr[i])
        recur(cnt + 1, path) 
        path.pop()

recur(0, [])
