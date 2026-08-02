import heapq
import math
T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    heap = []
    for item in arr:
        heapq.heappush(heap,item)
    index = len(heap)-1
    while index > 0:
        index = math.floor((index-1)//2)
        sum += heap[index]
    print(f"#{test_case} {sum}")