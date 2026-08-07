test_case = int(input())
for t in range(test_case):
    _ = input()
    elems = input().split()
    if len(elems) % 2:
        front = elems[:len(elems)//2 + 1]
        back = elems[len(elems)//2 +1:] 
    else:
        front = elems[:len(elems)//2]
        back = elems[len(elems)//2:]

    # print(f"front : {front}\n back : {back}")
    ans = [ ]
    while (front):
        ans.append(front.pop(0))
        if back:
            ans.append(back.pop(0))
    print(f"#{t + 1}", end = " ")
    for a in ans:
        print(a, end = " ")
    print()