print('x y z w')
for x in (0,1):
    for y in (0,1):

        for z in (0,1):
            for w in (0,1):
                if(((z<=y)and((not(x))<=w))<=((z== w)or(y and(not(x)))))==False:
                    print(x,y,z,w)
    