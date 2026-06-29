array=(1,2,5,6,8)
large=(0)
for i in range(1, len(array)):
    if array [i]> large:
        large = array[i]
print(large)


# problem no 2
# check array is sort or not
arry=(1,2,3,5,6,9,8,)
num=("true")
for i in range(len(arry)-1):
    if arry [i]> arry[i+1]:
        num=False
        break
if num:
    print("sort")
else:
    print("not sort")    
print(sorted,(arry))