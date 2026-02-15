S, P = map(int, input().split())
dna = input()
need = list(map(int, input().split()))
#현재 ACGT 개수 
count = [0, 0, 0, 0]
idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

#초기 윈도우
for i in range(P):
    count[idx[dna[i]]] += 1

result = 0

def check():
    for i in range(4):
        if count[i] < need[i]:
            return False
    return True

if check():
    result += 1

#슬라이딩 윈도우
for i in range(P, S):
    count[idx[dna[i]]] += 1
    count[idx[dna[i-P]]] -= 1

    if check():
        result += 1

print(result)