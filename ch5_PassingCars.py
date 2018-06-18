def solution(A):

    going_east = 0
    pairs = 0

    for car in A:
        # if the car is going east
        if car == 0:
            going_east +=1
        # if the car is going west
        else:
            pairs += going_east
        # check pairs
            if pairs > 1000000000:
                return -1

    return pairs