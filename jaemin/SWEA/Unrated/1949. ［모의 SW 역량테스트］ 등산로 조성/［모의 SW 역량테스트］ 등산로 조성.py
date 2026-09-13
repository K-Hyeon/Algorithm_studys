def dfs(r, c, length, cut):
    global answer

    # 현재까지 만든 등산로 길이의 최댓값 갱신
    answer = max(answer, length)

    # 4방향 탐색
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        # 범위를 벗어나면 이동 불가
        if not (0 <= nr < N and 0 <= nc < N):
            continue

        # 다음 칸이 현재 칸보다 낮다면
        if mountain[nr][nc] < mountain[r][c]:
            # 방문 처리
            visited[nr][nc] = True

            # 다음 칸으로 이동
            dfs(nr, nc, length + 1, cut)

            # 백트래킹
            visited[nr][nc] = False

        # 다음 칸이 높거나 같고, 아직 한 번도 깎지 않았다면
        elif not cut and not visited[nr][nc]:

            # 현재 높이보다 1 낮게 만들 수 있는 최대 깊이 계산
            diff = mountain[nr][nc] - mountain[r][c] + 1

            # 최대 K만큼 깎을 수 있어야 함
            if diff <= K:

                # 실제로 산을 깎음
                mountain[nr][nc] -= diff

                # 방문 처리
                visited[nr][nc] = True

                # 깎은 상태(cut=True)로 이동
                dfs(nr, nc, length + 1, True)

                # 원래 높이로 복구
                mountain[nr][nc] += diff

                # 방문 해제
                visited[nr][nc] = False


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    max_height = max(map(max, mountain))

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    answer = 0

    # 모든 가장 높은 봉우리에서 출발
    for r in range(N):
        for c in range(N):
            if mountain[r][c] == max_height:

                visited = [[False] * N for _ in range(N)]
                visited[r][c] = True

                # 현재 봉우리에서 DFS 시작
                # length = 현재까지 지나온 칸 수
                # cut = 아직 산을 깎았는지 여부
                dfs(r, c, 1, False)

    print(f"#{tc} {answer}")