N, M = map(int, input().split())          # 보드 크기 입력

arr = [list(input().strip()) for _ in range(N)]  # 문자열로 입력

result = []

for r in range(N - 7):                    # 8x8 시작 행
    for c in range(M - 7):                # 8x8 시작 열

        cnt1 = 0                          # W로 시작하는 경우
        cnt2 = 0                          # B로 시작하는 경우

        for i in range(8):
            for j in range(8):

                # W로 시작하는 체스판 기준
                if (i + j) % 2 == 0:      # 짝수 칸
                    if arr[r+i][c+j] != 'W':
                        cnt1 += 1
                    if arr[r+i][c+j] != 'B':
                        cnt2 += 1
                else:                     # 홀수 칸
                    if arr[r+i][c+j] != 'B':
                        cnt1 += 1
                    if arr[r+i][c+j] != 'W':
                        cnt2 += 1

        result.append(min(cnt1, cnt2))    # 더 작은 값 저장

print(min(result))                        # 전체 최소 출력
