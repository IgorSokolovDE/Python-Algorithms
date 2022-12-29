for A in range(1,1000):
    ok=True
    for x in range(1,1000):
        if (  ((x%3!=0)and(not(x in [48,52,56])))<=( ((abs(x-50)<=7)<=(29<=x<=47))or(x&A==0) ))==False:
            ok=False
            break
    if ok:
        print(A)
        break
