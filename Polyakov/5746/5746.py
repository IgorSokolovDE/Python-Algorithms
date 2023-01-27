k=0
for a in '1234':
    for b in '01234':
        for c in '01234':
            for d in '01234':
                for e in '01234':
                    Ch5=a+b+c+d+e
                    if abs(int(a)-int(b))>=2:
                        if abs(int(e)-int(d))>=2:
                            if (abs(int(b)-int(c))>=2):
                                if (abs(int(d)-int(c))>=2):
                                    k+=1
print(k)                            
                    
