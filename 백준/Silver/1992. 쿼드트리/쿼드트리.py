N = int(input())
arr = [list(input().strip()) for _ in range(N)]

def recur(x, y, s):
    first = arr[x][y]
    for i in range(x, x+s):
        for j in range(y, y+s):
            if arr[i][j] != first:
                half = s // 2
                print('(', end='')
                
                #4분할 재귀호출
                recur(x, y, half)
                recur(x, y+half, half)
                recur(x+half, y, half)
                recur(x+half, y+half, half)
                
                print(')', end='')
                return
    print(first, end='')     

recur(0, 0, N)