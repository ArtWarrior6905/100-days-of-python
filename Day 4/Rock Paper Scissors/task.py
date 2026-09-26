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
a = int(input("To pick rock type '0', paper type '1', scissors type '2':\n "))
print("You chose: ",a)
if a == 0:
    print(rock)
elif a == 1:
    print(paper)
elif a == 2:
    print(scissors)
b = [rock,paper,scissors]
c=random.choice(b)
print("Computer chose: ",c)
if (a == 0 and c == scissors) or (a == 1 and c == rock) or (a == 2 and c == paper):
    print("You win!")
elif (a == 0 and c == paper) or (a == 1 and c == scissors) or (a == 2 and c == rock):
    print("You lose!")
else:
    print("It's a Draw")