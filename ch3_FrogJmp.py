def solution(X, Y, D):

    if (Y-X)//D * D < (Y-X):
        return (Y-X)//D + 1
        
    else:
        return (Y-X)//D