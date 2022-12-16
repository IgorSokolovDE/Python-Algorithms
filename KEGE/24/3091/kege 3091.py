f=open('24_.txt')
KStr=0
while True:
    s=f.readline()
    if not(s):
        break
    if len(s)>=7:
        palindrom=False
        
        for i in range(len(s)-7):
            podS=s[i:i+7]
            
            
            if podS==podS[::-1]:
                palindrom=True
                break
            else:
                A=[]
                for j in range(7): A.append(podS[j])
                for j in range(6):
                    for k in range(j+1,7):
                        B=A[:]
                        el=B[j]
                        B[j]=B[k]
                        B[k]=el
                        if B==B[::-1]:
                            palindrom=True
                            
                            break
                    if palindrom: break
            if palindrom: break
    if palindrom: KStr+=1      
print(KStr)                    
                        
