# Calma, Eugene Marie S.
# BSCPE_1-4
# # OOP Laboratory Exercise Number 3 Problem 2 (LINE-OF-TEXT)

#Write a method in python to write multiple line of text contents into a text file mylife.txt.
def process():
        # open mylife.txt(append)
    with open("mylife.txt","a") as input_file:
        user_input= input("Good day! Please type your line of text!")
        #ask the user to try and input once again
        askyesno = input("\n\33[36mDo you still want to continue? (yes/no):\33[0m ")
        if askyesno.lower() == 'yes':
            user_input=input("Please type your new line of text")
        else: 
            askyesno.lower() == 'no'
            print("\33[41mTerminating Program... Your text is generated, feel free to open it at mylife.txt. Have a good day!")
            exit()
            # encode the user input to the txt file
        input_file.write(user_input + "\n")
process()
        
