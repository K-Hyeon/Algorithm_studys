class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, nums):
        if not self.head:
            temp_nodes = [ ]
            for num in nums:
                new_node = Node(num)
                if not len(temp_nodes):
                    temp_nodes.append(new_node)
                else:
                    temp_nodes[-1].next = new_node
                    new_node.prev =  temp_nodes[-1]
                    temp_nodes.append(new_node)
            self.head = temp_nodes[0]
            self.tail = temp_nodes[-1]

        else:
            if self.head.data > nums[0]:
                temp_nodes = []
                for num in nums:
                    new_node = Node(num)
                    if not len(temp_nodes):
                        temp_nodes.append(new_node)
                    else:
                        temp_nodes[-1].next = new_node
                        new_node.prev =  temp_nodes[-1]
                        temp_nodes.append(new_node)
                temp_nodes[-1].next = self.head
                self.head.prev = temp_nodes[-1]
                self.head = temp_nodes[0]
                return
            
            current  = self.head
            while current.next and current.next.data <= nums[0]: 
                #  current.next가 None일때
                # current.next data가 nums[0]보다 클 때 멈춤 
                current = current.next
            temp_nodes = []
            for num in nums:
                new_node = Node(num)
                if not len(temp_nodes):
                    temp_nodes.append(new_node)
                else:
                    temp_nodes[-1].next = new_node
                    new_node.prev =  temp_nodes[-1]
                    temp_nodes.append(new_node)
            if current.next:
                current.next.prev = temp_nodes[-1]
                temp_nodes[-1].next = current.next
            else: # current가 마지막일 때 
                self.tail = temp_nodes[-1]

            current.next = temp_nodes[0]
            temp_nodes[0].prev = current
            return

    def print_tail(self):
        current  = self.tail
        for _ in range(10):
            print(current.data, end=" ")
            if not current.prev:
                break
            current = current.prev
        return 


test_case = int((input()))
for t in range(test_case):
    N, M = map(int, input().split())
    my_Linked_list = Linked_list()
    for _ in range(M):
        belt = list(map(int, input().split()))
        my_Linked_list.append(belt)
    print(f"#{t+1}", end= " ")
    my_Linked_list.print_tail()
    print()