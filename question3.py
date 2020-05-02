a = int(input("enter a number for a"))
count = 0
r = 0
if a == 0 :
    count = 1
else :
    while a!=0:
        r = a % 10
        count = count + 1
        a = a//10
    
        
    
print ("no. of digits = ",count)
