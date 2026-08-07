"""
N<500 인 경우
이진 트리 -> 1차원 리스트로 구현
부모 노드가 idx // 2가 되도록 유지 => swap 
조상 노드의 합은 idx // 2 반복하기  
"""



T = int(input())

for testCaseNum in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    heap = [0] # 0번 인데스 0 넣어놓고 1번 인덱스 부터 쓰면 부모 노드 idx 계산에 편함!

    for num in numbers:
        heap.append(num)
        curr = len(heap) - 1 

        # 부모 노드(curr // 2)와 비교하며 자식의 값이 더 작으면 swap
        while curr > 1 and heap[curr] < heap[curr // 2]:
            heap[curr], heap[curr // 2] = heap[curr // 2], heap[curr]
            curr = curr // 2

    ans = 0
    node = N // 2  # 직계 부모
    while node > 0:
        ans += heap[node]
        node = node // 2  # 한 단계 위 조상 노드로 이동

    print(f"#{testCaseNum} {ans}")