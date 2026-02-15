# N
N = int(input())

result = -1

for i in range(N//5, -1, -1):
    remain = N - (i*5)

    if remain % 3 == 0:
        result = i + (remain // 3)
        break

print(result)