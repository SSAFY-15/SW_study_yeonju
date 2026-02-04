word = input().upper()
count = {}

for ch in word:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

max_value = max(count.values())
max_chars = [k for k, v in count.items() if v == max_value]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])