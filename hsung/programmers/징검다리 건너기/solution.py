# def solution(stones, k):
#     reverse_stones = stones[::-1]
#     limit  = k + 1  # k + 1 는 못뜀
#     count_acseding = 0
#     candidates = []
#     for i in range(1, len(reverse_stones)):
#         if reverse_stones[i-1] <= reverse_stones[i]:
#             count_acseding += 1
#         else:
#             count_acseding = 0 
            
#         if count_acseding == limit:
#             candidates.append(reverse_stones[i])
#     return min(candidates)




from collections import deque

def solution(stones, k):
    answer = float('inf')
    dq = deque()  # 인덱스를 저장할 덱
    
    for i in range(len(stones)):
        # 1. 윈도우 범위를 벗어난 인덱스는 덱의 맨 앞에서 제거 (슬라이딩)
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # 2. 덱에 남은 돌들 중 현재 돌(stones[i])보다 작은 값들은 모두 덱에서 제거
        # (현재 돌이 들어온 이상, 이전의 작은 돌들은 앞으로 윈도우 최댓값이 될 일이 없으므로 쓸모가 없음)
        while dq and stones[dq[-1]] < stones[i]:
            dq.pop()
            
        # 3. 현재 돌의 인덱스를 덱에 추가
        dq.append(i)
        
        # 4. 첫 윈도우(k개)가 꽉 찬 시점부터 최솟값 갱신 시작
        if i >= k - 1:
            # 덱의 맨 앞에 있는 값이 현재 윈도우의 최댓값
            answer = min(answer, stones[dq[0]])
            
    return answer