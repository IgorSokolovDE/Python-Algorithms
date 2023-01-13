f=open('26-j6.txt')
N=int(f.readline())
files=[int(x) for x in f]
Arhiv=sum(files)*0.9
files.sort()
files=files[::-1]
KolArh=0
SumF=sum(files)
i=0
while SumF>Arhiv:
   SumF-=files[i]*0.2
   KolArh+=1
   i+=1
print(N-KolArh,files[i])   
