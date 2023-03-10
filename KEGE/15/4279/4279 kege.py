for A in range(1,1000000):
    ok=True
    for x in range(1,3000):
        if ((x&1097==0)<=((x&2047!=0)<=(x&A!=0)))==False:
            ok=False
            break
    if ok:
        print(A)
        break
