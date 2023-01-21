def C(n):
    if n==0:
        return 1
    else:
        Sum=0
        for i in range(0,n):
            Sum+=C(i)*C(n-1-i)
        return Sum
print(C(12))    
