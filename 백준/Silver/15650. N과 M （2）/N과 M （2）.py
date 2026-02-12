N, M = map(int, input().split())

arr = list(range(1, N + 1))

def recur(start, path):
    if len(path) == M:
        print(*path)
        return

    for i in range(start, N):
        path.append(arr[i])
        recur(i + 1, path)  # 다음 숫자부터 선택
        path.pop()

recur(0, [])