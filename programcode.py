# Calma, Eugene Marie S.
# BSCPE_1-4
# # OOP Laboratory Exercise Number 3 Problem 2 (LINE-OF-TEXT)

#Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
def write_to_file():
 # OPEN file 'mylife.txt' in write mode
  with open('mylife.txt', 'w') as file:
  # SET line equal to user input of a line of text
     line = input("Enter line: ")
  # WRITE line to file with newline character
     file.write(line + '\n')
  # SET line_choice equal to user input of 'y' or 'n'
     line_choice = input("Enter another line? (y/n): ")
  # WHILE line_choice.lower is equal to 'y'
  while line_choice.lower() == 'y':
    # SET line equal to user input of a line of text
      line = input("Enter line: ")
    # WRITE line to file with newline character
      file.write(line + '\n')
    # SET line_choice equal to user input of 'y' or 'n'
      line_choice = input("Enter another line? (y/n): ")
  # CLOSE file
  file.close()
  print("Writing to file complete")