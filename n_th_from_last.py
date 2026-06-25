# Goal: return n-th node from last
# 1 2 3 4 5 6 6 7 8 9 

# Hint: how would you return n-th from start

import reverse_list
import random


# store the nodes value in an array
# arr[:-n]
# last me jao -> O(n)

def n_th_from_from(n:int, lst, head):
    if n <= 0 or n > len(lst):
        raise RuntimeError("Invalid Position.")
    
    curr = head

    for _ in range(n):
        curr = curr.next
    
    walker_node = head

    while curr is not None:
        curr = curr.next
        walker_node = walker_node.next


    return walker_node.data

    pass



if __name__ == "__main__":
    arr = [random.randrange(0, 101) for _ in range(10)]


    lst = reverse_list.SLL()
    for num in arr:
        lst.append(num)


    lst.print_list()

    try:
        while True:
            print("Size: ", len(lst))
            n = random.randrange(0, len(lst))
            print("Position: ", n)
            print("N-th element: ", n_th_from_from(n, lst, lst.head))
            print()
    except RuntimeError as e:
        print(e)