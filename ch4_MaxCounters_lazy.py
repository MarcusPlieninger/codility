def solution(N, A):

    count = [0] * N
    maxCounter = currentMax = 0
    
    for i in A:
        if 1 <= i <= N:
            if maxCounter > count[i-1]:
                count[i-1] = maxCounter
            count[i-1] +=1
            
            if currentMax < count[i-1]:
                currentMax = count[i-1]
                
        else: 
             maxCounter = currentMax
        
    for j in range(0,N):
        if count[j] < maxCounter:
            count[j] =+ maxCounter
    
    return count