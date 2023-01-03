
F=[0]*60
for n in range(60):
    if n<3:
        F[n]=3*n
    else:
        if n%2==0:
            F[n]=F[n-2]*F[n-1]-n
        else:
            F[n]=F[n-1]-F[n-2]+2*n
    print(n,str(F[n])[-2:])        
