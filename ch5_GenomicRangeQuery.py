def solution(S, P, Q):
    n = len(P)

    S = list(S)
    impactfactor = []
    for nucleotide in S:
        if nucleotide == "A":
             impactfactor.append(1)
        elif nucleotide == "C":
             impactfactor.append(2)
        elif nucleotide == "G":
             impactfactor.append(3)
        elif nucleotide == "T":
             impactfactor.append(4)

    result = []

    for i in range (0, n):
        if P[i] == Q[i]:
            result.append(impactfactor[P[i]])
        else:
            result.append(min(impactfactor[P[i]:Q[i]]))

    return result