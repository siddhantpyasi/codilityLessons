def jumpCount(X, Y, D):
    estimate = (Y-X)//D
    if ((estimate * D) + X) < Y:
        return estimate + 1
