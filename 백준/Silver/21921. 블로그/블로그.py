# N, X, visitor
N, X = map(int, input().split())
visitor = list(map(int, input().split()))

# 첫 윈도우 값으로 초기화
window = sum(visitor[:X])
max_sum = window
count = 1

# 합계 중 최대값 구하기
for i in range(len(visitor) - X):
    window = window - visitor[i] + visitor[i + X]
    if window > max_sum:
        max_sum = window
        count = 1
    elif window == max_sum:
        count += 1
        
if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)
