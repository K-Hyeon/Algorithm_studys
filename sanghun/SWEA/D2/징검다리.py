def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        count = 0  # 연속으로 건너뛸 수 없는 디딤돌 수
        
        for stone in stones:
            if stone < mid:
                count += 1
            else:
                count = 0
            
            # 연속된 0 이하의 돌이 k개 이상이면 mid명은 건널 수 없음
            if count >= k:
                break
        
        if count >= k:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer
