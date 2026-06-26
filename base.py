import random


class Node:
    def __init__(self, value: int) -> None:
        self.data: int = value
        self.next: Node | None = None


class SLL:
    def __init__(self) -> None:
        self.head: Node | None = None
        self._size: int = 0

    # for printing the list using SLL object
    def __str__(self) -> str:
        curr: Node | None = self.head
        values:list[str] = []

        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next

        return "->".join(values)
    

    

    
    def __len__(self) -> int:
        return self._size
    
    def append(self, value:int) -> None:
        new_node: Node | None = Node(value)

        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        
        self._size += 1




# They have stopped using Optional[SLL]. They say "type | None" is best
def merge(lst1: Node | None, lst2: Node | None) -> Node | None:
    head1: Node | None = lst1
    head2: Node | None = lst2

    dummy_head: Node = Node(-1)
    tail: Node = dummy_head

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = Node(head1.data)
            head1 = head1.next
        else:
            tail.next = Node(head2.data)
            head2 = head2.next
        tail = tail.next

    while head1:
        tail.next = Node(head1.data)
        tail = tail.next
        head1 = head1.next

    while head2:
        tail.next = Node(head2.data)
        tail = tail.next
        head2 = head2.next

    return dummy_head.next


def get_size(head: Node | None) -> int:
    n: int = 0
    walker: Node | None = head

    while walker is not None:
        n += 1
        walker = walker.next

    return n


def intersect(head1: Node | None, head2: Node | None) -> None:
    if head1 is None or head2 is None:
        return
    
    start1: Node | None = head1
    start2: Node | None = head2

    n = random.randrange(1, get_size(head1))

    # for _ in range(n):
    #     assert start1 is not None
    #     start1 = start1.next

    while n and start1.next is not None:
        n -= 1
        start1 = start1.next
    # assert start2 is not None
    # while start2.next is not None:
    #     start2 = start2.next

    # start2.next = start1
    start1.next = start2



def print_list(head: Node | None) -> None:
    if head is None:
        return
    
    walker: Node | None = head

    while walker is not None:
        print(walker.data, end="->")
        walker = walker.next

    print("-1")



if __name__ == "__main__":
    test_cases = 0
    while test_cases < 1:
        arr1 = [random.randrange(0, 101) for _ in range(random.randrange(5, 7))]
        arr2 = [random.randrange(0, 101) for _ in range(random.randrange(5, 7))]

        lst1 = SLL()
        lst2 = SLL()

        for num in arr1:
            lst1.append(num)

        for num in arr2:
            lst2.append(num)

        print("List1: ", lst1)
        print("List2: ", lst2)

        lst = merge(lst1.head, lst2.head)
        print("Merged List: ")
        print_list(lst)

        print("Size of list1: ", len(lst1))
        print("Size of list2: ", len(lst2))
        print("Size of merged list: ", get_size(lst))

        test_cases += 1

        intersect(lst1.head, lst2.head)
        print_list(lst1.head)
    
    print(test_cases)