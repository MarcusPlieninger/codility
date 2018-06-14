def solution(A):
    N = len(A)
    count = [0]*(N + 1)
    
    for i in A:
        if N >= i > 0:
            count[i] += 1
            
    for j in range(1, N+1):
        if count[j] == 0:
            return j
    
    return N+1