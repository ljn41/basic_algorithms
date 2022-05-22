# let A[n] be given
# step 1: set a key A[i]
# step 2: swap the elements(A[0: i-1] )before the key until all of them are sorted
# step 3: let A[i+1] be the new key

def insertionSort(A):
    for i in range(1,len(A)):
        for j in range(0,i):
            if A[j] > A[i]:
                temp1 = A[j]
                temp2 = A[i]
                A[i] = temp1
                A[j] = temp2
    return A
if __name__ == '__main__':
    array = [3,6,4,1,2]
    print(insertionSort(array))