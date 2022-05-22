# step 1: find the mid point and divide the arr into 2 parts
# step 2: call merge sort for first half,
# step 3: call merge sort for second half
# step 4: merge 2 arrays into a big sorted array

# so there's 2 defs :
# (1) Mergesort, which is a recursion def to divide arrays
# (2) Merge, a def which is used to merge 2 array into 1
def merge(array,left,mid,right):
    #print(f"array {array}")
    #count the sub-array lengths
    left_num = mid - left + 1
    print(f"left num {left_num}")
    right_num = right - mid
    print(f"right num {right_num}")
    #create two sub-array and put numbers into them
    left_sub = [0] * left_num
    right_sub = [0] * right_num
    for i in range(0, left_num):
        left_sub[i] = array[left+i]
        print(f"array[left+i] {array[left + i]}")
    print(f"left sub {left_sub}")

    for i in range(0,right_num):
        right_sub[i] = array[mid+i+1]
        print(f"array[mid+i] {array[mid+i+1]}")
    print(f"right sub {right_sub}")
    #merge them into 1
    j, k = 0, 0
    l = left
    while j < left_num and k < right_num:
        if left_sub[j] <= right_sub[k]:
            array[l] = left_sub[j]
            j += 1
        else:
            array[l] = right_sub[k]
            k += 1
        l += 1
    while k < right_num:
        array[l] = right_sub[k]
        k += 1
        l += 1

    while j < left_num:
        array[l] = left_sub[j]
        j += 1
        l += 1


    print(f"array {array}")




def merge_sort(array ,left, right):
    if left < right:
        mid = (left + right) // 2
        print(f"mid {mid}")
        merge_sort(array,left,mid)
        merge_sort(array,mid+1,right)
        merge(array,left,mid,right)


if __name__ == '__main__':
    a = [1,0]
    merge_sort(a,0,len(a)-1)
    print(a)

