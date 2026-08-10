test_case = int(input())

for t in range(test_case):
    num_codes = int(input())
    codes = list(map(int,input().split()))
    queue = []

    print(f"#{t+1}", end=" ")
    count = 1
    for code in codes:
        if code == 1:
            queue.append(count)
            count +=1
        if code == 2:
            print(queue.pop(0), end=" ")
    print()