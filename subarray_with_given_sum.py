def ans(arr:list[int], k:int, target: int) -> list[int]:
    n = len(arr)

    window_sum = sum(arr[:k])
    if window_sum == target:
        return arr[:k]

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        if window_sum == target:
            return arr[:k]
    
    return []


if __name__ == "__main__":
    print("Enter the array: ", end="")
    nums = list(map(int, input().split()))
    k = int(input("Enter k: "))
    target = int(input("Enter target: "))
    print(ans(nums, k, target))