testCaseTotalNum = int(input())
for testCaseNum in range(testCaseTotalNum):
    nums = list(map(int, input().split()))
    print(f"#{testCaseNum + 1} {max(nums)}")