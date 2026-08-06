for t in range(10):
    length = int(input())
    brackets = list(input())
    bracket_stack = []

    left_bracket = ["(", "{", "<", "["]
    right_bracket = [")", "}", ">", "]"]
    for bracket in brackets:
        if bracket in left_bracket:
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) == 0:
                print(f"#{t + 1} 0")
                break
            elif bracket_stack[-1] != left_bracket[right_bracket.index(bracket)]:
                print(f"#{t + 1} 0")
                break
            elif bracket_stack[-1] == left_bracket[right_bracket.index(bracket)]:
                bracket_stack.pop()
    if len(bracket_stack) == 0:
        print(f"#{t + 1} 1")