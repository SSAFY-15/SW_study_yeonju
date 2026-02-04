A, B = map(int, input().split())

A_rev = int(str(A)[::-1])
B_rev = int(str(B)[::-1])

print(max(A_rev, B_rev))