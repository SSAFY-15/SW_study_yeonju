#잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

# 물건 가격
price = int(input())

# 거스름돈
change = 1000 - price

# 거스름돈 갯수
cnt = 0

cnt += change // 500
cnt += (change % 500) // 100
cnt += (change % 100) // 50
cnt += (change % 50) // 10
cnt += (change % 10) // 5
cnt += (change % 5) // 1

print(cnt)