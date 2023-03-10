MaxSum=0
for x in range(0,2**20):
    y=bin(x)[2:]
    y='0'*(20-len(y))+y
    if (not('1111' in y))and(not('0000' in y)):
        y=y+'<'
        
        
        while ('0<' in y)or('1<' in y):
            if ('11<' in y)or('10<' in y) :
                if ('11<' in y):
                    y=y.replace('11<','<3',1)
                else:
                    y=y.replace('10<','<2',1)
            else:
                if ('00<' in y):
                    y=y.replace('00<','<0',1)
                if ('01<' in y):
                    y=y.replace('01<','<1',1)
         
        SumCh=0
        for s in y:
             if s!='<':
                SumCh+=int(s)
        MaxSum=max(MaxSum,SumCh)
        
print(MaxSum)         
             
             
