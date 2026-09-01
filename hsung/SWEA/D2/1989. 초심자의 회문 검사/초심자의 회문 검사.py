test_case = int(input())
for t in range(test_case):
    does_it_panlindrome = input().strip()
    ans = 1 if does_it_panlindrome[::-1] == does_it_panlindrome else 0
    print(f"#{t+1} {ans}")