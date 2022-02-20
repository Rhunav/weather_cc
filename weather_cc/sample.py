n=int(input())
string=input()
arr=[]
arr=string.split()
lst=[]
for i in arr:
    lst.append(int(i))
s=sum(lst)
if(sum%2==0):
    print(sum)
else:
    nm=999999
    for i in lst:
        if(i%2!=0):
            if(n<nm):
                nm=i
    print(sum-nm)

