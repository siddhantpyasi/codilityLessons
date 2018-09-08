def solution(a, K):

    b = ['']*len(a)
    for m in range(K):
        for i in range(len(a)):
            if i == len(a)-1:
                b[0] = a[i]
            else:
                b[i+1] = a[i]
#            print(b)
        a = b
        b = ['']*len(a)

    return a
