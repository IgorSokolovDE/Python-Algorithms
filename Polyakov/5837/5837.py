k=0
for a in 'АМФИХЙ':
    for b in 'АМФИХЙ':
        for c in 'АМФИХЙ':
            for d in 'АМФИХЙ':
                for e in 'АМФИХЙ':
                    for f in 'АМФИХЙ':
                        for g in 'АМФИХЙ':
                            for h in 'АМФИХЙ':
                                s=a+b+c+d+e+f+g+h
                                if s.count('А')==2:
                                    if s.count('И')==2:                                        
                                        if s.count('М')==1:
                                            if s.count('Ф')==1:
                                                if s.count('Х')==1:
                                                    if s.count('Й')==1:
                                                        k+=1
print(k)
                                
