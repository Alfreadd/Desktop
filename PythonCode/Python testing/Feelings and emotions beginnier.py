"""
This is a program designed to genarate a qutoe based on the emotional state inputted of the user.
"""
# This is the feelings menu template for the resources.
#
# https://drive.google.com/drive/folders/1tD1FfW9UpQc-_9hjIiFpSaZiscEaCtbv
#

# Output a welcome message.
print()
print("###########################")
print("##           ##          ##")
print("##  Welcome  ## Stranger ##")
print("##           ##          ##")
print("###########################")

run_feelings = True

# Starting the loop.
while run_feelings: 
 print()           
 print("You can choose from the following list of feelings. Which one best matches your mood right now?")
 print()
 # Output a feeling
 print("===============================")
 print("A: I Feel a bit worried.")
 print("===============================")
 print("B: I'm feel Anxious")
 print("===============================")
 print("C: I'm feeling confused")
 print("===============================")
 print("D: I'm feeling Scared")
 print("===============================")
 print("E: I'm feeling Happy")
 print("===============================")
 print("To quit Press Q")
 print("===============================")
 print()

 # Output instructions
 print("Enter the letter that corresponds the most closely to how you feel.")
 
 # Creates a variable called feeling that stores the users input.
 # Notice the space. It's important.
 feeling = input("Choose a feeling from the options (A,B,C,D,E): ")
 print("-------------------------------------------------------------------------------------------")
 
 # Process the user input.
 if feeling == "A":
    print()
    print('###########################################################################################')
    print("You can destroy your now, by worrying about tomorrow.")
    print()
    print("Janis Joplin")
    print('###########################################################################################')
    print()
 if feeling == "B":
    print()
    print('###########################################################################################')
    print("Trust, You've survived a lot and will survive whatevers coming.")
    print()
    print("Jospeh Svens")
    print('###########################################################################################')
    print()
 if feeling == "C":
    print()
    print('###########################################################################################')
    print("“It’s pretty confusing. Good. Be confused. Confusion is where inspiration comes from.")
    print()
    print("Robyn Mundell, Brainwalker")
    print('###########################################################################################')
    print()
 if feeling == "D":
    print()
    print('###########################################################################################')
    print("“Don't be afraid of being scared. To be afraid is a sign of common sense. Only complete idiots are not afraid of anything.”")
    print()
    print("Carlos Ruiz Zafón, The Angel's Game")
    print('###########################################################################################')
    print()
 if feeling == "E":
    print()
    print('###########################################################################################')
    print("Being Happy Doesnt mean that everything is perfect, It means you have decided to look beyond the imperfections.")
    print()
    print("Boom Sumo")
    print('###########################################################################################')
    print()

 elif feeling == "Q":
        print("OK, it was fun while it lasted.")

        # Stop the loop
        run_feelings = False
else:
        print("I don't understand.")

# to add more feelings.
# Use
# else:
# to catch errors.
# Remember to space in the parts after the elif and the else.