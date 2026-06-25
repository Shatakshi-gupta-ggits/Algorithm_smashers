def max_subarray_sum(arr:list[int], k:int) -> int:
    n = len(arr)

    # 2 4 2 7 8
    window_sum = 0


    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    print("Enter the array: ", end=" ")
    nums = list(map(int, input().split()))
    k = int(input("Enter k: "))
    print(max_subarray_sum(nums, k))
