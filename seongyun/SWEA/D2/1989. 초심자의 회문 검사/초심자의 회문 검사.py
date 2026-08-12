def solve():
    text = input()
    return 1 if text == text[::-1] else 0

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case} {solve()}")