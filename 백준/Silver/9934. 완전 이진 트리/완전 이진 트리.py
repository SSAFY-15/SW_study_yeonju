# import sys
# sys.stdin = open('input.txt', 'r')

K = int(input())
# 노드 수 
N = 2**K - 1
# 값 입력
arr = list(map(int, input().split()))

# 중위순회 배열로부터 트리를 복원
# 각 레벨별로 출력
tree = [[] for _ in range(K)]

def build(start, end, depth):
    if start > end:
        return
    # 루트 = 현재 구간의 중앙
    # 해당 깊이에 저장
    mid = (start + end) // 2
    tree[depth].append(arr[mid])

    build(start, mid-1, depth+1)
    build(mid+1, end, depth+1)

build(0, len(arr) -1, 0)

for level in tree:
    print(*level)