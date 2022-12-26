kol=0
for a in 'СПОРТЛ':
    for b in 'СПОРТЛ':
        for c in 'СПОРТЛ':
            for d in 'СПОРТЛ':
                for e in 'СПОРТЛ':
                    for f in 'СПОРТЛ':
                        for g in 'СПОРТЛ':
                            for h in 'СПОРТЛ':
                                for i in 'СПОРТЛ':
                                    slovo=a+b+c+d+e+f+g+h+i
                                    if 'ОО' in slovo:
                                            if slovo.count('О')==3:
                                                if slovo.count('Т')==2:
                                                    if slovo.count('С')==1:
                                                        if slovo.count('П')==1:
                                                            if slovo.count('Р')==1:
                                                                if slovo.count('Л')==1:
                                                                    kol+=1

                                        
print(kol)                            
    
