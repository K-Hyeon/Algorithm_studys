T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def bubble_sort(str_list):
    n = len(str_list)
    num_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }

    for i in range(n):
        for j in range(0,n-i-1):
            num_str = str_list[j]

            next_num_str = str_list[j+1]
            if num_dict[num_str] > num_dict[next_num_str]:
                str_list[j] = next_num_str
                str_list[j + 1] = num_str

for test_case in range(1, T + 1):
    t, length = input().split()
    length = int(length)
    str_list = list(input().split())
    bubble_sort(str_list)
    print(f"{t}")
    [print(f"{item}",end=" ") for item in str_list]
    print()
