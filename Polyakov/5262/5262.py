s=open('24-210.txt').readline()
troiki=["ABC","BAC","CAB","CBA"]
MaxK3=0
for start in range(len(s)-2):
    podS=s[start:start+3]
    if podS in troiki:
        i=start
        k3=0
        while i<(len(s)-2):
            podS=s[i:i+3]
            if not(podS in troiki):
                break
            else:
                k3+=1
                i+=2
                MaxK3=max(MaxK3,k3)
print(MaxK3)                
    
