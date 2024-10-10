array = [5, 7, 9, 0, 3, 1, 6, 2, 4]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    no_pivot = array[1:]
    
    left = []
    right = []
    for i in no_pivot:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_listCom(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    no_pivot = array[1:]
    
    left = [x for x in no_pivot if x <= pivot]
    right = [x for x in no_pivot if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_sort_norm(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[right]:
            left += 1
        
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    
    quick_sort_norm(array, start, right-1)
    quick_sort_norm(array, right+1, end)

print(quick_sort(array))
print(quick_sort_listCom(array))

quick_sort_norm(array, 0, len(array)-1)
print(array)