#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator")
total_bill=input("Enter the total amount? - ")
no_people=input("enter the total number of people - ")
percentage=input("enter how much percentage would you like to give as a tip? ")
total_bill=int(total_bill)
no_people=int(no_people)
each_share=total_bill/no_people
total_tip=(total_bill)*12/100
each_tip=total_tip/5
one_share=each_share+each_tip
one_share=("{:.2f}".format(one_share))
print(f"Each share will be {one_share}")



