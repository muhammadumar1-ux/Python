position = -1

def search(list,n):
    l = 0
    u = len(list) - 1
    
    while (l <= u):
        mid = (u + l) // 2
    
        if list[mid] == n:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
            

list = [2,4,5,8,45,67,90,99]
n = 67

if search(list,n):
        print("Found at ",position)
else:
        print("Not found")