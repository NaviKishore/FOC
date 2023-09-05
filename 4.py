def birthdayCakeCandles(l):
    g=0
    for i in range(len(l)):
        
            if(l[i]>g):
                g=l[i]
    c=0

    for i in range(len(l)):
        if(l[i]==g):
            c+=1
    print(c)
l=list(map(int,input().split()))
birthdayCakeCandles(l)
        
