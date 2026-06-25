import reverse_list
import random



if __name__ == "__main__":
    arr = [random.randrange(0, 101) for _ in range(20)]

    lst = reverse_list.SLL()


    for num in arr:
        lst.append(num)

    lst.print_list()
    