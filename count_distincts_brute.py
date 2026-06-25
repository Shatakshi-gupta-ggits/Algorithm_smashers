def distincts(arr:list[int], k:int)->list[int]:
    ans:list[int] = []
    for i in range(len(arr) - k + 1):
        ans.append(len(set(arr[i:i+k])))
            
    return ans



if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())

    print(distincts(nums, k))

