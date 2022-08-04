def bubble_sort(array)
    for i in 1..array.length - 1
        sorted = true
        for j in 0..array.length - 1
            if array[j] > array[i]
                sorted = false
                array[j], array[i] = array[i], array[j]
            end
        end
        if sorted
            break
        end
    end
    array
end
print bubble_sort([4,3,78,2,0,2])