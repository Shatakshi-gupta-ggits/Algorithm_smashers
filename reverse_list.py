import random
import math
from collections import Counter

class Node:
    def __init__(self, value:int):
        self.data = value
        self.next = None



class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def find(self, pos:int):
        if pos < 0 or pos >= len(self):
            raise RuntimeError(f"Invalid Position. Should be in range 0 to {len(self) - 1}")
        
        walker_node = self.head
        for _ in range(pos):
            walker_node = walker_node.next

        return walker_node

    def __str__(self):
        curr = self.head
        values = []

        while curr:
            values.append(str(curr.data))
            curr = curr.next

        
        
        return "->".join(values)

        

    def append(self, value:int):
        new_node = Node(value)

        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
            self._size += 1
        else:
            self.head = self.tail = new_node
            self._size += 1


    def print_list(self):
        walker_node = self.head

        while walker_node is not None:
            print(walker_node.data, end='->')
            walker_node = walker_node.next

        print("-1")



    def reverse(self):
        prev = None
        curr = self.head
        next_node = None

        self.tail = self.head

        # 1 2 3 
        # last_node = self.head.next.next
        # sec_last = self.head.next
        # start = self.head

        # 1 2 3 4 5 6 7 
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        

    def get_random_node(self):


        # intervals = [
        #     (i, j)
        #     for i in range(1, len(self) - 1)
        #     for j in range(i, len(self) - 1)
        # ]

        # start, end = random.choice(intervals)

        position1 = random.randrange(1, len(self) - 1)

        position2 = random.randrange(1, len(self) - 1)
        while position2 == position1:
            position2 = random.randrange(1, len(self) - 1)

        start = min(position1, position2)
        end = max(position1, position2)
        

        return self.find(start), self.find(end)




if __name__ == "__main__":
    arr = [random.randrange(0, 101) for _ in range(6)]

    lst = SLL()

    for num in arr:
        lst.append(num)

               
    print("list:", end=" ")
    lst.print_list()

    lst.reverse()

    lst.print_list()
    # print(lst)

    # lst.append(-1)

    # print(f"size: {lst._size}")

    # start, end = lst.get_random_node()

    # print(start.data)
    # print(end.data)