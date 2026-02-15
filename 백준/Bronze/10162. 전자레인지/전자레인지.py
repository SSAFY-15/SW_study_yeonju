# T초
T = int(input())

# A B C 횟수
lst = [0] * 3

#버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초
ta = 5*60
tb = 1*60
tc = 10

lst[0] = T // ta
lst[1] = (T % ta) // tb
lst[2] = (T % tb) // tc

if T % tc == 0:
    print(*lst)
#제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1
else:
    print(-1)