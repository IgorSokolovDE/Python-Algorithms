kol=0
for a in 'КАПЫ':
    for b in 'КАРПЫ':
        for c in 'КАРПЫ':
            for d in 'КАРПЫ':
                for e in 'КАПЫ':
                    slovo=a+b+c+d+e
                    if (not('АЫ' in slovo)) and (not('ЫA' in slovo)):
                        if slovo.count("К")==1:
                            if slovo.count("А")==1:
                                if slovo.count("Р")==1:
                                    if slovo.count("П")==1:
                                        if slovo.count("Ы")==1:
                                            kol+=1
print(kol)                                            
                                            
                    
                    
