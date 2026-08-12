T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, x = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    result_cnt = 0
    for _ in range(2):
        for row in matrix:
            #한 행씩 검사
            isOkay = True
            #경사로 놓은 인덱스
            hill_index = []
            #그 행의 모든 숫자가 같으면 넘어감
            if len(set(row)) == 1:
                result_cnt += 1
                continue
            else:
                #각 셀을 모두 돈다.
                for i in range(n):
                    #좌우 바로 양옆을 검사해서 작으면 세부적으로 더 검사
                    left, right = i - 1, i + 1
                    #왼쪽먼저
                    if left >= 0 and row[left] < row[i]:
                        #길이 x 만큼 검사해서 경사로 놓을 수 있는지, 없으면 바로 다음 행으로 넘어감
                        for m in range(1,x+1):
                            left_index = i - 1 * m
                            #배열을 벗어나거나 1보다 더작은지 그리고 경사로 놓여져있지 않은지 검사
                            if left_index >= 0 and row[left_index] == row[i] - 1 and left_index not in hill_index:
                                hill_index.append(left_index)
                                continue
                            else:
                                isOkay = False
                                break
                    if right < n and row[right] < row[i]:
                        # 길이 x 만큼 검사해서 경사로 놓을 수 있는지, 없으면 바로 다음 행으로 넘어감
                        for m in range(1, x + 1):
                            right_index = i + 1 * m
                            # 배열을 벗어나거나 1보다 더작은지 그리고 경사로 놓여져있지 않은지 검사
                            if right_index < n and row[right_index] == row[i] - 1 and right_index not in hill_index:
                                hill_index.append(right_index)
                                continue
                            else:
                                isOkay = False
                                break
            if isOkay:
                result_cnt += 1
        #행렬 뒤집어서 세로 검사
        matrix = list(map(list, zip(*matrix[::-1])))

    print(f"#{test_case} {result_cnt}")