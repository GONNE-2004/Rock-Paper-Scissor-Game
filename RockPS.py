import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

chose = [ rock, paper, scissors]

user_choice= int(input("What do you choose? type 0 for rock, 1 for paper and 2 for scissors."))
#  Checking for user's invalidation before printing user's choice
if  user_choice < 0 or user_choice >= 3:
    print("You have entered an invalid choice. please choose again!")
else:
    print("You chose:")
    print(chose[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(chose[computer_choice])


if user_choice == computer_choice:
    print("It's a draw!")
# the below lines of code checks multiple conditions in which you win
# the backlash (\) to tell the compiler
# the line of code is a continuation of the upper one and
# has not ended unless i use this (\n) which means new line
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
# parentheses groups the conditions together, one can also avoid using backlash by grouping
# all the logic in 1, parentheses and dividing the logic by (or) and
# helps the compiler decided what's true or false before printing
else:
    print("Computer wins!")


# to avoid much writing of code we can use the modulo math trick
# result = (user_choice - computer_choice) % 3
# if result == 0:
#     print("It's a draw.")
# elif result == 1:
#     print("You win!")
# else:
#     print("Computer wins!")

# the module turn numbers in loop, real life analogy is the clock
# when it is 11 you add 2 it becomes 1 and not 13.
# this happens because the clock use 12hr looping which is modulo12

# (0-2)= -2 but we can't use -2 in the game so
# we use this: (0 - 2) % 3 = 1
# "If I’m 1 step ahead in the circle, I win. If I’m 2 steps behind, I lose."




