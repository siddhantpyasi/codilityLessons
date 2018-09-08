
def count(A):
    numbers = {}

    for item in range(len(A)):
        if A[item] in numbers:
            numbers[A[item]] = numbers[A[item]] + 1
        else:
            numbers[A[item]] = 1

    # Print out all the items
#    print(numbers)
    

    for key, value in numbers.items():
        if value % 2 != 0:
            return key
