def quicksort(l):
    if not l:
        return []
    else:
        return partition(l)


def partition(l):
    begin = 0
    end = len(l)-1
    if len(l) < 2:
        return l

    pivot = begin
    for j in xrange(begin+1, end+1):
        if l[j] <= l[begin]:
            pivot +=1
            l[pivot] ,l[j] = l[j], l[pivot]
    l[pivot], l[begin] = l[begin], l[pivot]

    left_list = partition(l[begin:pivot])
    right_list = partition(l[pivot+1: end+1])

    return left_list + [l[pivot]] + right_list

