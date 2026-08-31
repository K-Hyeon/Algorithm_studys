
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ad_num, rotate_num = map(int, input().split())

    adds = list(map(int, input().split()))

    front_index_after_rotate = rotate_num % ad_num

    print(f"#{test_case} {adds[front_index_after_rotate]}")
