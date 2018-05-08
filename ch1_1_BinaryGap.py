
def solution(N):

    # set up variables to store
    max_gap = 0
    current_gap = 0

    # skip trailing zeros until hit 1
    while N > 0 and N%2 == 0:
        N //=2

    # gap tracker: count, compare
    while N > 0:
        if N%2 == 0:
            current_gap +=1
        elif current_gap > max_gap:
            max_gap = current_gap
            current_gap = 0
        elif current_gap < max_gap:
            current_gap = 0
        elif current_gap == max_gap:
            current_gap = 0
        N //=2

    # here's the result!
    return max_gap

