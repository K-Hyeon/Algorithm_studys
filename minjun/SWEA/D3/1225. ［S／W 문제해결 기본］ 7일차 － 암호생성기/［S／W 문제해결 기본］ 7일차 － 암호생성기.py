def reduce_shift(password):
    for i in range(1, 6):
        temp = password.pop(0)
        temp = temp - i
        if temp <= 0:
            temp = 0
            password.append(temp)
            return True, password
        password.append(temp)
    return False, password
    
for test_case in range(1, 11):
    T = int(input())
    password = list(map(int, input().split()))
    while True:
        zero_reached, password = reduce_shift(password)
        if zero_reached:
            break
    result = ' '.join(map(str, password))
    print(f'#{test_case} {result}')