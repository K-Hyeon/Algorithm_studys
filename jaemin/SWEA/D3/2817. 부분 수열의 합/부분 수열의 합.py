T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def dfs(index, total):
        # 모든 숫자를 확인한 경우
        if index == N:
            return 1 if total == K else 0

        # 현재 숫자를 선택하는 경우
        choose = dfs(index + 1, total + A[index])

        # 현재 숫자를 선택하지 않는 경우
        not_choose = dfs(index + 1, total)

        return choose + not_choose

    answer = dfs(0, 0)

    print(f"#{tc} {answer}")