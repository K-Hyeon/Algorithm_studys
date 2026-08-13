T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    water = list(map(int,input().split()))
    result = 0
    curr_index = 0
    while n - curr_index > k:
        max_water_index = 0
        #k만큼 탐색
        for i in range(1,k+1):
            next_index = curr_index + i
            if next_index < n and next_index in water:
                max_water_index = max(max_water_index,next_index)
        if max_water_index == 0:
            result = 0
            break
        else:
            curr_index = max_water_index
            result += 1

    print(f"#{test_case} {result}")