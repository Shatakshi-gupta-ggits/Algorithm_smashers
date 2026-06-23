def distinct(arr:list[int])->int:
    freq:dict[int, int] = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for x in arr:
        if freq[x] == 1:
            return x
    return -1




if __name__ == "__main__":
    nums = list(map(int, input().split()))


    print(distinct(nums))