from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque(range(1, N+1))
cnt = 0

for num in nums:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        
        idx = queue.index(num)
        
        #왼쪽 회전이 더 빠른경우
        if idx <= len(queue) // 2:
            queue.append(queue.popleft())
            cnt += 1
        # 오른쪽 회전이 빠른경우
        else:
            queue.appendleft(queue.pop())
            cnt += 1
        
print(cnt)