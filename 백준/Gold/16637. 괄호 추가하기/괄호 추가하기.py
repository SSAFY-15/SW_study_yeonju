# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
arr = input().strip()

nums = []
ops = []

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

for i in range(N):
    if i % 2 == 0:
        nums.append(int(arr[i]))
    else:
        ops.append(arr[i])
    
max_val = -float('inf')

def dfs(idx, value):
    global max_val

    # 모든 연산 끝
    if idx == len(ops):
        max_val = max(max_val, value)
        return
    # 괄호 없이 연산
    next_val = calc(value, ops[idx], nums[idx+1])
    dfs(idx+1, next_val)
    # 다음 연산부터 괄호로 계산
    if idx + 1 < len(ops):
        bracket = calc(nums[idx + 1], ops[idx + 1], nums[idx + 2])
        next_val = calc(value, ops[idx], bracket)
        dfs(idx + 2, next_val)

dfs(0, nums[0])

print(max_val)