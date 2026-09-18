def solution(stones, k):
    # 문제의 접근을 "X명이 건널 수 있는가?"에 초점을 둠
    # 이분 탐색의 왼쪽, 오른쪽 범위 지정
    left = 1
    right = max(stones)
    
    # 탐색 범위가 남아있는 동안 반복
    while left <= right:
        
        # 이번에 건널 사람의 수
        mid = (left + right) // 2
        cnt = 0
        
        # 건널 사람과 돌의 숫자와 비교
        # 건널 수 없는 연속된 돌을 cnt에 저장
        for stone in stones:
            # mid 명이 지나간 후에 이 돌을 사용할 수 없는 경우
            if stone < mid:
                cnt += 1
            # 사용할 수 있는 돌을 만난 경우 cnt 리셋
            else:
                cnt = 0
                
            # 건널 수 없는 연속된 돌이 k개일 경우 종료
            if cnt >= k:
                break
                
        # 이분탐색 적용
        # mid명이 건널 수 있는 경우
        if cnt >= k:
            right = mid - 1
        # mid명이 건널 수 없는 경우
        else:
            left = mid + 1
            
    return right