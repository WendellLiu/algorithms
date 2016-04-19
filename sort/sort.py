def quick_sort(array, asc=True):
    begin = 0
    end = len(array)-1
    if len(array) < 2:
        return array

    pivot = begin
    for j in xrange(begin+1, end+1):
        if (array[j] <= array[begin]) == asc:
            pivot +=1
            array[pivot] ,array[j] = array[j], array[pivot]

    array[pivot], array[begin] = array[begin], array[pivot]

    left_list = quick_sort(array[begin:pivot], asc)
    right_list = quick_sort(array[pivot+1: end+1], asc)

    return left_list + [array[pivot]] + right_list

def insertion_sort(array, asc=True):
    for i in xrange(1, len(array)):
            pivot = i
            while pivot > 0 and ((array[pivot] <= array[pivot-1]) == asc):
                array[pivot], array[pivot-1] = array[pivot-1], array[pivot]
                pivot -= 1

    return array
