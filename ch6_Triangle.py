'''
because A is sorted, the following obtains:
A[i] <= A[i+1] <= A[i+2]
A[i] <= A[i+2]

therefore:
A[i] < A[i+1] + A[i+2]
A[i+1] < A[i] + A[i+2]

Triangular is defined by:
0 <= A[i] < A[i+1] < A[i+2] < N (satisfied by above)
A[i] + A[i+1] > A[i+2] this criterion must be checked
A[i+1] + A[i+2] > A[i] (satisfied by above)
A[i+2] + A[i] > A[i+1] (satisfied by above)

'''

def solution(A):
    if len(A) < 3:
         return 0
    
    A = sorted(A)
    
    for i in range(0, len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
            
    return 0