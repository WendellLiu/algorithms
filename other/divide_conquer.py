def maximum_subarray(array, low, high):
    if low == high:
        return (low, high, array[low])
    else:
        mid = (low+high)/2
        (left_low, left_high, left_max) = maximum_subarray(array, low, mid)
        (right_low, right_high, right_max) = maximum_subarray(array, mid+1, high)
        (cross_low, cross_high, cross_max) = maximum_cross_subarray(array, low, high)

    if left_max >= right_max and left_max >= cross_max:
        return (left_low, left_high, left_max)
    elif right_max >= cross_max:
        return (right_low, right_high, right_max)
    else:
        return (cross_low, cross_high, cross_max)

def maximum_cross_subarray(array, low, high):
    # wrong!
    # length = high - low + 1
    # mid = length/2 + low

    mid = (low+high)/2

    tmp_sum = 0
    left_sum = -float('infinity')
    for i in xrange(mid, low-1, -1):
        tmp_sum += array[i]
        if tmp_sum > left_sum:
            left_sum = tmp_sum
            left_anchor = i

    tmp_sum = 0
    right_sum = -float('infinity')
    for j in xrange(mid+1, high+1):
        tmp_sum += array[j]
        if tmp_sum > right_sum:
            right_sum = tmp_sum
            right_anchor = j

    return (left_anchor, right_anchor, left_sum+right_sum)
