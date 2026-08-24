T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    Linkedlist = []
    #c가 1이면 맨앞에 2이면 맨뒤에 선다.
    for i in range(n):
        c, val = map(int, input().split())
        if c == 1:
            Linkedlist.insert(0,val)
        elif c == 2:
            Linkedlist.append(val)
    print(f'#{test_case}', end="")
    [print(f' {i}', end="") for i in Linkedlist]
    print()