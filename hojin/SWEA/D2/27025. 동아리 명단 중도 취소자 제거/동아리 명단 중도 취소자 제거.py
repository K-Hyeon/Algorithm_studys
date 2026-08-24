T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    Linkedlist = list(map(int, input().split()))
    k = int(input())
    cancel = list(map(int, input().split()))

    for c in cancel:
        Linkedlist.remove(c)
    
    if not Linkedlist:
        print(f'#{test_case} empty')
    else:
        print(f'#{test_case}', end="")
        [print(f' {i}', end="") for i in Linkedlist]
        print()