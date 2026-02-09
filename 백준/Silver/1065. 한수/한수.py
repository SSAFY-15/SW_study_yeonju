N = int(input())
count = 0

for num in range(1, N + 1):
    s = str(num)
    
    # 두 자리 수 이하는 모두 한수
    if len(s) <= 2:
        count += 1
    else:
        diff = int(s[1]) - int(s[0])
        is_hansu = True
        
        for i in range(1, len(s) - 1):
            if int(s[i + 1]) - int(s[i]) != diff:
                is_hansu = False
                break
        
        if is_hansu:
            count += 1

print(count)
