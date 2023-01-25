for n2 in range(0,10000000000):
    for x in range(0,2**(n2+10)):
        y=bin(x)[2:]
        y='0'*(n2+10-len(y))+y
        if y.count('1')==10:
            y=y.replace('0','2')
            while '21' in y:
                y=y.replace('21','6',1)
            sumCifr=0
            for s1 in y:
                sumCifr+=int(s1)
            if sumCifr==50:
                print(n2)
                ii=input()
            
    
