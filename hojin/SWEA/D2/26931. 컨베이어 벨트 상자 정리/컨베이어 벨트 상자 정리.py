

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    input_str = input()

    belt_stack = []

    for c in input_str:
        if len(belt_stack) == 0:
            belt_stack.append(c)
        else:
            top = belt_stack[-1]

            if top == c:
                belt_stack.pop()
            else:
                belt_stack.append(c)

        # print(f"test: {belt_stack}")

    print(f"#{test_case} {len(belt_stack)}")
