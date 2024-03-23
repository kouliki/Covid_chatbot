def symptoms():
    #fever,dry cough,tiredness
    count=0
    print("Do you have fever?\n")
    x=input("enter 1 if YES else any other key")
    if x=='1':
        count+=1

    print("Do you have dry cough?\n")
    x=input("enter 1 if YES else any other key")
    if x=='1':
        count+=1

    print("Do you have tiredness?\n")
    x=input("enter 1 if YES else any other key")
    if x=='1':
        count+=1
    
    if count==0:
        print("Chances of covid positive very low")
        print("get tested to be sure")
    
    elif count==1:
        print("chances of covid positive is low")
        print("get tested to be sure")

    elif count==2:
        print("Chances of being Covid positive is high")
        print("You must get tested")

    elif count==3:
        print("Chances of being Covid positive is very high")
        print("you must get tested")






def bookvaccine():
    print(" To book vaccine go to : https://www.cowin.gov.in/")




def helpline():
    print(""" Helpline numbers:
    Helpline: +91-11-23978046 (Toll Free - 1075 https://www.cowin.gov.in/)
    Technical Helpline: 0120-4783222
    CHILD : 1098
    MENTAL HEALTH : 08046110007
    SENIOR CITIZENS : 14567
    NCW : 7827170170""")




def safety():
    print(""" Safety Measures:
   1. Get vaccinated as soon as it’s your turn and follow local guidance on vaccination.
2. Keep physical distance of at least 1 metre from others, even if they don’t appear to be sick. Avoid crowds and close contact.
3. Wear a properly fitted mask when physical distancing is not possible and in poorly ventilated settings.
4. Clean your hands frequently with alcohol-based hand rub or soap and water.
5. Cover your mouth and nose with a bent elbow or tissue when you cough or sneeze. Dispose of used tissues immediately and clean hands regularly. 
6. If you develop symptoms or test positive for COVID-19, self-isolate until you recover.""")


print("Hello , Welcome my name is covi ")
print("Hpw may I help you today\n?")


while True:
    print(""" Please Enter:
    1. to check for symptoms
    2. to book vaccine
    3. to get a list of helpline numbers
    4. to get to know about safety measures\n""")

    choice=int(input("enter your choice:"))

    if choice==1:
        symptoms()
    elif choice==2:
        bookvaccine()
    elif choice==3:
        helpline()
    elif choice==4:
        safety()
    else:
        print("Invalid selection")

    print("""\n\n To start again enter 1 
    enter any other key to quit""")

    x=input("enter your choice:")
    if x!="1":
        break
    
