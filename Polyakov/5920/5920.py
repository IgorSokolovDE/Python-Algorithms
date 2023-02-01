
for A in range(1000,0,-1):
    OK=True
    for x in range(1,200):
        for y in range(1,200):
            for z in range(1,200):
                if (((z%115==0)or(y%78==0)or(x%51==0))<=((x*y*z)%A==0))==False:
                    OK=False
                    break
            if not(OK):
                break
        if not(OK):
            break
    if (OK):
        print(A)
        break        
    
