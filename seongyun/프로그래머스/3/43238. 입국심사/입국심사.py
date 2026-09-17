def is_possible(time, n, times):
    cnt = 0
    for t in times:
        cnt += time // t
    return cnt >= n

def solution(n, times):
    l = 1
    r = 10**20
    answer = -1
    
    while l <= r:
        mid = (l + r) // 2
        
        if is_possible(mid, n, times):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer