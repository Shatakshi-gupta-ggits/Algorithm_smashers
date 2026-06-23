class Node:
    def __init__(self, value:int):
        self.data = value
        self.next = None


# -1
# 2 -> new int[2]
# head -> 2
# 3
# head -> 3
# head->[2, ref(3)] [3, ref(4)] [4, None]
# walker_node
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def append(self, value:int):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def prepend(self, value:int):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
            self.size += 1
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            self.size += 1
        
    def insert(self, pos:int, value:int):
        if pos < 0 or pos > self.size:
            raise RuntimeError(f"Invalid Position {pos}. Should in range 0 to {self.size}")
        

        if pos == 0:
            self.prepend(value)
            return
        

        new_node = Node(value)
        walker_node = self.head
        while pos > 1:
            walker_node = walker_node.next
            pos -= 1

        # 2 3 4 5 6 7 
        temp = walker_node.next
        walker_node.next = new_node
        new_node.next = temp
        self.size += 1

    def delete(self, pos:int):
        if pos < 0 or pos >= self.size:
            raise RuntimeError(f"Invalid Postion. Should be in range 0 to {self.size - 1}")
        
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size -= 1
            return
        
        prev = self.head

        for _ in range(pos - 1):
            prev = prev.next

        target = prev.next

        prev.next = target.next
        target.next = None


        self.size -= 1


    def get(self, pos:int):
        if pos < 0 or pos > self.size - 1:
            raise RuntimeError(f"Ivalid Position. Should be in range 0 to {self.size - 1}")

        walker_node = self.head
        for _ in range(pos):
            walker_node = walker_node.next
        
        return walker_node.data

    def set(self, pos:int, value:int):
        if pos < 0 or pos > self.size - 1:
            raise RuntimeError(f"Ivalid Position. Should be in range 0 to {self.size - 1}")
        
        walker_node = self.head
        for _ in range(pos):
            walker_node = walker_node.next

        walker_node.data = value
        self.size += 1

    def pop(self):
        if not self.head:
            raise RuntimeError("List Empty.")
    
        self.delete(self.size - 1)
    
    def popleft(self):
        if self.head is None:
            raise RuntimeError("List Empty.")

        if self.head.next is None:
            self.head = None
            return None
        

        temp = self.head.next
        self.head = None
        self.head = temp
        self.size -= 1
        

    

        


    def print_list(self):
        walker_node = self.head

        while walker_node is not None:
            print(walker_node.data, end="->")
            walker_node = walker_node.next

        print("-1")



if __name__ == "__main__":
    nums = list(map(int, input().split()))

    lst = SLL()
    for num in nums:
        lst.append(num)

    try:
        lst.print_list()
        lst.prepend(-2)
        lst.print_list()

        lst.insert(pos=3, value=-11)
        lst.print_list()
        lst.insert(pos=0, value=0)
        lst.print_list()
        print(lst.size)
        lst.insert(pos=8, value=99)
        lst.print_list()

        lst.delete(0)
        lst.print_list()
        lst.delete(1)
        lst.print_list()
        lst.delete(6)
        lst.print_list()
        print(lst.get(5))
        lst.set(5, 33)
        lst.print_list()
        lst.pop()
        lst.print_list()
    except RuntimeError as e:
        print(e)

