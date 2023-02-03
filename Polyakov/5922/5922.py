F4500=0
for n in range(4500,10001,2):
    if n<10000:
        F4500+=n%10
    else:
        print(F4500,n)
        F4500+=1
F5515=0
for n in range(5515,10,-2):
    if n >10:
        F5515+=(n-1)%10
    else:
        print(F5515,n)
        F5515+=n
print(F4500, F5515,n)      
        
