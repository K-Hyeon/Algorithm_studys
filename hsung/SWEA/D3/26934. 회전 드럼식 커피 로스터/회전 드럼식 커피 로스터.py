test_case = int(input())

for t in range(test_case):
    N, M =  map(int, input().split())
    temp = list(map(int, input().split()))
    items = [[i+1,t] for i,t in enumerate(temp)]

    coffe_drum = []
    # 우선 스택 채우기
    while len(coffe_drum) < N:
        coffe_drum.append(items.pop(0))

    last_popped_item = None
    while(coffe_drum):
        drying_item = coffe_drum.pop(0)
        if drying_item[1] // 2 == 0:
            last_popped_item = drying_item[0]
            if items:
                coffe_drum.append(items.pop(0))
        else:
            drying_item[1] = drying_item[1] // 2
            coffe_drum.append(drying_item)
    print(f"#{t + 1} {last_popped_item}")