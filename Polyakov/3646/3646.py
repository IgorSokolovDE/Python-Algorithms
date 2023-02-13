print('x y z w')
for x in (0,1):    
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                if (((x<=y)or(not(z<=w))and((w<=(not(x)))or((not(y))<=z))))==False:
                    print(x,y,z,w)
                
    
