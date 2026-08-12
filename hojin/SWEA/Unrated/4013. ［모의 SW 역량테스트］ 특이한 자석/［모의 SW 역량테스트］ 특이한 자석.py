T = int(input())

#연쇄된거라면그 방향의 배열은 무시해야함
def rotate_magnetic(magnetics, magnetic_num, direction, isChain='no'):


    # 돌리는 자석의 오른쪽 날
    right_blade = magnetics[magnetic_num][2]
    # 돌리는 자석의 왼쪽 날
    left_blade = magnetics[magnetic_num][-2]
    right_opponent_blade = None
    left_opponent_blade = None
    # 반대 자석의 오른쪽 날
    if magnetic_num != 3:
        right_opponent_blade = magnetics[magnetic_num + 1][-2]

    # 반대 자석의 왼쪽 날
    if magnetic_num != 0:
        left_opponent_blade = magnetics[magnetic_num - 1][2]

    #연쇄작용은 이미 돌려진 톱니를 돌리지 않는다.
    if isChain == 'from_left':
        left_opponent_blade = None
    elif isChain == 'from_right':
        right_opponent_blade = None

    # 시계방향 회전
    if direction == 1:
        # 일단 본인은 무조건 돌아감
        magnetics[magnetic_num] = [magnetics[magnetic_num][-1]] + magnetics[magnetic_num][:7]
        # 왼쪽
        # 만약에 자성이 다르다? 그러면 반대쪽도 반대 방향으로 회전시킴
        # 반대 자석이 없으면 돌리지 않음
        if left_opponent_blade is not None and left_blade != left_opponent_blade:
            rotate_magnetic(magnetics, magnetic_num - 1, -1,'from_right')

        # 오른쪽
        # 만약에 자성이 다르다? 그러면 반대쪽도 반대 방향으로 회전시킴
        if right_opponent_blade is not None and right_blade != right_opponent_blade:
            rotate_magnetic(magnetics, magnetic_num + 1, -1,'from_left')


    # 반시계 방향
    elif direction == -1:

        magnetics[magnetic_num] = magnetics[magnetic_num][1:] + [magnetics[magnetic_num][0]]
        # 왼쪽
        # 만약에 자성이 다르다? 그러면 반대쪽도 반대 방향으로 회전시킴
        if left_opponent_blade is not None and left_blade != left_opponent_blade:
            rotate_magnetic(magnetics, magnetic_num - 1, 1,'from_right')

        # 오른쪽
        # 만약에 자성이 다르다? 그러면 반대쪽도 반대 방향으로 회전시킴
        if right_opponent_blade is not None and right_blade != right_opponent_blade:
            rotate_magnetic(magnetics, magnetic_num + 1, 1,'from_left')


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    # 결과
    result = 0
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    # 점수표
    scorecard = [{0: 0, 1: 1}, {0: 0, 1: 2}, {0: 0, 1: 4}, {0: 0, 1: 8}]
    # k번의 회전
    for _ in range(k):
        magnetic_num, direction = map(int, input().split())
        # 0-index로 통일하자
        magnetic_num -= 1
        # 회전 함수
        rotate_magnetic(magnetics, magnetic_num, direction)

    # 회전후 점수 계산
    for i in range(4):
        red_arrow = magnetics[i][0]
        score = scorecard[i][red_arrow]
        result += score

    print(f'#{test_case} {result}')
