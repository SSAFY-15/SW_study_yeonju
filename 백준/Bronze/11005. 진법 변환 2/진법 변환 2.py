import sys
input = sys.stdin.readline

N, B = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
while N > 0:
    result.append(digits[N % B])   # 나머지를 문자로 변환
    N //= B                        # 몫 갱신
print(''.join(result[::-1]))       # 뒤집어서 출력