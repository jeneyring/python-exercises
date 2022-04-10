#Conditional Basics:_____________________________________________________________________________________
#1
## a) Prompt the user for a day of the week, print out whether the day is Monday or not

happy_monday = 'Monday'
user_input = input('What day of the week is it?: ')

while user_input != happy_monday:
    print('Dang, wish it was Monday...')
    user_input = input('Monday' or 'monday')

print('YES! Thank God it is Monday!')



## b) prompt the user for a day of the week, print out whether the day is a weekday or a weekend

weekday = ['Monday', 'Tuesday','Wednesday','Thursday','Friday']
weekend = ['Saturday', 'Sunday']
user_input = input('What day of the week is it?: ') 
    
while user_input in weekday:
    print('Dang, another work day...')
    break
else:
    print('Yay! The weekend is here!')


## c)create variables and make up values for:
#--the number of hours worked in one week
#--the hourly rate
#--how much the week's paycheck will be
#--write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours

hours = input("Enter number of hours worked\n")
hours = int(hours)
rate = input("Enter pay rate per hour\n")
rate = int(rate)

if int(hours)> 40:
    print('Overtime pay is:', (rate * 1.5) + (hours * rate))
else:
    print("Weekly pay is:", hours * rate)


#2) LOOP exercises______________________________________________________________________________

###Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5

while i <= 15:
    print(i)
    i = i + 1


###Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.
i = 2

while i in range(1,101):
        print(i)
        i = i * 2



###Alter your loop to count backwards by 5's from 100 to -10.
i = 100

while i >= -10:
    print(i)
    i = i - 5


###Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000. 
i = 2

while i <= 1000000:
    print(i)
    i = i **2



###Write a loop that uses print to create the output shown below.
i = 100

while i >= 5:
    print(i)
    i = i - 5

### 2: b) Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

num = int(input("Choose a number:  "))
i = 1

while i<=10:
    print(num, "X", i, "=", num * i)
    i = i+1

### Create a for loop that uses print to create the output shown below:
n = int(9)

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()


##Prompt the user for an odd number between 1 and 50 (X)
#  Use a loop and a break statement to continue prompting the user
#  if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this).

#NOT FINISHED////////
num = int(input("Choose an odd number from 1-50:  "))
i = 1

while i<=50:
    if num %2 == 0:
        print((input("Try again: ")))
        break
    
    else: 
        print("Here is an odd number:", i)
    i = i+2 

#  Use a loop and the continue statement to output all the 
# odd numbers between 1 and 50, except for the number the user entered.


#NOT FINISHED///////////
num = int(input("Choose an odd number from 1-50:  "))
i = 1

while i<=50:
    if num %2 == 0:
        print((input("Try again: ")))
        break
    
    else: 
        print("Here is an odd number:", i)
    i = i+2 

    

