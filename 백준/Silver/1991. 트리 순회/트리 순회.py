# import sys
# sys.stdin = open('input.txt', 'r')

# 전위순회
def pre_order(T):
    if T != '.':
        print(T, end='')
        pre_order(arr[T][0])
        pre_order(arr[T][1])

#중위순회
def in_order(T):
    if T != '.':
        in_order(arr[T][0])
        print(T, end='')
        in_order(arr[T][1])

# 하위순회
def post_order(T):
    if T != '.':
        post_order(arr[T][0])
        post_order(arr[T][1])
        print(T, end='')

N = int(input())

arr = {}

for _ in range(N):
    p, l, r = input().split()
    arr[p] = (l, r)

pre_order('A')
print()
in_order('A')
print()
post_order('A')