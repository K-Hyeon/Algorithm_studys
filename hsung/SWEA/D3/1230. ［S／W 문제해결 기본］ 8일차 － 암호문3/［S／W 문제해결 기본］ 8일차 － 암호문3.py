
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self,datas:list):
        for data in datas:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                continue
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            # print(f"we added {data}")

        return

    def delete(self, index, d_counts):
        count = 1
        current = self.head

        if index == 0:
            for _ in range(d_counts):
                self.head = self.head.next
            return
        while count != index:
            if not current.next:
                break
            current = current.next
            count += 1
    
        for _ in range(d_counts):
            if not current.next:
                break
            current.next = current.next.next   
        return

    def insert(self, index, I_count, S:list):
        count =1
        current = self.head
        if index  == 0:
            node_list = []
            for new_data in S:
                new_node = Node(new_data)
                if node_list:
                    node_list[-1].next = new_node
                node_list.append(new_node)
            node_list[-1].next = self.head
            self.head = node_list[0]
            return 
        while count != index:
            if not current.next:
                break
            current = current.next
            count += 1
    
        for new_data in S:
            new_node = Node(new_data)
            new_node.next = current.next
            current.next = new_node
            current = current.next
        return 

    def print_node_front(self):
        current = self.head
        count = 0
        # print(f"check current : {current}")
        while count < 10:
            print(current.data , end = " ")
            current = current.next
            count += 1

for t in range(10):
    N = int(input())
    origin_s= list(map(int, input().split()))
    M = int(input())
    operations = input().split()

    refined_ops = []
    index = 0  
    while index < len(operations):
        one_op = []
        if operations[index] == "I":
            one_op.append("I")

            #X
            index += 1
            one_op.append(int(operations[index]))

            # Y
            index += 1
            Y = int(operations[index])
            one_op.append(Y)

            index += 1
            S = []
            for _ in range(Y):
                S.append(int(operations[index]))
                index += 1
            one_op.append(S)
            refined_ops.append(one_op)
        elif operations[index] == "D":
            one_op.append("D")

            index += 1
            one_op.append(int(operations[index]))

            index += 1
            one_op.append(int(operations[index]))

            index += 1

            refined_ops.append(one_op)
        elif operations[index] =="A":
            one_op.append("A")

            index += 1
            Y = int(operations[index])
            one_op.append(Y)

            index += 1
            S = []
            for _ in range(Y):
                S.append(int(operations[index]))
                index += 1
            one_op.append(S)
            refined_ops.append(one_op)

    # print(refined_ops)
    """
    [['D', 111, 4], 
    ['D', 966, 7],
    ['D', 402, 6], 
    ['D', 1541, 7],
    ['I', 456, 9, [981611, 272008, 230837, 675611, 621683, 906919, 530069, 376019, 164102]],
    ['I', 3, 1, [688219]],
    ['A', 7, [733384, 124593, 229343, 279168, 582310, 780824, 699431]]
    ['D', 522, 2],
    ['I', 2, 6, [248872, 927796, 508541, 110112, 441355, 950485]], ['D', 344, 8],
    ['A', 7, [734661, 152680, 368189, 225622, 850366, 393573, 167382]],
    ['A', 10, [942536, 335702, 443320, 177984, 896373, 794141, 330854, 740183, 969700, 563764]],
    ['I', 1556, 3, [780780, 603104, 643082]], ['D', 97, 7],
    ['A', 9, [330277, 795557, 588851, 962669, 994994, 930452, 209763, 525142, 309187]],
    ['I', 1407, 6, [407757, 765954, 866931, 808806, 348973, 917749]]
    """
    our_linked_list = Linked_List()
    # print(f"origin_s : {origin_s} ")
    our_linked_list.append(origin_s)

    # # print("front of linked list: ", end=" ")
    # # our_linked_list.print_node_front()
    # # print()
    for op in refined_ops:
        if op[0] == "I":
            our_linked_list.insert(*op[1:])
        elif op[0] == "D":
            our_linked_list.delete(*op[1:]) 
        elif op[0] == "A":
            our_linked_list.append(op[-1])    

    print(f"#{t+1}", end=" ")
    our_linked_list.print_node_front()
    print()

