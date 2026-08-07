T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    max_num = max(arr)
    min_num = min(arr)
    arr.remove(max_num)
    arr.remove(min_num)
    sum_val = sum(arr)
    avg_val = round(sum_val/len(arr))
    print(f"#{test_case} {avg_val}")