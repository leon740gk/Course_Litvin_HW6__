from random import randint
#1st
#temperature_c=int(input("Write a temperature in celsius: "))
#temperature_f=(temperature_c * 1.8)+32
#print(f"Temperature in fahrenheit is: {temperature_f}")

#2nd
#started_money=int(input("Type value of your deposit: "))
#percent=(int(input("Type percent of your deposit: ")))/100
#i=0
#while i<5:
#    started_money+=started_money*percent
#    i+=1
#print(started_money)
#3th
# while True:
#     month_number = int(input("Type month number,if you want to ext,enter 0: "))
#     if month_number==0:
#         break
#     elif month_number==1:
#         print(f"You typed {month_number},so it's January")
#     elif month_number==2:
#         print(f"You typed {month_number},so it's February")
#     elif month_number==3:
#         print(f"You typed {month_number},so it's March")
#     elif month_number==4:
#         print(f"You typed {month_number},so it's April ")
#     elif month_number==5:
#         print(f"You typed {month_number},so it's May")
#     elif month_number==6:
#         print(f"You typed {month_number},so it's June ")
#     elif month_number==7:
#         print(f"You typed {month_number},so it's July")
#     elif month_number==8:
#         print(f"You typed {month_number},so it's August ")
#     elif month_number==9:
#         print(f"You typed {month_number},so it's September")
#     elif month_number==10:
#         print(f"You typed {month_number},so it's October ")
#     elif month_number==11:
#         print(f"You typed {month_number},so it's November")
#     elif month_number==12:
#         print(f"You typed {month_number},so it's December ")
#
#     else:
#         print(f"Month with number {month_number} doesn't exist")

#4th

# first=int(input("Type first number: "))
# second=int(input("Type second number: "))
# if first-second>99:
#     print("yes")
# elif first-second<-99:
#     print("yes")
# elif first-second==0:
#     print("yes")
# else:
#     print("no")

#5th
# first=int(input("Type first number: "))
# second=int(input("Type second number: "))
# third=int(input("Type third number: "))
# fourth=int(input("Type fourth number: "))
# if first % 2==0 and first>second and first>third and first>fourth :
#     print(f"The bigger number is: {first}")
# elif second % 2==0 and second>first and second>third and second>fourth :
#     print(f"The bigger number is: {second}")
# elif third % 2==0 and third>first and third>second and third>fourth :
#     print(f"The bigger number is: {third}")
# elif fourth % 2==0 and fourth>first and fourth>second and fourth>third :
#     print(f"The bigger number is: {fourth}")
# else:
#     print("not found")

#6th

# a=int(input("Write 1st number: "))
# b=int(input("Write 2nd number: "))
# c=int(input("Write 3th number: "))
# if a==b:
#     print("yes")
# elif a==c:
#     print("yes")
# elif b == c:
#     print("yes")
# else:
#     print("no")

#7th
# random_number = randint(1, 100)
# i=0;
# while i<3:
#     inpt=int(input("Guess the number(you have 3 chances :"))
#     if inpt==random_number:
#         print("You are right!")
#         break
#     else:
#         print("You are wrong")
#         if inpt>random_number:
#             print(f"Your number is {inpt},and it's bigger than secret's number")
#         else:
#             print(f"Your number is {inpt},and it's smaller than secret's number")
#     i+=1
# print(f"{random_number} was a secret number")
