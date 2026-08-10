from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    boxes = list(input().strip())
    s = deque()
    for box in boxes:
        if s and s[-1] == box:
            s.pop()
        else:
            s.append(box)

    print(f"#{test_case} {len(s)}")
    