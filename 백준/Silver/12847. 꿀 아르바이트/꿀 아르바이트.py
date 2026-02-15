N, M = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:M])
max_sum = window_sum

for i in range(M, N):
    window_sum += arr[i]
    window_sum -= arr[i-M]
    max_sum = max(max_sum, window_sum)

print(max_sum)