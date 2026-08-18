def inorder(tree, n, N, res):
    if n * 2 <= N:
        inorder(tree, n * 2, N, res)
    res.append(tree[n])
    if n * 2 + 1 <= N:
        inorder(tree, n * 2 + 1, N, res)


def solve():
    N = int(input())
    tree = [""] * (N + 1)

    for _ in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp[1]

    res = []
    inorder(tree, 1, N, res)
    return "".join(res)


for test_case in range(1, 11):
    print(f"#{test_case} {solve()}")
