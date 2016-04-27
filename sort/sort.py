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

def merge_sort(array, asc=True):
    begin = 0
    end = len(array)-1

    if len(array) > 1:
        # partition
        l = array[begin:len(array)/2]
        r = array[len(array)/2:end+1]
        l = merge_sort(l, asc)
        r = merge_sort(r, asc)

    else:
        return array

    return merge(l, r, asc)

def merge(sorted_l, sorted_r, asc):

    l_index = 0
    r_index = 0
    result = [0] * (len(sorted_l+sorted_r))

    i = 0
    while True:
        if (l_index < len(sorted_l)) and (r_index < len(sorted_r)):
            if (sorted_l[l_index] <= sorted_r[r_index]) == asc:
                result[i] = sorted_l[l_index]
                l_index += 1
                i += 1
            else:
                result[i] = sorted_r[r_index]
                r_index +=1
                i += 1
        else:
            result[i:] = sorted_l[l_index:] if r_index == len(sorted_r) else sorted_r[r_index:]
            return result

def bubble_sort(array, asc=True):
    for i in xrange(len(array)):
        for j in xrange(len(array)-1-i):
            if (array[j] > array[j+1]) == asc:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def heap_left(i):
    return (2*(i+1))-1

def heap_right(i):
    return (2*(i+1)+1)-1

class heaped_list(list):
    def __init__(self, *args):
        super(heaped_list, self).__init__(*args)
        self.heap_size = len(self)

def max_heapify(array, i):
    l = heap_left(i)
    r = heap_right(i)

    if l < array.heap_size and array[i] < array[l]:
        largest = l
    else:
        largest = i
    if r < array.heap_size and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        array = max_heapify(array, largest)
    return array

def build_max_heap(array):
    """
    guaruntee the root of heaped array is the maximum
    """
    start = (array.heap_size)/2 -1
    for i in xrange(start, -1, -1):
        array = max_heapify(array, i)

    return array

def heap_sort(array):
    array = heaped_list(array)
    array = build_max_heap(array)
    start = len(array)-1
    end = 1
    for i in xrange(start, end-1, -1):
        array[0], array[i] = array[i], array[0]
        array.heap_size -= 1
        array = max_heapify(array, 0)

    return array
