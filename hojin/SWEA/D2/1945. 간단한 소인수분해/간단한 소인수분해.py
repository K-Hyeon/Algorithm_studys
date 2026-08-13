T= int(input())

for test_case in range(1,T+1):
    n = int(input())
    nums = [2,3,5,7,11]
    arr = [0]*5
    for i in range(len(nums)):
        while n % nums[i] == 0:
            arr[i] += 1
            n //= nums[i]
    print(f'#{test_case} ', end="")
    [print(f'{item} ',end="") for item in arr]
    print()