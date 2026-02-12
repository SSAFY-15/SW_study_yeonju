
N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

def recur(cnt, path):
    if cnt == M:
        print(*path)
        return

    for i in range(N):
        path.append(arr[i])
        recur(cnt + 1, path) 
        path.pop()

recur(0, [])
