# 시작점 : N
# 끝점 : 1
# 누적값 : n > 1 내려가는 숫자
def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num - 1)

N = int(input())
result = factorial(N)
print(result)
