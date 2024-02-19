#wap to odd numbers from 1 to 100
'''num=int(input("enter the number:"))
x=0
while n>0:
    r=num%10
    sum=sum+r
    num=num//10
print(sum)'''
#wap to reverse the number and print
'''num=int(input("enter the number:"))
x=0
p=1
while num>0:
    r=num%10
    x=x+r
    p=p*r
    num=num//10
print(x)
print(p)
if x==p:
    print("\nNumber is spy")
else:
    print("\nNumber is not spy")
#WAP TO FIND factorial of the number
num=int(input("enter the number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1
print ("factorial:",fact)
#wap to input number and find the number is prime ior not
num=int(input("enter a number:"))
i=1
count=0
while i<=num:
    r=num%i
    if r==0:
        count+=1
    i+=1
    print(r,end=',')
if count==2:
    print("%d number is prine"%num)
else:
    print("%d number is not prime"%num)
#wap to print palindrome numbers from 1 to 100
i=1
while i<100:
    n=i
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==i:
        print('%d is palindrome'%i,end=' , ')
    i+=1
#wap to print armstrong number
i=1
while i<1000:
    n=i
    s=0
    while n>0:
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if s==i:
        print('%d is armstrong'%i)
    i+=1
for r in range(5,0,-1):
    for c in range(1,r+1):
        print(c,end=' ')
    
    print()
for r in range(5,0,-1):
    for c in range(1,r+1):  
        print('*',end=' ')
    
    print()
#wap to print the summation of the series
# x+(x+1)^1+(x+2)^2....nterms
x=int(input("enter the number:"))
n=int(input("enter the number:"))
series_sum=x
for i in range(1,n+1):
    series_sum+=(x+i)**i
print("sum of series:",series_sum)
#wap to print the summation of series 
# x+(x+1)^2+(x+2)^3+...nterms
x=int(input("enter the number:"))
n=int(input("enter the number:"))
series_sum=0
for i in range(n):
    series_sum+=((x+i)**(i+1))
print("sum of series:",series_sum)
#wap to check if given pair is amicable pairs
x=int(input("enter the number:"))
n=int(input("enter the number:"))
sumfactor_x=0
sumfactor_n=0
for i in range(1,(x//2)+1):
    if x%i==0:
        sumfactor_x+=i
for i in range(1,(n//2)+1):
    if n%i==0:
        sumfactor_n+=i
if sumfactor_x==n and sumfactor_n==x:
    print("pair is amicable")
else:
    print("pair is not amicable")
#wap to print sum of only prime numbers in a given number
n=int(input("enter the number :"))
sum_prime=0
while n:
    r=n%10
    for i in range(2,r):
        if r%i==0:
            break
    else:
        sum_prime+=r
    n=n//10
print("sum of prime digits :",sum_prime)'''
l1=[10,20,23,345,35,45,353.453,352,53,5,35,75,4]
print(l1[::-1])
print(l1[10:11:])
print(l1[2:])
print(l1.append(23))


