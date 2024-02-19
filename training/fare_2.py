print("Enter the units:",end="")
unit=int(input())
print("1.Industrial\n2.Instituional\n3.Domestic")
print("Area of connection")
area=int(input())
fare=(unit-5000)*0.25
fare1=(unit-10000)*0.23
if area==1:
    if unit<=5000 :
          print("FARE:Rs 1500")
    elif unit<=10000 :
          fare=((unit-5000)*0.25)
          print("Fare:Rs",1500+fare)
    elif unit<=20000 :
         new_fare=1500+5000*0.25+fare1
         print("fare: rs",new_fare)
    else :
         print("fare :rs",1500+10000*0.23+5000*0.25+(unit-20000)*0.20) 
                    