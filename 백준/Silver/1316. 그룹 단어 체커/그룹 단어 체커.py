N = int(input())
count = 0

for _ in range(N):
    word = input().strip()
    reduced = [word[0]]

    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            reduced.append(word[i])

    if len(reduced) == len(set(reduced)):
        count += 1

print(count)