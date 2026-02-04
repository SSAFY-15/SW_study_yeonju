T = int(input())

def score(arr):
    score = 0
    streak = 0

    for str in arr:
        if str == 'O':
            streak += 1
            score += streak

        else:
            streak = 0

    return score

for tc in range(1, T+1):
    arr = list(map(str, list(input())))
    print(score(arr))
