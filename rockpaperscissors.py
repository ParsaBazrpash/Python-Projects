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

game_images = [rock,paper,scissors]

x = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))
print("Your chose:")
print(game_images[x])


comp = random.randint(0,2)
print("Computer Chose:")
print(game_images[comp])

if x == 0 and comp ==2:
    print("You Win!")
elif x >= 3 or x < 0:
    print("You tried an invalid number, you lose!")
elif comp == 0 and x==2:
    print("You lose!")
elif x > comp:
    print("You win")
elif comp > x:
    print("You lose!")
elif comp == x:
    print("It's a draw")



