N = int(input())

lst = list(map(int, input().split()))
price = list(map(int, input().split()))

total = lst[0] * price[0]

for i in range(1, N-1):
    if price[i] == min(price[1:N-1]):
        total += sum(lst[1:]) * price[i]
        break
    else:
        total += lst[i] * price[i]

print(total)