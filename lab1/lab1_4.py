def choose(arr):
    for i in range (len(arr)):
        m = i
        for j in range (i, len(arr)):
            if arr[m] > arr[j]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr

print(choose([7,6,10,5,9,8,3,4]))    