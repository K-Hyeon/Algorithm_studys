import math
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = list(map(int, input().split()))
    grade = ['','A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    arr = []
    for i in range(n):
        scores = list(map(int, input().split()))
        final_score = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.2
        arr.append(final_score)

    score = arr[k-1]
    sort_arr = sorted(arr, reverse=True)
    index = sort_arr.index(score) + 1
    rating = math.ceil(index / n * 10)
    print(f"#{test_case} {grade[rating]}")