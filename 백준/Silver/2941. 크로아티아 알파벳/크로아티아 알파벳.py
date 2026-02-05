s = input()
i = 0
count = 0

while i < len(s):
    # 3글자 먼저 확인
    if s[i:i+3] == "dz=":
        i += 3
    # 2글자 확인
    elif s[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        i += 2
    # 일반 문자
    else:
        i += 1

    count += 1

print(count)