for t in range(10):
    _, passwords_Str = input().split()
    passwords = list(map(int,list(passwords_Str)))

    pw_stack = []
    for password in passwords:
        if len(pw_stack) == 0 :
            pw_stack.append(password)
        elif pw_stack[-1] == password:
            pw_stack.pop()
        else:
            pw_stack.append(password)
    ans = "".join(list(map(str,pw_stack)))
    print(f"#{t + 1} {ans}")