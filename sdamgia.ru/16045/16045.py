for A in range(1000,0,-1):
    ok=True
    for x in range(1000):
        for y  in range(1000):
            if (((y+2*x)!=48)or(A<x)or(A<y))==False:
                ok=False
                break
        if not(ok):
            break
    if ok:
        print(A)
        break
