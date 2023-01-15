k=0
for a in '123456':
    for b in '0123456':
        for c in '0123456':
            for d in '0123456':
                for e in '0123456':
                    Ch7=a+b+c+d+e
                    kolCh=0
                    SumCifr=0
                    
                    for cifr in Ch7:
                        

                        
                        if (int(cifr)%2)==0:
                            kolCh+=1
                        SumCifr+=int(cifr)
                   # print(Ch7,kolCh,SumCifr)
                   # iii=input()
                    if kolCh>=3:
                        prost=True
                        for D in range(2,SumCifr):
                            if SumCifr%D==0:
                                prost=False
                                break
                        if prost:
                            k+=1
print(k)                            
