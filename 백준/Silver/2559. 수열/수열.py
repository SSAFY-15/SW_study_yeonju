N, K = map(int, input().split())
arr = list(map(int, input().split()))

s = sum(arr[:K])
max_sum = s

for i in range(N-K):
    s = s + arr[i+K] - arr[i]
    max_sum= max(s, max_sum)
print(max_sum)