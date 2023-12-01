import random
 
game_pic = ['''Rock:
    _______
---'   ____
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''Paper:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''Scissors:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
 
devam = "yes"
 
while devam.lower() == "yes":
    human_choice = int(input('''Rock, Paper, Scissors? "Rock" to choose "0", "Paper" to choose "1" and "Scirssors" to choose "2" press the number...\n'''))
 
    if 0 <= human_choice <= 2:
        print("Your choice...")
        print(game_pic[human_choice])
 
        computer_selection = random.randint(0, 2)
        print("Choosing a computer...")
        print(game_pic[computer_selection])
 
        if human_choice == 0 and computer_selection == 2:
            print("You Earned!")
        elif computer_selection == 0 and human_choice == 2:
            print("You Lost!")
        elif computer_selection > human_choice:
            print("You Lost!")
        elif human_choice > computer_selection:
            print("You Earned!")
        elif computer_selection == human_choice:
            print("You're Tied!")
    else:
        print("You have entered an invalid value...")
 
    devam = input("Would you like to play again? (yes/no): ")