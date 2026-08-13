T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    for _ in range(dump):
        #오름차순 정렬
        boxes = sorted(boxes)
        #최솟값
        min_val = boxes[0]
        #최댓값
        max_val = boxes[-1]
        #최댓값 - 최솟값
        diff = max_val-min_val
        if diff < 2:
            result = diff
            break
        else:
            boxes[0] += 1
            boxes[-1] -= 1
    
    boxes = sorted(boxes)
    # 최솟값
    min_val = boxes[0]
    # 최댓값
    max_val = boxes[-1]
    result = max_val - min_val
    print(f"#{test_case} {result}")