from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 중요도 리스트에 저장
    value = list(map(int, input().split()))
    
    queue = deque(range(N))
    count=0
    
    while True:
        # 만약 첫번째가 가장 중요하다면
        # count 1증가
        # popleft로 위치값 없애기
        # 중요도 0으로 바꾸기
        if value[queue[0]] == max(value):
            count += 1
            idx = queue.popleft()
            value[idx] = 0
            # 만약
            if idx == M:
                print(count)
                break
        # 아니라면 제일 뒤로 보내기
        else:
            queue.append(queue.popleft())