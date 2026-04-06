import sys
input = sys.stdin.readline

# 사람 수 N, 파티 수 M
N, M = map(int, input().split())

# 진실을 아는 사람 정보
truth = list(map(int, input().split()))
truth_people = truth[1:]  # 첫 번째는 인원 수

# Union-Find 초기화
parent = [i for i in range(N + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa  # 한쪽으로 합침

# 파티 정보 저장
parties = []

for _ in range(M):
    party = list(map(int, input().split()))
    members = party[1:]
    parties.append(members)

    # 같은 파티 사람들 모두 union
    for i in range(len(members) - 1):
        union(members[i], members[i + 1])

# 진실을 아는 사람들의 root 저장
truth_roots = set(find(x) for x in truth_people)

# 거짓말 가능한 파티 수 세기
result = 0

for party in parties:
    can_lie = True
    for person in party:
        if find(person) in truth_roots:
            can_lie = False
            break
    if can_lie:
        result += 1

print(result)