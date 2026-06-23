class Node:
    def __init__(self, value:int):
        self.data = value
        self.next = None

    
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0



# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# head -> 1
# tail -> 5
# tail->next = 6
# tail = tail->next = 6


# 1 2 3 4
# head = 1

    # def trad_method(self, value:int):
    #     new_node = Node(value)

    #     if self.head is None:
    #         self.head = new_node
    #         self._size += 1
    #         return

    #     walker_node = self.head
    #     while walker_node.next is not None:
    #         walker_node = walker_node.next
        
    #     walker_node.next = new_node
    #     self._size += 1
    


    def append(self, value:int):
        new_node = Node(value)

        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
            self._size += 1
        else:
            self.head = self.tail = new_node
            self._size += 1

    # new_node->1 2 3 4 5 -1 
    # 77 1 2 3 4 5 -1
    def prepend(self, value:int):
        new_node = Node(value)

        temp = self.head
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    # function to get an element from random position
    # 1 2 3 4 5 6 -> 0-based indexing

        
    # list = [1, 2, 3, 4, 5, 6, 7]
        #    [0, 1, 2, 3, 4, 5, 6]
        #  head
    def get_element(self, pos:int):
        if pos < 0 and pos > self.size - 1:
            raise RuntimeError(f"Invalid Index. Should be in range 0 to {self.size - 1}")

        if self.head is None:
            return
        
        walker_node = self.head
        # pos = 3
        while pos > 0:
            walker_node = walker_node.next
            pos -= 1
        
        return walker_node.data
    
    def update_element(self, pos:int, new_value:int):
        if pos < 0 and pos > self.size - 1:
            raise RuntimeError(f"Invalid Index. Should be in range 0 to {self.size - 1}")
    
        if self.head is None:
            return
        
        walker_node = self.head
        while pos > 0:
            walker_node = walker_node.next
            pos -= 1

        walker_node.data = new_value


    # 1 2 3 4 5 6 7 8 -1
    #head->1             #  head
    # head -> 1
    # 1  
    # head.next.data = 2 
    # head = head.next == head -> 2 
    # head -> 1
    # head.next = 3


    # at 08: 03 PM
    # Deletions in linked list
    
    # deleting head element
    def delete_head(self):
        # List is empty
        if self.head is None:
            return
        
        # if list has single element
        if self.head.next is None:
            self.head = None
            self._size -= 1
            return
    
        # 1
        # 2 3 4 4
        # head = 2 

        # list has more than one element
        temp = self.head
        self.head = self.head.next
        temp = None
        self._size -= 1
    
    def delete_tail(self):
        # list is empty
        if self.head is None:
            return
        
        # list has single element
        if self.head.next is None:
            self.head = self.tail = None
            self._size -= 1
            return 


        # 1 2 3 4 [5, next(ref(-1))] -1
        # 6 -1
        walker_node = self.head
        while walker_node.next.next is not None:
            walker_node = walker_node.next

        walker_node.next = None
        self.tail = walker_node
        self._size -= 1


    def pop(self):
        self.delete_tail()

    def mid(self)->int:
        # list is empty
        if self.head is None:
            return -1
        
        # list has single element
        if self.head.next is None:
            return self.head.data
        
        
        # More than one element
        turtle = self.head
        hare = self.head

        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
        
        return turtle.data
    

    def del_mid(self):
        # list is empty
        if self.head is None:
            raise RuntimeError("List empty")
    
        # list has one element
        if self.head.next is None:
            self.head = self.tail = None
            self._size -= 1
            return
        
        # more than one element
        
        turtle = self.head
        hare = self.head
        turtle_ke_peechhe = None

        while hare and hare.next:
            hare = hare.next.next

            turtle_ke_peechhe = turtle
            turtle = turtle.next

        turtle_ke_peechhe.next = turtle.next
        turtle.next = None
        self._size -= 1
        
        
    # n-th element from last 
    # n-th element from start
    # 1 2 3 4 5 6 7 8 
    def n_th_from_last(self, pos:int):
        if not self.head:
            raise RuntimeError("List Empty.")
        
        if pos < 0 or pos >= self._size:
            raise RuntimeError("Invalid Position. Should be in the range 0 to {self._size - 1}")
        

        
        walker_node = self.head
        for _ in range(pos - 1):
            walker_node = walker_node.next

        current = self.head

        while walker_node.next:
            current = current.next
            walker_node = walker_node.next

        
        return current.data
    
    def is_cycle(self):
        turtle = self.head
        hare = self.head

        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

            if turtle == hare:
                return True
            
        return False


    def print_list(self):
        walker_node = self.head

        while walker_node is not None:
            print(walker_node.data, end="->")
            walker_node = walker_node.next
        print("-1")

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self):
        return self._size

    def __contains__(self, value:int):
        curr = self.head
        while curr.next:
            if curr.data == value:
                return True
            curr = curr.next
        
        return False
    
    def __bool__(self):
        return self._size > 0
    
    def __str__(self):
        curr = self.head
        values = []

        while curr:
            values.append(str(curr.data))
            curr = curr.next

        return "->".join(values)
    


    
if __name__ == "__main__":
    lst = SLL()

    nums = list(map(int, input().split()))

    for num in nums:
        lst.append(num)


    lst.print_list()
    # lst.prepend(0)
    # lst.print_list()
    # lst.trad_method(10)
    lst.print_list()

    try:
        print(lst.get_element(3))
    except RuntimeError as e:
        print(e)


    try:
        lst.update_element(3, 44)
        lst.print_list()
    except RuntimeError as e:
        print(e)

    print("Deleting tail")
    lst.delete_tail()
    lst.print_list()
    print(lst.tail.data)
    print(lst.mid())

    print(lst.del_mid())
    lst.print_list()

    lst.pop()
    lst.pop()
    lst.print_list()

    try:
        print(lst.n_th_from_last(3))
    except RuntimeError as e:
        print(e)
    
    print(lst.is_cycle())

    for x in lst:
        print(x, end="->")
    print("-1")
    print(len(lst))
    print(3 in lst)

    print("Here")
    print(lst)
    # wait a minut# let them pray  # we will continue once their prayer is completed
    # till then I am writing another function to append an element at head