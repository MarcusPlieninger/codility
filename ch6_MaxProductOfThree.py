def solution(A):

    def mergeSort(A):
        n = len(A)
        if n > 1:
            # reduce input (ie, divide)
            m = n // 2 
            A1, A2 = A[:m], A[m:]
            # create call stack by calling function on each half (ie, recursion)
            mergeSort(A1)
            mergeSort(A2)
            # merge pieces back to original list in sorted order (ie, conquer)
            merge(A1, A2, A)
        return A

    # merge A1 and A2 into A
    def merge(A1, A2, A):
        # keep track of current index in each list
        iA1, iA2, iA = 0, 0, 0 # all start at front
        n1, n2 = len(A1), len(A2)
        # loop while A1 and A2 have more items
        while iA1 < n1 and iA2 < n2:
            if A1[iA1] < A2[iA2]:
                A[iA] = A1[iA1]
                iA1 += 1
            else:
                A[iA] = A2[iA2]
                iA2 += 1
            iA +=1
        # copy any remaining items from A1
        while iA1 < n1:
            A[iA] = A1[iA1]
            iA1 += 1
            iA += 1
        # copy any remaining items from A2
        while iA2 < n2:
            A[iA] = A2[iA2]
            iA2 += 1
            iA += 1

    # max product
    A = mergeSort(A)
    product = A[-1] * A[-2] * A[-3]
    return product
