N = int(input())
hints = [list(map(int, input().split())) for _ in range(N)]

count = 0

# 가능한 모든 3자리 수 생성
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or a == c:
                continue

            candidate = [a, b, c]
            valid = True

            # 모든 힌트와 비교
            for num, strike, ball in hints:
                s = str(num)
                guess = [int(s[0]), int(s[1]), int(s[2])]

                s_count = 0
                b_count = 0

                # 스트라이크 계산
                for i in range(3):
                    if candidate[i] == guess[i]:
                        s_count += 1

                # 볼 계산
                for i in range(3):
                    if candidate[i] != guess[i] and candidate[i] in guess:
                        b_count += 1

                if s_count != strike or b_count != ball:
                    valid = False
                    break

            if valid:
                count += 1

print(count)
