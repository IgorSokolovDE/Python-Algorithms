s='1'*33+'3'+'2'*33
while ('11' in s)or('22' in s)or('13' in s)or('23' in s):
    s=s.replace('11','2',1)
    s=s.replace('22','1',1)
    s=s.replace('13','2',1)
    s=s.replace('23','1',1)
Sum=0
for s1 in s:
    Sum+=int(s1)
print(Sum)
    
