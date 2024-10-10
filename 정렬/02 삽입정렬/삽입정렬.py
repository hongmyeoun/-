array = [7, 5, 9, 0, 3, 1, 6, 2, 4]

for i in range(1, len(array)): # i는 비교할 대상(정렬 되지 않은것)
    for j in range(i, 0, -1): # i부터 0까지 내려오면서, j는 정렬되어 있는 것
        if array[j] < array[j-1]: # 정렬된 위치중 가장 뒷부분과 비교
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break # 정렬된 값보다 크면 맨뒤에 위치

print(array)