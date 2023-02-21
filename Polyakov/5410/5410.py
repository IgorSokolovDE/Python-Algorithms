for A in range(1000,0,-1):
    ok=True
    for x in range(0,300):
        for y in range(0,300):
            if(((2*y+x)!=70)or(x<y)or(A<x))==False:
                ok=False
                break
            
        if not(ok):
                break
    if ok:
        print(A)
        break
