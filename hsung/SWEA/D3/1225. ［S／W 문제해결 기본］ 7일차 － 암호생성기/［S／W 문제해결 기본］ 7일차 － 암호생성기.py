for t in range(10):
    _ = input()
    stack = list(map(int, input().split()))
    keep = True
    while(keep):
        for dis_num in range(1,6):
            candi = stack.pop(0)
            if candi - dis_num > 0:
                stack.append(candi-dis_num)
            else:
                stack.append(0)
                keep = False
                break
    print(f"#{t + 1}",end=" ")
    for pw in stack:
        print(f"{pw}",end=" ")
    print()