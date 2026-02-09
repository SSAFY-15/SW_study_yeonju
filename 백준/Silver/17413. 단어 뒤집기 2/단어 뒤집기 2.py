s = input()

stack = []
result = ""
in_tag = False

for ch in s:
    if ch == '<':
        while stack:
            result += stack.pop()
        in_tag = True
        result += ch

    elif ch == '>':
        in_tag = False
        result += ch

    elif in_tag:
        result += ch

    elif ch == ' ':
        while stack:
            result += stack.pop()
        result += ' '

    else:
        stack.append(ch)

# 마지막 처리
while stack:
    result += stack.pop()

print(result)
