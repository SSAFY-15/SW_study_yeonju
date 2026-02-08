import sys
input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
query = list(map(int, input().split()))

for q in query:
    if q in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
