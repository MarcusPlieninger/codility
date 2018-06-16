def solution(A, B, K):
    if K > A:
        A = K

    while B % K !=0:
        B -=1
 
    for i in range(A, B+1):
        A += A+i

    divisiblecount = 0
    while A % K == 0:
        A /=K
        divisiblecount +=1

    return divisiblecount




