T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(f"#{test_case}")
    for i in range(n):
        #90도
        for j in range(n):
            print(matrix[n-1-j][i], end="")

        print("",end=" ")
        # #180도
        for j in range(n):
            print(matrix[n - 1 - i][n-1-j], end="")

        print("", end=" ")
        #270도
        for j in range(n):
            print(matrix[j][n - 1 - i], end="")

        print()