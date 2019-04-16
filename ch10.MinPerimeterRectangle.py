def solution(N):
    from math import sqrt
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return 2 * int(i+N/i)
# not sure why 'int' is necessary in the return statement
# smallest perimeter is a square