for A in range(1,1000):
    ok=True
    for x in range(1,1000):
        if ( ((x%7==0)<=(x%21!=0))or((2*x+A)>=120) )==False:
            ok=False
            break
    if ok:
        print(A)
        break
