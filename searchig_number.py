import array
arr=array.array('i',[1,2,3,4,5])
a=int(input("enter value"))
c=0
for i in range(len(arr)):
    if (a==arr[i]):
        print(i)
        c+=1
        break
if(c==0):
    print(-1)