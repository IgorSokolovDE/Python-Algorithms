A=[]
for x in range(1,10**6+1):
    s=str(x)
    stepen=len(s)
    SumCifrStep=0

    for s1 in s:
        SumCifrStep+=int(s1)**stepen
    if SumCifrStep==x:
        A.append(x)
SS=open('24-234.txt').readline()        
for i in range(len(A)-1,-1,-1):
    kolPov=SS.count(str(A[i]))
    if kolPov>0:
        print(kolPov)
        break
        
