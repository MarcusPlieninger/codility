def solution(S, P, Q):
    ones = []
    twos = []
    threes = []
    fours = []
    sumOnes = sumTwos = sumThrees = sumFours = 0

    for nucleotide in S:
        if nucleotide == "A":
            sumOnes +=1
        if nucleotide == "C":
            sumTwos +=1
        if nucleotide == "G":
            sumThrees +=1
        if nucleotide == "T":
            sumFours +=1
        ones.append(sumOnes)
        twos.append(sumTwos)
        threes.append(sumThrees)
        fours.append(sumFours)

    result = []
    for i in range(len(P)):
        if P[i] == 0:
            A = ones[Q[i]]
            C = twos[Q[i]]
            G = threes[Q[i]]
            T = fours[Q[i]]
        else:
            A = ones[Q[i]] - ones[P[i]-1]
            C = twos[Q[i]] - twos[P[i]-1]
            G = threes[Q[i]] - threes[P[i]-1]
            T = fours[Q[i]] - fours[P[i]-1]
        if A > 0:
            result.append(1)    
        elif C > 0:
            result.append(2)
        elif G > 0:
            result.append(3)
        else:
            result.append(4)
            
    return result
