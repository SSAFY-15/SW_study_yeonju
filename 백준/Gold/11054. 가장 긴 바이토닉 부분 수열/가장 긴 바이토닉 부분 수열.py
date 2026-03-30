# 11053 기존 문제(증가)에서 (증가 + 감소)로 추가

N = int(input())
arr = list(map(int, input().split()))

# 증가
inc = [1] * N
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            inc[i] = max(inc[i], inc[j]+1)

# 감소
dec = [1] * N
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[j] < arr[i]:
            dec[i] = max(dec[i], dec[j]+1)

# 증가+감소
result = 0
for i in range(N):
    result = max(result, inc[i] + dec[i]-1)

print(result)