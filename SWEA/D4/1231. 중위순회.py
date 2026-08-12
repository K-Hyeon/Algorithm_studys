T = 10

def inorder(node):
    global answer
    if node is None: return
    inorder(tree[node][0])
    answer += word[node]
    inorder(tree[node][1])
    
for test_case in range(1, T + 1):
    N = int(input())
    word = {}
    tree = {}
    for i in range(N):
        arr = input().split()
        node = int(arr[0])
        word[node] = arr[1]
        
        left = None
        right = None
        if len(arr) >= 3:
            left = int(arr[2])
        if len(arr) >= 4:
            right = int(arr[3])
        tree[node] = [left, right]

    # 중위 순회
    answer = ""
    inorder(1)
    print(f"#{test_case} {answer}")
