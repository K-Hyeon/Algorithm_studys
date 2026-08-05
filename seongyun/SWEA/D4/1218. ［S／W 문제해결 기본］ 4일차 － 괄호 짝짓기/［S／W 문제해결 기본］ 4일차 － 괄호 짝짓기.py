from collections import deque

for test_case in range(1, 11):
    n = int(input())
    text = input().strip()

    s = deque()
    open_brackets = ('(', '[', '{', '<')
    close_brackets = (')', ']', '}', '>')
    ans = 1
    for c in text:
        if c in open_brackets:
            s.append(c)
        elif c in close_brackets:
            idx = close_brackets.index(c)
            if s[-1] == open_brackets[idx]:
                s.pop()
            else:
                break

    ans = 0 if s else 1
    print(f"#{test_case} {ans}")
    