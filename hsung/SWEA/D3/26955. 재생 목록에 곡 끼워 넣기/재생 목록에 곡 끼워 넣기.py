class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node_list:
    def __init__(self):
        self.head = None

    def append(self, nums):
        for num in nums:
            new_node = Node(num)
            if not self.head:
                self.head = new_node
                continue
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return 

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        count = 1
        current = self.head
        while count != index:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        return 

    def print_pos(self, pos):
        count = 0
        current = self.head
        while count != pos:
            current = current.next
            count += 1
        print(current.data)

test_case = int(input())
for t in range(test_case):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    our_node_list = Node_list()
    our_node_list.append(nums)
    for _ in range(M):
        index, data = map(int, input().split())
        our_node_list.insert(index=index, data=data)

    print(f"#{t+1}", end=" ")
    our_node_list.print_pos(L)
