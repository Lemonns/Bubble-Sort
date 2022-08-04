def bubble_sort(array):
    for i in range(1, len(array)):
        sorted = True
        for j in range(len(array)-1):
            if array[j] > array[i]:
                sorted = False
                array[j], array[i] = array[i], array[j]
        if sorted:
            break
    return array

print(bubble_sort([4,3,78,2,0,2]))
#[0,2,2,3,4,78]