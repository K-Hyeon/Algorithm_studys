def is_possible(n, k, stones):
    cnt = 0
    tmp_cnt = 0
    for stone in stones:
        if stone < n:
            tmp_cnt += 1
        else:
            cnt = max(cnt, tmp_cnt)
            tmp_cnt = 0
    cnt = max(cnt, tmp_cnt)
    return cnt < k

def solution(stones, k):
    ans = -1
    l = 1
    r = max(stones)
    
    while l <= r:
        mid = (l + r) // 2
        
        if is_possible(mid, k, stones):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans