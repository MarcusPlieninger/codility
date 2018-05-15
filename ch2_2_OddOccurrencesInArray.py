def solution(A):
    N = len(A)
    while N > 0:
        a = A.count(A[i])
        if a//2 == 0:
            for j in range (0,N):
                if A[j] == A[i]:
                    list.remove(A[j])
        i +=1
        N = len(A)
    return A

# listcomp?
# def solution(A):
#   A = [x for x in A if A.count(x)//2 != 0]
#    return A