#Question-1
print("Question 1")
ls=[10,20,30,40,50,60,70,80]
print("The Starting list:-",ls)
ls.append(200)
ls.append(300)
print("The List after adding 200,300:-",ls)
ls.remove(10)
ls.remove(30)
print("The list after removing 10,30:-",ls)
ls.sort(reverse=False)
print("Sorted list:-",ls)
ls.sort(reverse=True)
print("Sorted list in reversed order:-",ls)

#Question-2
print("Question 2:-")
tu=(45,89.5,76,45.4,89,92,58,45)
print("Highest marks:-",max(tu),"at index",tu.index(max(tu)))
print("Lowest marks is:-",min(tu)," and it appeared",tu.count(min(tu)))
ls_q2=list(tu[::-1])
print("Reversed tuple into a list",ls_q2)
x=int(input("Enter a number="))
if(tu.count(x)>0):
    print(tu.index(x))
else:
    print("Not found")

#Question-3
print("Question 3")
from random import randint as rd
ls_q3=[]
for i in range(100):
    ls_q3.append(rd(100,900))
print("Even Number=")
for i in ls_q3:
    if(i%2==0):
        print(i,end=",")
print("\nOdd Number=")
for i in ls_q3:
    if(i%2!=0):
        print(i,end=",")
print("\nPrime Number=")
isPrime=False
for i in ls_q3:
    isPrime=True
    for j in range(2,i):
        if(i%j==0):
            isPrime=False
    if(isPrime):
        print(i,end=",")
print("\n")

#Question-4
print("Question 4=")
a={34,56,78,90}
b={78,45,90,23}
print("The union of a and b",a.union(b))
print("The intersection of a and b",a.intersection(b))
print("The differance b/w and b",a.difference(b))
print("if a is subset of b",a.issubset(b))
x=int(input("Enter Score to search="))
try:
    a.remove(x)
except:
    print("Not found")
print("The list after removing",x,"is",a)

#Question-5
sample_dict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}
sample_dict.update({"location":"New york"})
sample_dict.pop("city")
print(sample_dict)
    
