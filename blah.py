# Problem 1:
# Create two variables.
# One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.

# name = ("My name is ")
# name2 = ("LaVar Johnson")

# print(name + name2)


# Problem 2:
# Ask the user to enter the extra credit they earned.
# If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.

# userInput = int(input("Enter your extra credit"))
# if userInput < 5:
#     print("That's not enough extra Credit")
# elif userInput > 20:
#     print("That's too much extra credit")



# Problem 3:
# Ask a user to enter a password.
# Enter a password. Ask user to reenter password. Check to see if they are correct.

# userInput = input("Enter a password")
# userInput2 = input("Reenter your password")
# if userInput2 != userInput:
#     print("Wrong!")
# else:
#     print("Correct!")


# Problem 4:
# Ask for two card numbers.
# If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”

card1 = int(input("Enter a number"))
card2 = int(input("Enter another number"))
Sum = card1 + card2
if Sum == 21:
    print("BLACKJACK!")
elif Sum > 21:
    print("BUST!")
else:
    print ("The total is " )
