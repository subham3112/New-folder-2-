lower = int(input("enter lower range"))
upper = int(input("enter upper range"))
for num in range(lower , upper + 1):
    if num >1:
        for i in range(2,num):
            if (num % i)==0:
                break
        else:
            print(num)

# program to check if a number is prime or not
num = int(input("input any number"))
if num>1:
    for i in range (2,num ):
        if num%i == 0:
            print(num, "is not a prime number ")
            break
        
    else  :
        print(num, "is a prime number")
else:
    print (num , "is not prime")