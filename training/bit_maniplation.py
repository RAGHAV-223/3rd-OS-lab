#wap to check if a given program is even or odd using bit manipulation
print("enter the number:",end="")
n=int(input())
if ((n ^ 1) == (n + 1)):
    print("even")
else:
    print("odd")