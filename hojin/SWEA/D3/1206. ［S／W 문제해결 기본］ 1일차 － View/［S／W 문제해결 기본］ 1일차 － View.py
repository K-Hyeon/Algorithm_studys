T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    #땅 부분 제외하고 처음 빌딩 부터 검사
    for curr_index in range(2,n-2):
        building_list = []
        for j in range(1,3):
            left = curr_index - 1*j
            right = curr_index + 1*j
            if arr[left] < arr[curr_index] and arr[right] < arr[curr_index]:
                building_list.append(arr[left])
                building_list.append(arr[right])
        if len(building_list) == 4:
            result += arr[curr_index] - max(building_list)

    print(f"#{test_case} {result}")