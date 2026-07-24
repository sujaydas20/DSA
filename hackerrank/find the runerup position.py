# for my logic


num = [6, 5, 4, 3, 2, 1]

def sort(num):
    return sorted(num)

print(sort(num))
print(len(num) - 1)



# as need for hackerrank 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = list(set(arr))   
    arr.sort()            
    print(arr[-2])         