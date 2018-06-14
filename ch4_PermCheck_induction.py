def solution(A):
    N = len(A)
    
# test first by induction
    sumA = sum(A)
    sumInduction = (N * (N-1))/2
    if sumA == sumInduction:
        return 1

# create frequency array
    count = [0] * (N+2)
    
    for i in range(0, N):
        if N >= A[i] > 0:
            count[A[i]] += 1

# if last index is empty, iterate up to it    
    if count[-1] == 0:
        for i in range(1, N+1):
            if count[i] != 1:
                return 0

# if last index is not empty, include it
    elif count[-1] > 0:
        for i in range(1, N+2):
            if count[i] != 1:
                return 0
              
    return 1