import array
arr=array.array('i',[44,55,55,43])
is_pall=True
for i in range(len(arr)//2):
    if(arr[i]!=arr[len(arr)-1-i]):
       is_pall=False
       break
if is_pall:
   print("yup")
else:
   print("nop")