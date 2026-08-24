
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, numbers : list):
        first_node_list = []
        for num in numbers:
            new_node = Node(num)
            if not len(first_node_list):
                first_node_list.append(new_node)
                continue
            new_node.prev =  first_node_list[-1]
            first_node_list[-1].next = new_node
            first_node_list.append(new_node)

        self.head = first_node_list[0]
        self.tail = first_node_list[-1]

        # circular 만들기!
        self.head.prev = self.tail
        self.tail.next = self.head
        return 

    def insert(self, M, K):
        current = self. head
        for _ in range(K):
            for _ in range(M):
                current = current.next
            new_node  = Node(current.data + current.prev.data)

            new_node.prev = current.prev
            new_node.next = current

            current.prev.next = new_node
            current.prev = new_node

            if current == self.head:
                self.tail = new_node

            # 순서가 새로운 노드로 변경 되어야 함.
            current = new_node

    def print_tail(self):
        current = self.tail
        count = 0
        while count < 10:
            print(current.data, end = " ")
            if current.prev == self.tail:
                break
            current = current.prev
            count += 1
        return

test_case = int(input())
for t in range(test_case):
    N, M, K  = map(int, input().split())
    nodes = list(map(int, input().split()))
    our_linked_list = Linked_List()
    our_linked_list.append(nodes)
    our_linked_list.insert(M,K)

    print(f"#{t+1}", end=" ")
    our_linked_list.print_tail()
    print()