T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    result = list(map(int, input().split()))
    cur_index = 0
    for _ in range(k):
        mod_index = cur_index + m
        if mod_index >= len(result):
            mod_index = mod_index % len(result)

        front = mod_index - 1
        back = mod_index
        sum_val = result[front] + result[back]
        if mod_index == 0:
            result.append(sum_val)
            cur_index = mod_index - 1
        else:
            result.insert(mod_index, sum_val)
            cur_index = mod_index

    # 오른쪽 끝부터 거꾸로 10개 읽기
    result = result[::-1][:10]
    print(f'#{test_case}', end="")
    [print(f' {i}', end="") for i in result]
    print()
