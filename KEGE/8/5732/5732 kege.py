def F(x,y):
    global ksposob
    #print(x,y,ksposob)
    #iii=input()
    if (x>11)or(y>11):
        return
    if (x==11)and(y==11):
        ksposob+=1
        return
    else:
        if x<11: 
           F(x+1,y)
        if y<11:
           F(x,y+1)
ksposob=0
F(1,1)
print(ksposob)
