k=0
for a in "СПОРТЛ":
    for b in "СПОРТЛ":
        for c in "СПОРТЛ":
            for d in "СПОРТЛ":
                for e in "СПОРТЛ":
                    for f in "СПОРТЛ":
                        for g in "СПОРТЛ":
                            for h in "СПОРТЛ":
                                for i in "СПОРТЛ":
                                    s=a+b+c+d+e+f+g+h+i
                                    if a!=i:
                                        if s.count("О")==3:
                                            if s.count("Т")==2:
                                                if s.count("С")==1:
                                                    if s.count("П")==1:
                                                        if s.count("Р")==1:
                                                            if s.count("Л")==1:
                                                                k+=1
                                                            

                        
print(k)
