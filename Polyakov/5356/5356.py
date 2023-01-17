for A in range(1000,0,-1):
    ok=True
    for x in range(0,1000):
        for y in range(0,1000):
            if ( ((x+y)<=22)or(y<=(x-6))or(y>=A) )==False:
                ok=False
                break
        if not(ok):
            break
    if ok:
        print(A)
        break
    
