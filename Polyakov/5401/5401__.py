s=open('24-222.txt').readline()
words=s.split('A')
words.pop(0)
kolPodOdinakov=0
MaxDlinaStr=0
for i in range(len(words)-1):
    if words[i]==words[i+1]:
        if kolPodOdinakov==0:
            kolPodOdinakov=2
        else:
            kolPodOdinakov+=1
    else:
       DlinaStr= kolPodOdinakov*len(words[i])+(kolPodOdinakov+1)
       MaxDlinaStr=max(MaxDlinaStr,DlinaStr)
       kolPodOdinakov=0
print(MaxDlinaStr)       
