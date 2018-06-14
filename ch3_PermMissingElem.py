def solution(A):

    N = len(A) + 1
    result = (N * (N + 1)//2) - sum(A)
    
    return result