T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    stack = []
    grass = input()
    cnt = 0
    for c in grass:
        if c == '(':
            cnt += 1
        elif c == ')':
            if stack and stack[-1] == '(':
                continue
            else:
                cnt += 1
        stack.append(c)
    print(f"#{test_case} {cnt}")