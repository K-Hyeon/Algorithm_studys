
def check_brackets(line):
    stack = []
    in_quote = False
    quote_char = None
    
    for char in line:
        # 따옴표 감싼 문자열 구간 처리
        if in_quote:
            if char == quote_char:
                in_quote = False
                quote_char = None
            continue
        else:
            if char in ("'", '"'):
                in_quote = True
                quote_char = char
                continue
        
        # 여는 괄호 push
        if char in ('(', '{'):
            stack.append(char)
        # 닫는 괄호 pop 및 짝 검사
        elif char in (')', '}'):
            if not stack:
                return 0
            
            top = stack.pop()
            if char == ')' and top != '(':
                return 0
            if char == '}' and top != '{':
                return 0
                
    # 닫히지 않은 괄호가 남아있거나 따옴표가 닫히지 않은 경우 0
    if stack or in_quote:
        return 0
        
    return 1


T = int(input().strip())
for tc in range(1, T + 1):
    line = input()
    result = check_brackets(line)
    print(f"#{tc} {result}")
