arr = [input() for _ in range(5)]

new_str = ''

for x in range(15):
    for y in range(5):
        if x < len(arr[y]):
            new_str += arr[y][x]

print(new_str)