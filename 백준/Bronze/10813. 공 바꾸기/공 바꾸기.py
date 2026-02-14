N, M = map(int, input().split())

basket = []
for i in range(1, N+1):
    basket.append(i)

for _ in range(M):
    x, y = map(int, input().split())
    basket[x-1], basket[y-1] = basket[y-1], basket[x-1]

print(*basket)