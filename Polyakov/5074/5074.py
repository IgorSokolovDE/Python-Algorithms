def F(n,moschno):
    global x1
    global xnot1
    if n>11: return
    if n==11:
        if moschno:
           xnot1+=1
        else:
           x1+=1 
        return
    else:
        if moschno:
            F(n+1,False)
        F(n+2,True)
        F(n*2,True)
def F2(n,moschno):
    global y
    if (n>79)or(n==23): return
    if n==79:
        y+=1
        return
    else:
        if moschno:
            F2(n+1,False)
        F2(n+2,True)
        F2(n*2,True)
def F3(n,moschno):
    global y2
    if (n>79)or(n==23): return
    if n==79:
        y2+=1
        return
    else:
        if moschno:
            F3(n+1,False)
        F3(n+2,True)
        F3(n*2,True)        
x1=0
xnot1=0
F(3,True)
y=0
y2=0
F2(11,False)
F3(11,True)
print(x1*y+xnot1*y2)
