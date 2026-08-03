T = int(input())
for test_case in range(1, T + 1):
    text = input()
    stack = []
    ans = 1
    for c in text:
        if stack and stack[-1] in ['"', "'"]:
            if c == stack[-1]:
                stack.pop()
            continue

        if c in ['(', '{', '"', "'"]:
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans = 0
                break
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                ans = 0
                break
    if stack:
        ans = 0

    print(f"#{test_case} {ans}")
        