import math
def dfs(numbers,cur_result, index, plus, minus, mul, div, result_list):
    if index == length:
        result_list.append(cur_result)
        return

    for i in range(4):
        if i == 0 and plus != 0:
            dfs(numbers, cur_result + numbers[index], index + 1, plus-1,minus,mul,div,result_list)
        elif i == 1 and minus != 0:
            dfs(numbers, cur_result - numbers[index], index + 1, plus, minus-1, mul, div,result_list)
        elif i == 2 and mul != 0:
            dfs(numbers, cur_result * numbers[index], index + 1, plus, minus, mul-1, div,result_list)
        elif i == 3 and div != 0:
            if cur_result > 0:
                dfs(numbers, cur_result // numbers[index], index + 1, plus, minus, mul, div-1,result_list)
            else:
                dfs(numbers, math.ceil(cur_result / numbers[index]), index + 1, plus, minus, mul, div-1,result_list)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    plus, minus, mul, div = map(int, input().split())
    numbers = list(map(int, input().split()))
    length = len(numbers)
    result_list = []
    dfs(numbers, numbers[0], 1, plus, minus, mul, div, result_list)
    max_val = max(result_list)
    min_val = min(result_list)
    result = max_val - min_val
    print(f'#{test_case} {result}')