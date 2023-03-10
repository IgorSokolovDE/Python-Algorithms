for A in range(1000,0,-1):
    ok=True
    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                if((150!=(y+2*x+2*z))or(A<x)or(A<y)or(A<z))==False:
                    ok=False
                    break
            if not(ok):
                break
        if not(ok):
                break
    if (ok):
                print(A)
                break
