s = input()
list = []
count = 0

S = len(s)
for i in range(S):
    list.append(s[i:S])

new_list = sorted(list)

for str in new_list:
    print(str)