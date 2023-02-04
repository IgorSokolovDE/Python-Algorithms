for A in range(1000,0,-1):
    Ok=True
    for x in range(1000):
        for y in range(1000):
            if (((x+y)<=22)or(y<=(x-6))or(y>=A))==False:
                Ok=False
                break
        if not(Ok):
            break
    if Ok:
        print(A)
        break
