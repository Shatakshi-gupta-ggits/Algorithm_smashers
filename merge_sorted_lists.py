import reverse_list
import random


def merge(lst1, lst2):
    walker_node1 = lst1.head
    walker_node2 = lst2.head

    dummy = reverse_list.Node(-1)
    tail = dummy

    while walker_node1 and walker_node2:
        if walker_node1.data <= walker_node2.data:
            new_node = reverse_list.Node(walker_node1.data)
            tail.next = new_node
            walker_node1 = walker_node1.next
        else:
            new_node = reverse_list.Node(walker_node2.data)
            tail.next = new_node
            walker_node2 = walker_node2.next
        
        tail = tail.next

    while walker_node1:
        new_node = reverse_list.Node(walker_node1.data)
        tail.next = new_node
        tail = tail.next
        walker_node1 = walker_node1.next
    
    while walker_node2:
        new_node = reverse_list.Node(walker_node2.data)
        tail.next = new_node
        tail = tail.next
        walker_node2 = walker_node2.next

    merged = reverse_list.SLL()
    merged.head = dummy.next

    return merged






if __name__ == "__main__":
    arr1 = sorted([random.randrange(0, 101) for _ in range(random.randrange(5, 15))])
    arr2 = sorted([random.randrange(0, 101) for _ in range(random.randrange(5, 15))])

    lst1 = reverse_list.SLL()
    lst2 = reverse_list.SLL()


    for num in arr1:
        lst1.append(num)

    for num in arr2:
        lst2.append(num)
    
    print("List 1: ", lst1)
    print("List 2: ", lst2)

    head = merge(lst1, lst2)

    print("List: ", merge(lst1, lst2))
    # print(lst1.head.data)