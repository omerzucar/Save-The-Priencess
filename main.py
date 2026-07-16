print("Welcome to the Save the Princess")
print("Your mission is to find the princess and save them.")

choice1 = input("You went to the castle. "
                 "Then you see 3 doors.\n"
                 "One red door, one blue door and one yellow door.\n"
                 "You have to select just one. "
                 "Type 'red door', 'blue door' or 'yellow door': ")

if choice1 == "red door":
    choice_item = input("You didn't die. Now, you see 3 materials. "
                         "Type 'Sword', 'Armor' or 'Shield': ")
    if choice_item == "Sword":
        print("You picked the Sword. It's the real one, you are safe! You keep going the way.")
    elif choice_item == "Armor":
        print("You picked the Armor. The Armor was cursed! You died.")
        exit()
    elif choice_item == "Shield":
        print("You picked the Shield. The Shield was cursed! You died.")
        exit()
    else:
        print("Invalid choice. You got confused and died.")
        exit()
else:
    print("Invalid choice. You got confused and died.")
    exit()

choice2 = input("Okay, it remains a bit of the way.\n"
                 "Now, you have to select a partner to save the princess.\n"
                 "Which one will you select? 'Iron Man', 'Superman' or 'Spiderman': ")

if choice2 == "Spiderman":
    print("It's the best choice. Spiderman isn't affected by any bad things and he will help you all the way.")
elif choice2 == "Superman":
    print("You won't succeed in the mission because Superman was affected by Green Kryptonite, which affects him badly.")
    exit()
elif choice2 == "Iron Man":
    print("You won't succeed in the mission because Iron Man was affected by a magnetic field and died.")
    exit()
else:
    print("Invalid choice. Something went wrong.")
    exit()

choice4 = input("Finally, you've reached the last part.\n"
                 "You see a monster and you have to fight the monster.\n"
                 "However, first you take a pill: 'red' or 'blue'. Which one will you select? ")

if choice4 == "red":
    print("You've got ultimate power, speed and laser eyes.\n"
          "It's a big deal. You can kill the monster with Spiderman.\n"
          "Then you will kill the monster and save the princess.\n"
          "Congratulations, you win! And the princess kissed you :)")
else:
    print("You've got nothing, so the monster will kill you. You couldn't save the princess.")