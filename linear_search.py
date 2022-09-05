from tkinter import N


position = -1

def search(list,n):
    
    for i in range(0,5):
        if list[i] == n:
            globals()['position'] = i
            return True
    return False
    
    
    
list = [1,9,7,5,8,6]
n = 1
if search(list,n):
    print("Found at",position)
else:
    print("Not Found")