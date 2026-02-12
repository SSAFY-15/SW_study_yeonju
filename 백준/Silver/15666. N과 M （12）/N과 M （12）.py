
N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

used = [0] * N

def recur(cnt, pre, path):
    if cnt == M:
        print(*path)
        return
    
    prev = -1

    for i in range(pre, N):

        if arr[i] == prev:
            continue
        path.append(arr[i])
        prev = arr[i]
        recur(cnt + 1, i, path) 
        path.pop()


recur(0, 0, [])