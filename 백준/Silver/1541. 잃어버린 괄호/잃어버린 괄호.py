parts = input().split('-')
lst = []

for part in parts:
    s = sum(map(int, part.split('+')))
    lst.append(s)

result = lst[0]
for i in lst[1:]:
    result -= i

print(result)
