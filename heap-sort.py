#
# turn an array into a max heap (O(n))
# pop the root of this max heap every time
# let the last leave become the root and max heapify the heap(O(log(n)))
# with a total of O(nlogn) time complexity

# input: current_node is the index of the node, array length is the length of
# the full array
# left child -> 2i + 1
# right child -> 2i + 2
# parent -> [i/2]
# max-heapify describe a base case, for example:
#   2               4
# /   \    -->    /   \
#4     1        2       1
def max_heapify(array,current_node,arr_length):
    largest_node = current_node
    left_child = 2 * current_node + 1
    right_child = 2 * current_node + 2
    # attention: recursion ** need a boundary **  !!
    if left_child < arr_length and array[left_child] > array[largest_node]:
        largest_node = left_child

    if right_child < arr_length and array[right_child] > array[largest_node]:
        largest_node = right_child
    print(f'largest node {array[largest_node]}')
    print(f'current node {array[current_node]}')
    # array[left_child] > array[current_node] or array[right_child] > array[current_node]
    if largest_node != current_node:
        (array[largest_node], array[current_node]) = (array[current_node], array[largest_node])
        print(f'swapped array{array}')
        max_heapify(array, largest_node, arr_length)


# delete the root (which is the element at the top)
# max-heapify the array again
def heap_sort(array):
    # max-heapify the array
    # because leaves dont have child, so we start from n//2
    # and iterate only all the ancestors
    arr_length = len(array)
    # iterate from arr_length//2 to 0 (because the stop point is not included)
    for i in range(arr_length // 2, -1, -1):
        max_heapify(array, i, arr_length)

    # remove the root and let the last leave be the root
    # for range(n-1,0,-1) here means we do not iterate index 0
    for i in range(arr_length-1,0,-1):
        # swap the leave with root
        (array[i], array[0]) = (array[0], array[i])
        # max-heapify the new heap without the old root
        max_heapify(array, 0, i)


if __name__ == '__main__':
    array = [4,3,9,2,1]
    heap_sort(array)
    print(array)