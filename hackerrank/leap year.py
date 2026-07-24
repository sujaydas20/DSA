# as per my logic the code

a = 4
b = 100
d = 400

c = int(input("enter your year="))

if c % d == 0:
    print("year is a leap year")
elif c % b == 0:
    print("year is not a leap year")
elif c % a == 0:
    print("year is a leap year")
else:
    print("year is not a leap year")

# as per hackerrank need code
def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))