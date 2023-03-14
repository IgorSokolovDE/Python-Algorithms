k=0
for x in range(int('1000000',9),int('8888888',9)):
    x9=''
    y=x
    while y>0:
        x9=str(y%9)+x9
        x=x//9
    if x9.count('8')==1:
        kolNech=0
        for cifr in x9:
            if int(cifr)%2!=0:
                kolNech+=1
        if kolNech==4:
            k+=1
print(k)           
