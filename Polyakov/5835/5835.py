from itertools import product
p=product('АМФИБРХЙ',repeat=10)
c=0
for x in p:
    s=''.join(x)
    if s.count('А')==2:
        if s.count('И')==2:
            if s.count('Ф')==1:
                if s.count('М')==1:
                    if s.count('Б')==1:
                        if s.count('Р')==1:
                            if s.count('Х')==1:
                                if s.count('Й')==1:
                                    if s[:2]=='АМ':
                                        if s[-2:]=='ИЙ':
                                            c+=1
print(c)                                            
                                    
                                

                
