class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data, index =None):
        new_node = Node(data)
        if index == None:
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            return
        if index == 0:
            new_node.next  = self.head
            self.head = new_node
            return
        current = Node(0)
        current.next = self.head
        cur_index = 0

        while cur_index != index:
            current = current.next
            cur_index += 1
        new_node.next = current.next
        current.next = new_node
        return

    def print_node(self):
        current = self.head
        count = 0 
        while current and count <10:
            print(current.data, end=" ")
            current = current.next
            count += 1

for t in range(10):
    password_length = int(input())
    passwords = list(map(int, input().split()))
    our_linked_list = Linked_List()
    for pw in passwords:
        our_linked_list.append(pw)
    # print("linked list completed")

    op_num = int(input())
    ops = [op.strip() for op in input().split('I') if op]
    for op in ops:
        X,Y,*numbers = map(int, op.split())
        # print(f"X: {X} \nY: {Y} \nnumbers : {numbers}")
        for index in range(X,X+Y):
            # print(f"index: {index} numbers : {numbers[index-X]}")
            our_linked_list.append(numbers[index-X], index)
            #our_linked_list.print_node()
    # print(ops)
    print(f"#{t+1}", end=" ")
    our_linked_list.print_node()
    print()