def solution(distance, rocks, n):
    # 바위를 정렬해야 왼쪽부터 순서대로 확인할 수 있음
    rocks.sort()

    # 마지막 지점(도착점)도 하나의 위치로 취급
    rocks.append(distance)

    # 우리가 구하려는 최소 거리의 범위
    left = 1
    right = distance

    while left <= right:
        # 최소 거리를 mid로 가정
        mid = (left + right) // 2

        # 마지막으로 살아남은 바위의 위치
        prev = 0

        # 제거한 바위의 개수
        removed = 0

        # 시작점부터 모든 바위를 순서대로 확인
        for rock in rocks:

            # 현재 바위와 이전 바위 사이의 거리
            gap = rock - prev

            # 두 바위 사이의 거리가 mid보다 작다면
            # 현재 바위를 제거해야 함
            if gap < mid:
                removed += 1

            else:
                # 현재 바위를 유지
                # 다음 바위와 비교할 기준점이 됨
                prev = rock

        # 제거해야 하는 바위가 n개보다 많으면
        # mid라는 최소 거리를 만들 수 없음
        if removed > n:
            right = mid - 1

        else:
            # n개 이하만 제거하면 가능
            # 더 큰 최소 거리도 가능한지 확인
            left = mid + 1

    # 가능한 최소 거리 중 최댓값
    return right