class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next
        return

    def print_node(self):
        if self.head == None:
            print("empty", end = " ")
        current = self.head
        while current:
            print(current.data, end= " ")
            current = current.next
        return

test_case= int(input())
for t in range(test_case):
    N = int(input())
    members = list(map(int,input().split()))
    member_list = Linked_list()
    for member in members:
        member_list.append(member)
    K = int(input())
    # print("we completed making member_list")
    cancle_members = list(map(int,input().split()))
    # print("we completed get cancle information")

    for c_member in cancle_members:
        member_list.delete(c_member)

    print(f"#{t+1}", end = " ")
    member_list.print_node()
    print()