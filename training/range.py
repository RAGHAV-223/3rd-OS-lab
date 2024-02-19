#wap to find that if kth bit is set or unset
'''n=int(input("enter a number:"))
k=int(input("enter the bit to set:"))
x=1
x=x<<(k-1)
if x & n:
    print("bit is set",n)
else:
    print("bit is unset",n)
'''
#wap to set the kth given bit of a number
'''n=int(input("enter the number:"))
k=int(input("enter the bit to set:"))
x=1
x=x<<(k-1)
i=x|n    
print(i)'''
#wap to toggle the kth bit of given number 
'''n=int(input("enter the number:"))
k=int(input("enter the bit to set:"))
x=1
x=x<<(k-1)
i=x^n
print("after toggle:" ,i)'''
#wap to find the count of set bits of a given number
'''n=int(input("enter a number:"))
c=0
while n!=0:
    if n&1:
        c+=1
    n=n>>1
print(c)
#wap to check number is power of 2
n=int(input("enter the integer:"))
if n& (n-1)==0:
    print("%d number is power of 2"%n)
else:
    print("%d number is no power of 2"%n)

#wap to find number is negative or positive
n=int(input("enter the number:"))
n=n>>32
if n&1:
    print("number is negative")
else:
    print('number is positive')
#wap to find given number is perfect or not and print all number between 1 to 100
n=int(input("enter the number:"))
sum_factors=0
for i in range(1,n):
    if n%i==0:
        sum_factors+=i
if sum_factors==n:
    print('number is perfect')
else:
    print('number is not perfect')'''
#wap to find the summation of given series
#x+(X+1)^1+(x+2)^2+(x+3)^3...nterms






