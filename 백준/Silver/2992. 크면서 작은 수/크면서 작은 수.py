# import sys
# sys.stdin = open('input.txt', 'r')

num = list(input().strip())
n = len(num)
# 뒤에서부터 감소가 깨지는 지점 찾기
i = n - 2
while i >= 0 and num[i] >= num[i+1]:
    i -= 1
# 더 큰 수가 없는 경우
if i == -1:
    print(0)
else:
    # 뒤에서 num[i]보다 큰 가장 작은 수 찾기
    j = n-1
    while num[j] <= num[i]:
        j -= 1
    # swap
    num[i], num[j] = num[j], num[i]

    # 뒤쪽 정렬
    num[i+1:] = sorted(num[i+1:])

    print(int(''.join(num)))