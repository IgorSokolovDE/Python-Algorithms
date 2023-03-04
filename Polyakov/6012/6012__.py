for x in range(17):
    y=(3*17**4+11*17**3+8*17**2+x*17+1)+(2*17**4+x*17**3+9*17**2+x*17+3)
    k5=0
    w=y
    while w>0:
        if w%6==5:
            k5+=1
        w//=6
    if k5==3:
        print(y)
        break
