def distincts(arr:list[int], k:int)->list[int]:
    n = len(arr)

    ans:list[int] = []
    freq:dict[int, int] = {}

    for x in arr[:k]:
        freq[x] = freq.get(x, 0) + 1
    
    count = 0
    for x in arr[:k]:
        if freq[x] == 1:
            count += 1
    
    ans.append(count)


    # 1 2 1 2 3 4 5 
    for i in range(k, n):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

    return []



if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(distincts(nums, k))