# problem no 1
# find largest number

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


# problem 3
# find the 2nd large number
ary=(1,5,8,6,3,)
sot=(sorted(ary))
print(sorted(ary)),print("to show the array is sorted")
print(sot[len(sot)-2])


# problem no 4
# linear search
ary=[1,2,5,9,8,7,6]
target=9
for i in range(len(ary)):
    if ary[i]==target:
     print("target match",i,ary)
     
     
     break



# problem no 5
# Left Rotate Array by One
ary=[1,2,3,4,5,6]
frist=ary.pop(0)
print(ary.append(frist))
print(ary)





# easy array
# problem no 1
# Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

ary = [1,0,1,1,1,1,0,1]

con = 0
max_con = 0

for i in range(len(ary)):
    if ary[i] == 1:
        con = con + 1
        if con > max_con:
            max_con = con
    else:
        con = 0

print(max_con)



# problem no 2
# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
arr = [1, 0, 2, 0, 4, 3, 0, 5]

j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)