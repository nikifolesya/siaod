def quick_sort(arr):
    if (len(arr)) <= 1:
        return arr
    num = arr[0]
    left = []
    middle = []
    right = []
    for i in range(len(arr)):
        if arr[i] < num:
            left.append(arr[i])
        elif arr[i] == num:
            middle.append(arr[i])
        elif arr[i] > num:
            right.append(arr[i])    
    return quick_sort(left) + middle + quick_sort(right)

print(quick_sort([7,6,10,5,9,8,3,4]))        