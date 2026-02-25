N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minusone = 0
zero = 0
one = 0

def divide(x, y, s):
    global minusone, zero, one
    basic = paper[x][y]
    same = True
    #만약 전부 같지 않다면
    for i in range(x, x+s):
        for j in range(y, y+s):
            if paper[i][j] != basic:
                same = False
                break
        if not same:
            break
    
    # 만약 전부 같다면 카운트+
    if same:
        if basic == -1:
            minusone += 1
        elif basic == 0:
            zero += 1
        else:
            one += 1
        return

    # 아니라면 3*3분할
    h = s//3
    divide(x, y, h)
    divide(x+h, y, h)
    divide(x+2*h, y, h)
    divide(x, y+h, h)
    divide(x+h, y+h, h)
    divide(x+2*h, y+h, h)
    divide(x, y+2*h, h)
    divide(x+h, y+2*h, h)
    divide(x+2*h, y+2*h, h)

# -1, 0, 1 개수 출력
divide(0, 0, N)
print(minusone)
print(zero)
print(one)