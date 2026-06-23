import reverse_list
import random



# 1 2 3 4 5 6 7 8 
def rev(start, end):
    prev = None
    current = start.next
    next_node = None

    temp = start



    while current != end:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    start = prev



if __name__ == "__main__":
    arr = [random.randrange(101) for _ in range(10)]

    lst = reverse_list.SLL()

    for num in arr:
        lst.append(num)

    lst.print_list()

    start, end = lst.get_random_node()
    print(start.data, end.data)
    lst.print_list()


    print()
    print()
    for _ in range(100000):
        rev(start, end)
    print("success")
    lst.print_list()