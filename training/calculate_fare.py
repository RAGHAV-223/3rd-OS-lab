print("enter the distance travelled:",end="")
distance=float(input())
print("Travel Fares".upper())
if distance<=50 :
    charges=distance*8
    print("charges: Rs 8/km")
    print("Total cost:",charges)
elif distance<=100 and distance>50:
    charges=distance*6
    print("charges :Rs 6/km")
    print("Total cost:",charges)
elif distance>100 :
    charges=distance*5
    print("charges : Rs5/km")
    print("Total cost:",charges)    
print("****thank you for using travel. services***".upper())    

