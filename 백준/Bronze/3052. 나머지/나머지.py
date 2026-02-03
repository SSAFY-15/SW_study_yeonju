# 수 입력 후 리스트 변환
nums = [int(input()) for _ in range(10)]

# 42로 나눈 나머지를 리스트로 변환
new_list = []

for n in nums:
    new_list.append(n % 42)

# 서로 다른 값 카운팅 및 출력
unique = []

for num in new_list:
    if num not in unique:
        unique.append(num)

print(len(unique))