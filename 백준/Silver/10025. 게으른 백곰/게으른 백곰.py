N, K = map(int, input().split())
arr = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g

r = 2*K+1
a = sum(arr[:r])
max_num = a
for i in range(len(arr)-r):
    a = a + arr[i+r] - arr[i]
    max_num = max(a, max_num)

print(max_num)