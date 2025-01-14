n=10
li=[]
for i in range(n):
    a=list(map(int,input().split()))
    li.append(a)
max_li=[]
min_li=[]
avg_li=[]
print(li)
for i in range(4):
    max=0
    min=100
    avg=0
    for j in range(n):
        if(li[j][i]>=max):
            max=li[j][i]
        if(li[j][i]<=min):
            min=li[j][i]
        avg+=li[j][i]
    max_li.append(max)
    min_li.append(min)
    avg_li.append(avg/10)



    
