heights = [int(input()) for _ in range(9)]

total = sum(heights)

for i in range(9):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            result = heights[:i] + heights[i+1:j] + heights[j+1:]
            result.sort()

            for h in result:
                print(h)
            break
    else:
        continue
    break
