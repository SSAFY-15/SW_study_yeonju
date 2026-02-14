N = int(input())
target = int(input())

arr = [[0]*N for _ in range(N)]

x = y = N//2
arr[x][y] = 1

num = 2
step = 1

#상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while num<=N*N:
    for d in range(4):
        for _ in range(step):
            if num > N*N:
                break

            x = x+dx[d]
            y = y+dy[d]
            arr[x][y] = num
            num+=1
        
        if d%2==1:
            step+=1

tx = ty = 0

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
        if arr[i][j] == target:
            tx, ty = i+1, j+1
    print()

print(tx, ty)