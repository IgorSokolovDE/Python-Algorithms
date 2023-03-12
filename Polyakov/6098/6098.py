k=0
for b in 'ЕЫЯИ':
    for c in 'ХЛЕБНЫЙМЯКИШ':
        for d in 'БЫКИШ':
            for e in 'ХЛЕБНЫЙМЯКИШ':
                for f in 'ХЛЕБНЫЙМЯКИШ':
                    for g in 'ХЛЕБНЫЙМЯКИШ':
                        slovo='Х'+b+c+d+e+f+g
                        if not((c in 'ХЛБНЙМКШ')and (d in 'ХЛБНЙМКШ')):
                            if not((d in 'ХЛБНЙМКШ')and (e in 'ХЛБНЙМКШ')):
                                if not((e in 'ХЛБНЙМКШ')and (f in 'ХЛБНЙМКШ')):
                                    if not((f in 'ХЛБНЙМКШ')and (g in 'ХЛБНЙМКШ')):
                                        porhodit=True
                                        for p in 'ХЛЕБНЫЙМЯКИШ':
                                            if slovo.count(p)>1:
                                                porhodit=False
                                                break
                                        if porhodit:    
                                           k+=1
print(k)                                        
            
    
