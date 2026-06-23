def min_avg(arr:list[int], k: int) -> float:
    n = len(arr)

    window_sum = sum(arr[:k]) 
    window_avg = window_sum / k
    min_avg = window_avg

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        window_avg = window_sum / k
        min_avg = min(min_avg, window_avg)

    return min_avg


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(min_avg(nums, k))

