"""
() {} 검사

'' 안 문자열 구간안에서는 무시


짝을 이루면 1 어긋나면 0 반환
"""

test_case = int(input())
for t in range(test_case): 
    test_string = input().strip()
    test_stack = []# 검사용 스택 오직 append pop [-1] 만 확인합시다잉
    for test_c in test_string:
        if test_c == "(" or test_c == "{":
            if len(test_stack) == 0:
                test_stack.append(test_c)
            elif test_stack[-1] != "\'":
                test_stack.append(test_c)

        elif test_c == ")": #or test_c == "}":
            if len(test_stack) == 0:
                test_stack.append(0)
                break
            if test_stack[-1] != "\'":
                if test_stack[-1] == "(":
                    test_stack.pop()
                else:
                    test_stack.append(0)
                    break
        elif test_c == "}" :
            if len(test_stack) == 0:
                test_stack.append(0)
                break

            if test_stack[-1] != "\'":
                if test_stack[-1] == "{":
                    test_stack.pop()
                else:
                    test_stack.append(0)
                    break
        elif test_c == "\'" :
            if len(test_stack) == 0:
                test_stack.append(test_c)
            elif test_stack[-1] != "\'":
                test_stack.append(test_c)
            elif test_stack[-1] == "\'":
                test_stack.pop()

    if len(test_stack) == 0:
        print(f"#{t + 1} 1")
    else:
        print(f"#{t + 1} 0")
