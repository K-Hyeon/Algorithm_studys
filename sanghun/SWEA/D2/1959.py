

T = int(input())


for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 A가 더 짧거나 같도록 설정
    if N > M:
        A, B = B, A
        N, M = M, N

    # 음수 결과도 고려하여 최솟값으로 초기화 
    max_sum = -float('inf')

    # 짧은 배열 A를 이동시킬 수 있는 범위: M - N + 1번
    for i in range(M-N+1):
        total = 0

        for j in range(N):
            # 여기서 i+j 로 이동하면서 해준다
            # 큰 길이에서 작은 길이 빼고 그 수만큼 하나씩 더해가면서 순회한다 
            total += A[j] * B[i+j]

        # 만약 총 결과가 합의 최대값보다 크면 최대합에 총 합을 대입해준다 
        if total > max_sum:
            max_sum = total

    print(f"#{test_case} {max_sum}")
