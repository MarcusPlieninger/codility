def solution(A):
    A = sorted(A)
    counter = 1
    if len(A) > 0:
        for i in range (1, len(A)):
            if A[i] != A[i-1]:
                counter +=1
        return counter

    else:
        return 0
    
