import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)

result = 0

for c in N:
    if c.isdigit():                # 숫자
        value = int(c)
    else:                          # 문자 A~Z
        value = ord(c) - ord('A') + 10
    
    result = result * B + value    # 진법 변환

print(result)