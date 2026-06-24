import base


def delete_nth_from_last(lst: base.Optional[base.SLL], pos:int) -> None:
    if pos < 1 or pos > len(lst):
        raise RuntimeError(f"Invalid Position. Should be in range 2 to {len(lst)}.")


    if not lst.head:
        raise RuntimeError("List Empty.")
    

    fast = lst.head

    for _ in range(pos):
        fast = fast.next
    
    if fast is None:
        temp = lst.head
        lst.head = lst.head.next
        temp.next = None
        lst._size -= 1
        return 

    slow = lst.head
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # 1 2 3 4 5 6 7 8
    temp = slow.next
    slow.next = temp.next
    temp.next = None
    lst._size -= 1

    return



if __name__ == "__main__":
    arr = [base.random.randrange(0,101) for _ in range(base.random.randrange(5,21))]
    
    lst = base.SLL()

    for num in arr:
        lst.append(num)

    while True:
        if len(lst) == 0:
            arr = [base.random.randrange(0,101) for _ in range(base.random.randrange(5,21))]

            lst = base.SLL()

            for num in arr:
                lst.append(num)

            
        print(lst)
        print("Size: ", len(lst))
        n = base.random.randint(1, len(lst))
        
        print("Nth Position: ", n)
        try:
            delete_nth_from_last(lst, n)
        except RuntimeError as e:
            print(e)
            print()

        

    print(lst)