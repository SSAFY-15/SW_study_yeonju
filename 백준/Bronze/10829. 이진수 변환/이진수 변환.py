def two(num):
    # 종료 조건
    if num < 2:
        return str(num)
    return two(num//2) + str(num % 2)

N = int(input())
print(two(N))
