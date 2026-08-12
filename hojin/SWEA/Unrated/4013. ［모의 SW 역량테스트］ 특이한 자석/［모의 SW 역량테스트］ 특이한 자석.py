def rotation(arr, dir):
    if dir == 1:
        arr = [arr[-1]] + arr[:-1]
    else:
        arr = arr[1:] + [arr[0]]
    return arr

def check_right(mag_idx, dir):
    if mag_idx + 1 <= 3:
        if mag_info[mag_idx][2] == mag_info[mag_idx+1][6]:
            return
        else:
            check_right(mag_idx+1, -dir)
            mag_info[mag_idx+1] = rotation(mag_info[mag_idx+1], -dir)
            return
    else:
        return

def check_left(mag_idx, dir):
    if mag_idx - 1 >= 0:
        if mag_info[mag_idx][6] == mag_info[mag_idx - 1][2]:
            return
        else:
            check_left(mag_idx - 1, -dir)
            mag_info[mag_idx-1] = rotation(mag_info[mag_idx-1], -dir)
            return
    else:
        return

T = int(input())
for test_case in range(1, T+1):
    K = int(input())
    mag_info = [list(map(int, input().split())) for _ in range(4)]
    answer = 0
    for _ in range(K):
        num, direction = map(int, input().split())
        num -= 1
        if num == 0:
            check_right(num, direction)
            mag_info[num] = rotation(mag_info[num], direction)
        elif num == 1 or num == 2:
            check_right(num, direction)
            check_left(num, direction)
            mag_info[num] = rotation(mag_info[num], direction)
        else:
            check_left(num, direction)
            mag_info[num] = rotation(mag_info[num], direction)

    for i in range(4):
        if mag_info[i][0] == 1:
            answer += 2 ** i
    print(f"#{test_case} {answer}")