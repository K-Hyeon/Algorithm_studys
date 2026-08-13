T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #최빈값 문제
    score, max_cnt = 0, 0
    n = int(input())
    arr = list(map(int, input().strip()))
    arr = sorted(arr, reverse=True)
    cnt_arr = [0] * 10
    
    for item in arr:
        cnt_arr[item] += 1

    for i in range(9,-1,-1):
        if cnt_arr[i] > max_cnt:
            max_cnt = cnt_arr[i]
            score = i

    print(f"#{test_case} {score} {max_cnt}")
