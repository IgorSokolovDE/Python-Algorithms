Moscno=[40,41,42,43,44,45,46,47,48,49]
def F(n,S):
        global kpr
        #print(n,S,Moscno)
        #iii=input()
    
        if n==42 and len(S)>0:
              kpr+=1
              return
        else:   
            if (n+1) in Moscno:
                num=Moscno.index(n+1)
                Moscno.pop(num)
                #print('+1')
                F(n+1,S+'+1')
                Moscno.append((n+1))
                
            if (n+3) in Moscno:
                num=Moscno.index(n+3)
                Moscno.pop(num)
                #print('+3')
                F(n+3,S+'+3')
                Moscno.append((n+3))
            if (n-1) in Moscno:
                num=Moscno.index(n-1)
                Moscno.pop(num)
                #print('-1')
                F(n-1,S+'-1')
                Moscno.append((n-1))
            if (n-3) in Moscno:
                num=Moscno.index(n-3)
                Moscno.pop(num)
                #print('-3')
                F(n-3,S+'-3')
                Moscno.append((n-3))        
kpr=0
F(42,"")                
print(kpr)            
