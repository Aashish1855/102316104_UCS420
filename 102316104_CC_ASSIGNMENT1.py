#Assignment-1.1
for i in range(3):
    print("Aashish Sharma")
#Assignment-2.1
a,b,c=3,4,5
print("The Sum is ",a+b+c)
#Assignment-2.2
a,b,c="a","b","c"
print("The concatenated string is=",a+b+c)
#Assignment-4.1
for i in range(1,11,1):
    print(7,"*",i,"=",7*i)
for i in range(1,11,1):
    print(9,"*",i,"=",9*i)
#Assignment-4.2
n=int(input("Enter a number="))
for i in range(1,11,1):
    print(n,"*",i,"=",n*i)
#Assignment-4.3
n=int(input("Enter a number="))
sum=0
for i in range(1,n,1):
    sum+=i
print("The Sum upto n=",sum)
#Assignment-5.1
a,b,c=map(int,input("Enter three numbers").split())
print("The maximum of",a,b,c,"=",max(a,b,c))
#Assignment-5.2
n=int(input("Enter a number="))
sum=0
for i in range(1,n,1):
    if(i%7==0 and i%9==0):
        sum+=i
print("The Sum of number divisible by 7 and 9 upto n=",sum)
#Assignment-5.3
n=int(input("Enter a number="))
sum=0
for i in range(1,n,1):
    isprime=True
    for j in range(1,i+1):
        if(i%j!=0):
            isprime=False
    if(isprime):
        sum+=i
print("The Sum of prime number upto n=",sum)
#Assignment-6.1
def add_odd_number(n):
    sum=0
    for i in range(n):
        if(i%2!=0):
            sum+=i
    return sum
#Assignment-6.2
def add_prime_number(n):
    sum=0
    for i in range(1,n,1):
        isprime=True
        for j in range(1,i+1):
            if(i%j!=0):
                isprime=False
        if(isprime):
            sum+=i
    return sum



