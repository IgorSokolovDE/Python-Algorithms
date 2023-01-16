def F(x,y):
    global k
    if (x>17)or(y>27):
        return
    if (x==17)and(y==27):
        k+=1
    else:
        F(x+1,y)
        F(x*2,y)
        F(x,y+3)


k=0
F(1,0)
print(k)
