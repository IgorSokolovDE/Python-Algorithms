from itertools import product
p=product('СПОРТЛ',repeat=9)
c=0
Aslova=[]
for x in p:
    s=''.join(x)
   
    if s.count('О')==3:
        if s.count('Т')==2:
            if s.count('С')==1:
                if s.count('П')==1:
                    if s.count('Р')==1:
                        if s.count('Л')==1:
                            if 'ТТ' in s:
                                
                                if not(s in Aslova):
                                    Aslova.append(s)
print(len(Aslova))                                    
                                
                
