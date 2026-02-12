
N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

used = [0] * N

def recur(cnt, path):
    if cnt == M:
        print(*path)
        return
    
    prev = -1

    for i in range(N):
        if used[i]:
            continue
        if arr[i] == prev:
            continue

        used[i] = 1
        path.append(arr[i])
        prev = arr[i]
        recur(cnt + 1, path) 
        path.pop()
        used[i] = 0

recur(0, [])
