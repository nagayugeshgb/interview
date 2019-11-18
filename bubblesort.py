n=int(input())
x=[int(x) for x in input().split()]
for i in range(0,n):
    for j in range(0,n-i-1):

        if(x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
for i in range(len(x)):
    print(x[i],end=" ")
