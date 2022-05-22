# quick sort is an in-place sorting algorithm (auxillary space:O(1))
# recursive steps are as follows (partition function):
# step 1: choose a pivot
# step 2.1: put all the numbers less than pivot to the left
# step 2.2: put all the numbers larger than pivot to the right


# the partition function will return the index of the pivot
def partition(array, start, end):
    # select the last element as the pivot
    # iterate from the start to end to determine the pivot index
    pivot = array[end]
    pivot_index = start
    for i in range(start,end):
        if array[i] < pivot:
            # swap(array[i],array[pivot_index])
            (array[i], array[pivot_index]) = (array[pivot_index], array[i])

            pivot_index += 1
    # swap(array[end],array[pivot_index])
    (array[pivot_index], array[end]) = (array[end], array[pivot_index])


    return pivot_index



def quick_sort(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)

if __name__ == '__main__':
    array = [1,1,0]
    quick_sort(array,0,len(array) - 1)
    print(array)