# tc 번호
tc = 1

while True:

    # L, P, V
    L, P, V = map(int, input().split())

    # 종료 조건
    if L == 0 and P == 0 and V == 0:
        break

    # 캠핑장 이용 횟수
    cnt = 0

    if V % P >= L:
        cnt2 = L
    else:
        cnt2 = V % P

    cnt = (V // P) * L + cnt2


    print(f'Case {tc}: {cnt}')
    tc += 1