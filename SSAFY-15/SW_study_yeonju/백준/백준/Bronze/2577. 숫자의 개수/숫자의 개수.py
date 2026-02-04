A = int(input())
B = int(input())
C = int(input())

# A × B × C
num = A * B * C
# 문자열 변환
num_str = str(num)
# 횟수 세기
for i in range(10):
    print(num_str.count(str(i)))

# -------------------
# # 내장함수 제외

# A = int(input())
# B = int(input())
# C = int(input())

# num = A * B * C
# count = [0] * 10

# while num > 0:
#     digit = num % 10
#     count[digit] += 1
#     num //= 10

# for i in range(1, 10):
#     print(count[i])