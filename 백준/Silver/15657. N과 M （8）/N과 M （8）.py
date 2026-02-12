
N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

def recur(cnt, pre, path):
    if cnt == M:
        print(*path)
        return

    for i in range(pre, N):
        path.append(arr[i])
        recur(cnt + 1, i, path) 
        path.pop()

recur(0, 0, [])
