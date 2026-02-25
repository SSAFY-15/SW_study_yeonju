N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def color(x, y, s):
    global white
    global blue
    wb = paper[x][y]
    same = True

    # 색종이 색깔이 같은지 전체 확인
    for i in range(x, x+s):
        for j in range(y, y+s):
            if paper[i][j] != wb:
                same = False
                break
        if not same:
            break
    # 만약 색깔이 같다면 카운트+
    if same:
        if wb == 0:
            white += 1
        else:
            blue += 1
        return
    # 색깔이 같지 않다면 4분할
    h = s//2
    color(x, y, h)
    color(x+h, y, h)
    color(x, y+h, h)
    color(x+h, y+h, h)

color(0, 0, N)
print(white)
print(blue)