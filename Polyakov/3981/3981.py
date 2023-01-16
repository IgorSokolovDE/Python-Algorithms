N=[]
for m in range(0,40,2):
    for n in range(1,40,2):
        if 100_000_000 <=((2**m)*(7**n))<= 300_000_000:
            N.append([((2**m)*(7**n)),m+n])
N.sort()
print(N)
