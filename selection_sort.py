def sort(num):
    
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if num[j] < num[minpos]:
                minpos = j
                
        temp = num[i]
        num[i] = num[minpos]
        num[minpos] = temp
    
num = [5,6,4,2,7,1]
sort(num)

print(num)

