N = int(input())                                 
meetings = [tuple(map(int, input().split())) for _ in range(N)]

# (끝시간, 시작시간) 정렬
meetings.sort(key=lambda x: (x[1], x[0]))         

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:                         
        count += 1
        end_time = end

print(count)   