# Calma, Eugene Marie S.
# BSCPE_1-4
# # OOP Laboratory Exercise Number 3 Problem 2 (LINE-OF-TEXT)

#Write a method in python to write multiple line of text contents into a text file mylife.txt.
def process():
        # open numbers.txt (read), double txt even.txt (append), triple odd.txt (append)
    with open("mylife.txt","a") as input_file:
        user_input= input("Good day! Please type your line of text!")
        # encode the user input to the txt file
        input_file.write(user_input + "\n")

process()
        
