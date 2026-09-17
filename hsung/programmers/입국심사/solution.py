# import heapq

# def solution(n, times):
#     heap_times = [[time, time] for time in times]
#     heapq.heapify(heap_times)
#     for _ in range(n):
#         cur_min, org_data  = heapq.heappop(heap_times)
#         heapq.heappush(heap_times, [cur_min + org_data, org_data])

#     return cur_min

# 개떡같은 시간초과 
# o(log N) 이 필요함. 

def solution(n, times):
    answer = 0

    left = 1 
    right = max(times) * n  # 최악의 경우
    
    while left <= right:
        mid = (left + right) // 2  # 중앙값
        
        # mid 시간 동안 입국 가능한 사람 수 합
        people_processed = sum(mid // time for time in times)
        
        # mid 시간 기준으로 사람들이 많다면 오른쪽 줄이기 
        if people_processed >= n:
            answer = mid       
            right = mid - 1   
            
        else:
            left = mid + 1     # mid 시간 기준으로도 시간이 더 필요하다면 오른 쪽으로 넘어가기 
            
    return answer