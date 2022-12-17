def F(w1,w2):
    global k
    if (w1+w2)>88: return
    if (w1+w2)==88:
        k+=1
        return
    else:
        F(w1+w2,w2)
        F(w1,w2+w1)
k=0
F(1,1)
print(k)        
