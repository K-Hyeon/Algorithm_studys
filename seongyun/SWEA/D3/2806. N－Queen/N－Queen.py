def recursive(location, N, n):
    global ans
    if n == N:
        ans += 1
        return

    for i in range(N):
        for loc in location:
            x_diff = loc[0] - n
            y_diff = loc[1] - i
            if y_diff == 0 or x_diff + y_diff == 0 or x_diff - y_diff == 0:
                break
        else:
            location.add((n, i))
            recursive(location, N, n + 1)
            location.remove((n, i))
        

def solve():
    N = int(input())
    location = set()
    recursive(location, N, 0)


T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    solve()
    print(f"#{test_case} {ans}")
