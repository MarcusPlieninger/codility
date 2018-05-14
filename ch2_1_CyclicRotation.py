def solution(A,K):
    
    N = len(A)
    B = [0] * N 

    for i in range (0,K):
        for j in range (0,N):
            if j == 0:
                m = N-1
            else:
                m = j-1
            B[j] = A[m]
        A = B[:]
    return B

