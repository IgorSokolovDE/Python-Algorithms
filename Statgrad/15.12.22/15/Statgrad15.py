for A in range(1,100000000):
    ok=True
    for x in range(1,1000):
        for y in range(1,1000):
            if (((144%x==0)<=(x%y!=0))or((x+y)>100)or((A-x)>y))==False:
                ok=False
                break
        if not(ok):
            break
    if ok:
        print(A)
        break
