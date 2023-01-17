def F(n):
    #print(n)
    #ii=input()
    global X
    if n < 64:
        return
    if n == 64:
   
        X+=1
        #print(X)
        #ii=input()
        return
    else:
        F(n-2)
        x=n//10
        y=n%10
        if x!=0 and y!=0:
            minCifr=min(x,y)
        else:
            if x!=0: minCifr=x
            else: minCifr=y
        F(n-minCifr)
        if n%4>0:
          F(n-n%4)
def F2(n):
    global Y
    if n<60: return
    if n==60:
        Y+=1
        return
    else:
        F2(n-2)
        x=n//10
        y=n%10
        if x!=0 and y!=0:
            minCifr=min(x,y)
        else:
            if x!=0: minCifr=x
            else: minCifr=y
        F2(n-minCifr)
        if n%4>0:
          F2(n-n%4)       
X=0
F(96)
Y=0
F2(64)
print(X*Y)
        
