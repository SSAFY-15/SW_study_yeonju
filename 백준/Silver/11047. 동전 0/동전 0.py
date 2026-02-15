# N, K
N, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
cnt = 0
price = K

for i in range(N-1, -1, -1):
    cnt += price // arr[i]
    price = price % arr[i]

print(cnt)