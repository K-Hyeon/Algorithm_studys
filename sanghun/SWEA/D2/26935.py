
T = int(input().strip())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ads = list(map(int, input().split()))
    
    # M번 회전 후 정면에 오는 광고판의 인덱스
    target_idx = M % N
    
    print(f"#{tc} {ads[target_idx]}")
  
