T = int(input())
for test_case in range(1,T+1):
    result = 0
    stack = []
    boxes = input()
    for box in boxes:
        if stack and stack[-1] == box:
            stack.pop()
        else:
            stack.append(box)
    result = len(stack)
    print(f"#{test_case} {result}")