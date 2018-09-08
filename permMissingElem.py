def missingElement(A):
    A.sort()
    print(A)
    pairWiseDiff = {}
    for i in range(len(A)):
        if i+1 == len(A): 
            break
        else:
            pairWiseDiff[i] = A[i+1] - A[i]
            print(A[i], A[i+1])

    print(pairWiseDiff)

    invert = {}
    for key, value in pairWiseDiff.items():
        if value in invert:
            invert[value].append(key) 
        else:
            invert[value] = [key]
    
    itemToReturn = 0
    valToAdd = 0

    for key, value in invert.items():
        if len(value) > 1:
            valToAdd = key
        else:
            itemToReturn = A[value[0]]

    return itemToReturn + valToAdd  
