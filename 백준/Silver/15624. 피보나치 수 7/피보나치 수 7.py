N = int(input())
mod = 1000000007

a, b = 0, 1
for _ in range(N):
    a, b = b, (a + b) % mod

print(a)
