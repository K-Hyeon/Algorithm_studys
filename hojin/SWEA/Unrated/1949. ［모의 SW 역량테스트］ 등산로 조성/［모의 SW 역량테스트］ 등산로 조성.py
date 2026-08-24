import copy
def dfs(grid, start_r, start_c, n, k):
    # 초기 상태, 현재위치와 공사여부, 방문여부, 현재 길이를 나타냄
    stack = [(start_r, start_c, False, {(start_r, start_c)}, 1, copy.deepcopy(grid))]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_val = 0

    while stack:
        r, c, isWork, visited, length, grid_temp = stack.pop()
        # print(r, c, isWork, visited, length)
        # for row in grid_temp:
        #     print(row)
        max_val = max(max_val, length)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # grid를 벗어나지 않고 현재 가지에서 방문한 적이 없으면
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                # 그리고 그 위치의 값이 r,c위치의 값보다 작으면 (같은것도 안됨) 스택에 추가
                if grid_temp[nr][nc] < grid_temp[r][c]:

                    visited_copy = copy.deepcopy(visited)
                    grip_temp_copy = copy.deepcopy(grid_temp)

                    visited_copy.add((nr, nc))
                    stack.append((nr, nc, isWork, visited_copy, length + 1,grip_temp_copy))

                # 아직 공사를 하지 않았고 만약에 그 값에 k를 뺐을때 작으면 스택에 추가 가능하다. 근데 그 인덱스의 값을 k만큼 줄여야하는데
                #그러면 스택에 grid까지 넣는건가?
                elif not isWork and grid_temp[nr][nc] >= grid_temp[r][c] > grid_temp[nr][nc] - k:
                    visited_copy = copy.deepcopy(visited)
                    grip_temp_copy = copy.deepcopy(grid_temp)
                    #무조건 k만큼 깎는것이 아닌 이미 두 값의 차가 K보다 작은게 확인되었으니 1만큼 작게 한다
                    grip_temp_copy[nr][nc] -= grid_temp[nr][nc] - grid_temp[r][c] + 1
                    # 그럼 isWork를 True로 바꾸고


                    visited_copy.add((nr, nc))
                    stack.append((nr, nc, True, visited_copy, length + 1,grip_temp_copy))

    return max_val


def solve():
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        n, k = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]
        #결과
        result = 0
        #가장 높은 봉우리들
        max_val = 0
        for row in grid: max_val = max(max_val, max(row))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == max_val:
                    result = max(result, dfs(grid, i, j, n, k))
        print(f'#{test_case} {result}')


solve()
