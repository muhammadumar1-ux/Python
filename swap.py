a = 5
b = 6

temp = a
a = b 
b = temp

a = a ^ b
b = a ^ b 
a = a ^ b

a,b = b,a 

print(a)
print(b) 