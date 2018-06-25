'''
This version satisfies O(1) space complexity requirement.

def solution(A):
    A = sorted(A)
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])

'''
'In this version, space complexity is bounded by O(N).'

def solution(A):

    def mergeSort(aList):)
        if len(aList) > 1:
            midPoint = len(aList) // 2 
            leftHalf, rightHalf = A[:midPoint], A[midPoint:]
           
            mergeSort(lefHalf)
            mergeSort(rightHalf)
            
        iLeftHalf = iRightHalf = iFinalListResult = 0
        n1, n2 = len(lefHalf), len(rightHalf)
        # loop while lefHalf and rightHalf have more items
        while iLeftHalf < len(leftHalf) and len(rightHalf) < n2:
            if lefHalf[iLeftHalf] < rightHalf[iRightHalf]:
                A[iFinalListResult] = lefHalf[iLeftHalf]
                iLeftHalf += 1
            else:
                A[iFinalListResult] = rightHalf[iRightHalf]
                iRightHalf += 1
            iFinalListResult +=1
        # copy any remaining items from lefHalf
        while iLeftHalf < n1:
            A[iFinalListResult] = lefHalf[iLeftHalf]
            iLeftHalf += 1
            iFinalListResult += 1
        # copy any remaining items from rightHalf
        while iRightHalf < n2:
            A[iFinalListResult] = rightHalf[iRightHalf]
            iRightHalf += 1
            iFinalListResult += 1

    A = mergeSort(A)
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
