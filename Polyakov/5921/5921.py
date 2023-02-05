def SumBol(s,d):
    if (s+d)>0:
        return True
    else:
        return False
def DEL(n,m):
    if x%7==0:
        return True
    else:
        return False 
for A in range(1,1000):
    ok=True
    for x in range(1,1000):
        if (((x+A)>=160)or((DEL(x,7))<=(not(SumBol(x,-17)))))==False:
            ok=False
            break
    if ok:
        print(A)
        break
