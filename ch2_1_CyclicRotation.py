def solution(A, K):
    
    N = len(A)
    B = [0] * N 

    for i in range (0,K):
        for j in range (0,N):
            if j < N-1:
                m = j+1
                B[m] = A[j]
            else:
                m = N - j - 1
                B[j] = A[m]
            return B

