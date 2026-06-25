def first_negatives(arr:list[int], k:int) -> list[int]:
    from collections import deque
    n = len(arr)

    dq:deque[int] = deque() 

    ans:list[int] = []

    for i in range(n):
        # remove expired indices
        if dq and dq.popleft() <= i - k:
            dq.pop()
        
        # inserst negative value's indices
        if arr[i] < 0:
            dq.append(i)

        # calculate the answer
        if i >= k - 1 and not dq:
            ans.append(0)
        elif i >= k - 1 and dq:
            ans.append(arr[dq.popleft()])


    return ans




if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(first_negatives(nums, k))