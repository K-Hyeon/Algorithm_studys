def solution(n, times):
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 심사할 수 있는 사람 수
        people = 0
        
        for time in times:
            people += mid // time
            
            # 이미 n 명을 처리할 수 있다면 볼 필요 없음
            if people >= n:
                break
                
        if people >= n:
            # 더 짧은 시간도 가능한지 확인
            right = mid - 1
        else:
            # mid 시간으로는 모두 처리 불가능이므로 더 긴 시간 필요
            left = mid + 1
            
    return left