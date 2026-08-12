def inorder(tree, d, n):
    if not tree[n]:
        return d[n]

    word = ""
    word += inorder(tree, d, tree[n][0])
    word += d[n]
    if len(tree[n]) == 2:
        word += inorder(tree, d, tree[n][1])

    return word


def solve():
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    d = {}

    for _ in range(N):
        tmp = input().split()
        d[int(tmp[0])] = tmp[1]
        if len(tmp) >= 3:
            tree[int(tmp[0])].append(int(tmp[2]))
        if len(tmp) >= 4:
            tree[int(tmp[0])].append(int(tmp[3]))

    return inorder(tree, d, 1)


for test_case in range(1, 11):
    print(f"#{test_case} {solve()}")
