for A in range(1,1000):
    ok=True
    for x in range(1,1000):
        if(((x%3==0)<=(x%17!=0))or(not(A<(190-x))))==False:
            ok=False
            break
    if ok:
        print(A)
        break
