Zapret=['ОО', 'ОА', 'ОЕ', 'АО', 'АА', 'АЕ', 'ЕО', 'ЕА', 'ЕЕ']
k=0
for a in 'КОНФЕТА':
    for b in 'КОНФЕТА':
        for c in 'КОНФЕТА':
            for d in 'КОНФЕТА':
                for e in 'КОНФЕТА':
                    slovo=a+b+c+d+e
                    kgl=slovo.count("О")+slovo.count("А")+slovo.count("Е")
                    if kgl==2:
                       podhodit=True
                       for nelza in Zapret:
                           if nelza in slovo:
                               podhodit=False
                               break
                       if podhodit:
                           k+=1
                    if kgl==3:
                        if (b in 'КНТФ')and (d in 'КНТФ'):
                            k+=1
print(k)                            
                        
