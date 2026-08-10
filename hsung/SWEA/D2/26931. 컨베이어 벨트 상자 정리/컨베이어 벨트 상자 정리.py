test_case = int(input())
for t in range(test_case):
    boxes = list(input().strip().upper())
    belt_stack = []
    for box in boxes:
        if len(belt_stack) ==0:
            belt_stack.append(box)
        elif belt_stack[-1] == box:
            belt_stack.pop()
        else:
            belt_stack.append(box)
    print(f"#{t+1} {len(belt_stack)}")