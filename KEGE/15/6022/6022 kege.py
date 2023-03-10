for A in range(500):
    ok=True
    for x in range(500):
        for y in range(500):
            if ((x<A)or(y<A)or((x+2*y)>150))==False:
                ok=False
                break
        if not(ok):
            break
    if ok:
        print(A)
        break
