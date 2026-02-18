N = int(input())
cnt = 0

for _ in range(N):
    words = input().strip()
    stack = []
    
    for w in words:
        # 문자가 쌍을 이루면 
        if stack and stack[-1] == w:
            stack.pop()
        # 그렇지 않으면
        else:
            stack.append(w)
        
    if not stack:
        cnt += 1
print(cnt)