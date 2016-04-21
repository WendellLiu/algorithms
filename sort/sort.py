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

