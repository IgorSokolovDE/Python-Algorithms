for A in range(1,10000):
    ok=True
    for x in range(1000):
        for y in range(1000):
            if ((75!=(2*x+3*y))or(A>3*x)or(A>2*y))==False:
                ok=False
                break
        if not(ok):
            break
    if ok:
        print(A)
        break
