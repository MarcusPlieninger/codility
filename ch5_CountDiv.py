def solution(A, B, K):
    result = B // K - A // K
    if A % K == 0:
        result += 1
    
    return result