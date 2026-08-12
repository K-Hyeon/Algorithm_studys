T = 10
def square(num, m):
    if m <= 1:
        return num
    return num * square(num,m-1)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = int(input())
    n, m = map(int, input().split())
    print(f"#{t} {square(n,m)}")