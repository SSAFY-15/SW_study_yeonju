import sys
input = sys.stdin.readline

N, P = map(int, input().split())          
stacks = [[] for _ in range(7)]           
count = 0                                 

for _ in range(N):
    line, fret = map(int, input().split())  

    # 현재 줄에서 더 높은 프렛은 모두 떼기
    while stacks[line] and stacks[line][-1] > fret:
        stacks[line].pop()
        count += 1

    # 같은 프렛이면 아무 것도 안 함
    if stacks[line] and stacks[line][-1] == fret:
        continue

    # 새로운 프렛 누르기
    stacks[line].append(fret)
    count += 1

print(count)                               