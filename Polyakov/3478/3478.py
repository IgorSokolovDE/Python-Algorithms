for A in range(1,1000):
    Ok=True
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x*y>A)and(x>y)and(x<8)):
                Ok=False
                break
        if not(Ok):
            break
    if Ok:
        print(A)
        break
