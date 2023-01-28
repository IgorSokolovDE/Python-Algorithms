k=0
for a in '1234567':
    for b in '01234567':
        for c in '01234567':
            for d in '01234567':
                for e in '01234567':
                    for f in '01234567':
                        s8=a+b+c+d+e+f
                        Podchodit=True
                        for chCifrA in '0246':
                            for chCifrB in '0246':
                                for chCifrC in '0246':
                                    chCifrABC=chCifrA+chCifrB+chCifrC
                                    if chCifrABC in s8:
                                        Podchodit=False
                        if  Podchodit:
                            if max(int(a),int(b))< min(int(c),int(d),int(e),int(f)):
                                k+=1
print(k)
                            
                        
    
