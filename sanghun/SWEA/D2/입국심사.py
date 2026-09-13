def solution(n, times):
    left = 1
    # 가장 오래 걸리는 심사관이 모든 사람을 심사할 때의 최대 시간
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 모든 심사관이 처리할 수 있는 사람 수의 합
        people = sum(mid // t for t in times)
        
        if people >= n:
            answer = mid
            right = mid - 1  # 더 짧은 시간 내에도 가능한지 확인
        else:
            left = mid + 1   # 시간이 부족하므로 범위를 늘림
            
    return answer
