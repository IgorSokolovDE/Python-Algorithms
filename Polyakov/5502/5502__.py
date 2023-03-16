##import turtle as t
##t.left(90)
##for i in range(15):
##    t.forward(150)
##    t.right(120)
k=0    
for x in range(1,15):
    yred=(-x/(3**0.5))+15
    yblue=x/(3**0.5)
    for y in range(16):
        if yblue <y <yred:
            k+=1
print(k)            
