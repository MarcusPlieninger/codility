def solution(X, A):

    pathToTravel = [-1] * (X + 1)
    covered = 0

    for i in range(len(A)):
        if pathToTravel[A[i]] == -1:
            pathToTravel[A[i]] = i
            covered += 1
            if covered == X:
                return i
                
    return -1