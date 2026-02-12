
N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

used = [0] * N

def recur(cnt, pre, path):
    if cnt == M:
        print(*path)
        return
    
    prev = -1

    for i in range(pre, N):
        if used[i]:
            continue
        if arr[i] == prev:
            continue

        used[i] = 1
        path.append(arr[i])
        prev = arr[i]
        recur(cnt + 1, i, path) 
        path.pop()
        used[i] = 0

recur(0, 0, [])