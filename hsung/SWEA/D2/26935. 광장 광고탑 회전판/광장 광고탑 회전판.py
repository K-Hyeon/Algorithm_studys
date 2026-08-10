test_case = int(input())

for t in range(test_case):
    N, M = map(int, input().split())
    elems = list(map(int, input().split()))

    for _ in range(M):
        elems.append(elems.pop(0))

    print(f"#{t+1} {elems[0]}")