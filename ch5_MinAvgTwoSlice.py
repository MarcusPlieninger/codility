def solution(A):
    smalleststartingposition = 0
    minimalavg = (A[0] + A[1]) / 2
    
    for i in range(2, len(A)):
        avg2 = (A[i-1] + A[i]) / 2 
        avg3 = (A[i-2] + A[i-1] + A[i]) / 3
        
        if avg2 < minimalavg:
            minimalavg = avg2
            smalleststartingposition = i-1
            
        if avg3 < minimalavg:
            minimalavg = avg3
            smalleststartingposition = i-2
            
    return smalleststartingposition
    