def get_combinations(arr,n):
    result = []

    def backtrack(start, current):
        if len(current) == n:
            result.append(current.copy())
            return

        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i+1,current)
            current.pop()

    backtrack(0,[])
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = float('inf')

    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    combinations = get_combinations(list(range(n)),n//2)


    for combination in combinations:
        #고르고 난뒤 또다른 조합
        another_combination = []
        for i in range(n):
            if i not in combination:
                another_combination.append(i)

        #이중 포문
        S_sum1 = 0
        S_sum2 = 0

        for i in combination:
            for j in combination:
                if i != j:
                    S_sum1 += S[i][j]

        for i in another_combination:
            for j in another_combination:
                if i != j:
                    S_sum2 += S[i][j]

        result = min(abs(S_sum1-S_sum2),result)
    print(f'#{test_case} {result}')
