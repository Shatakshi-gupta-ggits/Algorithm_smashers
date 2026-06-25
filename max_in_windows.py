def max_in_windows(arr:list[int], k:int) -> list[int]:
    from collections import deque
    n = len(arr)

    ans:list[int] = []
    dq:deque[int] = deque()


    # 4 3 7 8 8 9 
    for i in range(n):
        # expired indices
        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)


        if i >= k - 1:
            ans.append(arr[dq[0]])


    return ans






if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(max_in_windows(nums, k))