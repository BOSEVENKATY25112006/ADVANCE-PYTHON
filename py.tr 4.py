 #1
n = int(input("Enter a number: "))
if n > 0:
    print("The number is Positive")
elif n < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


#---------------------------------------------------------------------------------------------
#2
    
##n = int(input("Enter a number: "))
##if n % 2 == 0:
##    print("The number is Even")
##else:
##    print("The number is Odd")


#---------------------------------------------------------------------------------------------
#3

##a = int(input("Enter first number: "))
##b = int(input("Enter second number: "))
##if a > b:
##    print("First number is greater")
##elif b > a:
##    print("Second number is greater")
##else:
##    print("Both numbers are equal")


#----------------------------------------------------------------------------------------------
#4    
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#-----------------------------------------------------------------------------------------------
#5

for i in range(1, 11):
    print(i)

#-----------------------------------------------------------------------------------------------
#6

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

#-----------------------------------------------------------------------------------------------
#7

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum of first", n, "natural numbers is:", sum)