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


#NOT FINISHED///////////(need to figure out the except part)
num = int(input("Choose an odd number from 1-50:  "))
i = 1

while i<=50:
    if num %2 == 0:
        print((input("Try again: ")))
        break
    
    else: 
        print("Here is an odd number:", i)
    i = i+2  


##Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, 
##also note that the input function returns a string, so you'll need to convert this to a numeric type.) 
i = 1
user_input = int(input("Choose a positive number: "))
n = user_input
while True:
    for i in range (0, user_input):
        print(i)
    i = i + 1
    if i == i:
        print(user_input)
        break

##Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.

i = 1
user_input = int(input("Choose a positive number: "))
n = user_input
while True:
    print(user_input)
    for i in reversed(range(0, user_input)):
        print(i)
    i = i - 1
    if i == i:
        break



#3) FIZZBIZZ::::
#Write a program that prints the numbers from 1 to 100.
i = 1
for i in range(1,101):
    print(i)
    i=i+1

#For multiples of three print "Fizz" instead of the number
i = 1 
for i in range(50):
    if i % 3 ==0:
        print('Fizz')
    else:
        print(i)
        i=i+1

#For muliples of five print "Buzz"
i = 1 
for i in range(51):
    if i % 5 ==0:
        print('Buzz')
    else:
        print(i)
        i=i+1

#For numbers which are multiples of both three and five print "FizzBuzz".
i = 1 
for i in range(51):
    if i % 5 ==0 and i % 3 ==0:
        print('FizzBuzz')
    else:
        print(i)
        i=i+1

#4) TABLES::::
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
##Ask if the user wants to continue.
#Assume that the user will enter valid data.
##Only continue if the user agrees to.

number = 0
square = 0
cube = 0

user_input=int(input("What number do you want to go up to?  "))
# print the header
print('number\tsquare\tcube')
# \t creates the spacing between titles

for number in range(0, 20):
    square = number * number
    cube = number * number * number
    
    # print the rows using f-strings
    print(f'{number}\t{square}\t{cube}')
    
    if number == user_input:
        break


#