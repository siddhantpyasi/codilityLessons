"""
What is this solution about?
If the list has only two elements, it returns the difference of the two
If more, the procedure followed is-
    1. take the difference between the first element and the sum of the rest, store it in "diff"
    2. add second element to first sum, remove it from second sum. See the diff. If < diff, diff = new difference
    3. Keep going till you've done this for all elements
"""
def solution(A):

    if len(A) == 2:
        return abs(A[0] - A[1])

    firstSet = A[0]
    secondSet = sum(A[1:])

    diff = abs(firstSet - secondSet)
    for i in range(1, len(A)-1):
        firstSet = firstSet + A[i]
        secondSet = secondSet - A[i]
        trial = abs(firstSet - secondSet)
        diff = min(diff, trial)

    return diff







print(solution([3,1,2,4,3]))
