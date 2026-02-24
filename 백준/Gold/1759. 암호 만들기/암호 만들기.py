L, C = map(int, input().split())
chars = input().split()
chars.sort()
# 모음 집합
alphabet = {'a', 'e', 'i', 'o', 'u'}

def dfs(start, path):
    if len(path) == L:
        v_cnt = sum(1 for ch in path if ch in alphabet)
        c_cnt = L - v_cnt

        if v_cnt >= 1 and c_cnt >= 2:
            print(''.join(path))
        return
    
    for i in range(start, C):
        path.append(chars[i])
        dfs(i+1, path)
        path.pop()
        
dfs(0, [])