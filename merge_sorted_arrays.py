import random


def merge(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0

    ans = []
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < m:
        ans.append(arr1[i])
        i += 1
    
    while j < n:
        ans.append(arr2[j])
        j += 1
    
    return ans



if __name__ == "__main__":
    arr1 = [random.randrange(0, 101) for _ in range(10)]
    arr2 = [random.randrange(0, 101) for _ in range(10)]

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    print(arr1)
    print(arr2)

    print(merge(arr1, arr2))