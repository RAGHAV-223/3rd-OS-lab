#wap to create a dynamic list by taking the list from use
'''ln=int(input("enter the number of elements:"))
arr=[]
for i in range(ln):
    ele=input("enter %d element:"%i)
    arr.append(ele)
print(arr)
#wap to find the elements in the list that are prime
ln=int(input("enter the number of elements:"))
arr=[]
for i in range(ln):
    ele=int(input("enter %d element:"%i))
    arr.append(ele)
for i in arr:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("prime elements are:",i)
def calc(na,id,m_c,m_java,m_py):
    total=m_c+m_java+m_py
    per=(total/300)*100
    print(id,na,m_c,m_java,m_py)
if __name__=='__main__':
    studid,name=input("enter the student id and name:")
    py,java,c=int(input("enter the marks in python, java and c:"))
arr=[]
for i in  range(5):
    arr.append(input())
print(arr)
arr=list(map(int,arr))
print(arr)
#wap to find the elements in the list where sum of digits of elements id odd
listt=list(map(int,input("enter number:").split()))
for i in listt:
    sum=0
    temp=i
    while i:
        rem=i%10
        sum+=rem
        i=i//10
    if sum%2!=0:
        print(temp,sum)
#wap to find the missing number in a given cosecutive array
#[23,24,25,26,28,29]
listt=list(map(int,input().split()))
for ele in range(len(listt)-1):
    if listt[ele+1]-listt[ele]==1:
        continue
    else:
        num=listt[ele]+1
        print(num)
strr="model"
print(strr[-3:0:-1])
print(help(slice))
#wap to reverse every words of a given sentence
strr="miet students are learning python"
lst=strr.split()
reverse=[]
print(strr)
for i in lst:
    reverse.append(i[::-1])
print(" ".join(reverse))'''
#wao to sort givens tring where alphabets should come first and then 
#digits and then special character either ascending and descending
'''s=input()
sorted(s)
digit=alpha=spe=""
for i in sorted(s):
    if i.isdigit():
        digit+=i
    elif i.isalpha():
        alpha+=i
    else:
        spe+=i
print(alpha+digit+spe)
#wap to make the minion game
strr=input()
vowels = 'aeiou'
player1_score = 0
player2_score = 0
for i in range(len(strr)):
    if strr[i] in vowels:
        player1_score += len(strr) - i
    else:
        player2_score += len(strr) - i
print("----WINNER-----")
if player1_score > player2_score:
    print("player1", player1_score)
elif player2_score > player1_score:
    print("player2", player2_score)
else:
    print("Draw")'''
#wap to asdfjkl;asdfjkl;asdfjkl;asdfjkl;asasdfjkl;asdfjkl;tree asdfjkl;jklasdfkite kite kite kite kite kite tree kite kite kite tree tree tree tree tree tree bubble bubble bubble bubble bubbel bubble bubble bubble bubble bubble random random random random random random random random random duplicate cannot degine an empty set 8
       

    





