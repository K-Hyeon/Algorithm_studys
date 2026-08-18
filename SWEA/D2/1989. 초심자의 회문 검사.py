T = int(input())
for test_case in range(1, T + 1):
    text = input().strip()
    
    if len(text) % 2: # 홀수
        temp = text[(len(text)//2)+1:]
        if text[:len(text)//2] == temp[::-1]: print(f"#{test_case} 1")
        else: print(f"#{test_case} 0")
    else: # 짝수
        temp = text[(len(text)//2):]
        if text[:len(text)//2] == temp[::-1]: print(f"#{test_case} 1")
        else: print(f"#{test_case} 0")
