f=open('26-76.txt')
L,N=map(int, f.readline().split())
DelaemDetali=[]
for i in  range(N):
    start,final=map(int, f.readline().split())
    DelaemDetali.append([start,final])
DelaemDetali.sort()
Prostoi=DelaemDetali[0][0]
MaxProstoi=0
for i in range(N-1):
    Prostoi+=DelaemDetali[i+1][0]-DelaemDetali[i][1]
    MaxProstoi=max(MaxProstoi,(DelaemDetali[i+1][0]-DelaemDetali[i][1]))
Prostoi+=L-DelaemDetali[N-1][1]
MaxProstoi=max(MaxProstoi,(L-DelaemDetali[N-1][1]))
print( Prostoi, MaxProstoi)  

