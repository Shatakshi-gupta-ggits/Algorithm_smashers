class Node:
    def __init__(self, value:int):
        self.data = value
        self.next = None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0


    def append(self, value:int) -> None:
        new_node = Node(value)

        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        
        self._size += 1

    def print_list(self):
        walker_node = self.head

        while walker_node:
            print(walker_node.data, end="->")
            walker_node = walker_node.next
        
        print("-1")

    