T=10
for test_case in range(1,T+1):
    n = int(input())
    codes = list(map(int, input().split()))
    command_len = int(input())
    commands = list(input().split())

    #명령어를 순회하며 I이면 다음 인덱스, x, y를 읽고
    for i in range(len(commands)):
        if commands[i] == 'I':
            x = int(commands[i+1])
            y = int(commands[i+2])

            for j in range(1,y+1):
                num = commands[i+2+j]
                codes.insert(x-1+j, int(num))

    print(f'#{test_case}', end="")
    [print(f" {codes[i]}", end="") for i in range(10)]
    print()