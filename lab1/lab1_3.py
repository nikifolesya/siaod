def turnir(arr):
    arr2 = []
    while len(arr) > 0:
        for i in range(len(arr)):
            index_head = (i - 1) // 2
            if (arr[i] < arr[index_head]) and (index_head >= 0):
                arr[index_head], arr[i] = arr[i], arr[index_head]
        arr2.append(arr[index_head])
        arr.remove(arr[index_head])
        
    return arr2
                
print(turnir([7,6,10,5,9,8,3,4]))    