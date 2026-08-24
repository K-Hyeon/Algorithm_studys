T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    id_list = list(map(int, input().split()))
    result = 0
    for _ in range(m):
        edit = list(input().split())
        command = edit[0]
        p = int(edit[1])
        if len(edit) > 2:
            v = int(edit[2])
        # 삽입
        if command == 'I':
            id_list.insert(p, v)
        elif command == 'D':
            id_list.pop(p)
        elif command == 'C':
            id_list[p] = v
    # L번자리에 곡이 존재하지 않으면 -1을 출력함
    if not id_list or l > len(id_list) - 1:
        result = -1
    else:
        result = id_list[l]
    print(f"#{test_case} {result}")
