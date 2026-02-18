def recur(n):
    if n == 0:
        return '-'
    prev = recur(n-1)
    space = ' ' * len(prev)
    
    return prev+space+prev

while True:
    try:
        N = int(input().strip())
        print(recur(N))
    except:
        break
        