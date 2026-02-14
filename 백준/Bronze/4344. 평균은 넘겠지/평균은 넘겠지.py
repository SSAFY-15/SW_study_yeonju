C = int(input())

for _ in range(C):
    lst = list(map(int, input().split()))
    N = lst[0]
    scores = lst[1:]

    avg = sum(scores)/N
    cnt = 0

    for score in scores:
        if score > avg:
            cnt += 1
    
    result = cnt/N*100
    print(f'{result:.3f}%')