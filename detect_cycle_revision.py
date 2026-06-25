import base
import cycle_start


# 1 2 3 4 5  
def has_cycle(lst: base.SLL) -> bool:
    turtle = lst.head
    hare = lst.head

    while hare and hare.next:
        turtle = turtle.next
        hare = hare.next.next

        if hare == turtle:
            return True
    
    return False


# return start node of cycle

def has_cycle2(lst: base.SLL) -> bool:
    st = set()

    walker = lst.head

    # 1 2 3 4 5 => 5(ref(3))
    while walker:
        if walker in st:
            return True
        
        st.add(walker)
        walker = walker.next

    return False

def start_of_cycle(lst: base.SLL) -> base.Node | None:
    st = set()

    walker = lst.head

    while walker:
        if walker in st:
            return walker

        st.add(walker)
        walker = walker.next
    
    return None


if __name__ == "__main__":

    test_cases = 0
    while test_cases <= 1000:
        arr = [base.random.randrange(0, 101) for _ in range(base.random.randrange(5, 15))]


        lst = base.SLL()

        for num in arr:
            lst.append(num)


        print("List: ", lst)

        cycle_start.create_cycle(lst)
        print(has_cycle(lst))
        print(has_cycle2(lst))
        # print(lst)

        ans = start_of_cycle(lst)
        if ans is not None:
            print(ans.data)
        else:
            print("No cycle")

        test_cases += 1

    print("Succesfull test cases: ", test_cases)