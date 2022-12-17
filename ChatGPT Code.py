import os
# Open the txt file in read mode
with open("G:/Georgetown Data/Discrete/Person.txt", 'r') as file:
  # Read the first line of the file (headers)
  headers = file.readline()
  # Print the headers
  #print(headers)

  # Ask the user for an input
  search_term = input("Enter a Patient ID # or type Quit to Stop: ")

  # Read the rest of the lines in the file
  for line in file:
    # Split the line into a list of words
    words = line.split("|")
    # Check if the first word in the line matches the search term
    if words[0] == search_term:
      # If it does, print the entire line
      print(line)

      #just printing Patient ID, First Name, and Last Name
      print(words[0],words[2],words[5])

        #if statement to keep the input question running until they enter quit
      if search_term.lower() != "quit":
        search_term = input("Enter another search term or Quit to Stop: ")
