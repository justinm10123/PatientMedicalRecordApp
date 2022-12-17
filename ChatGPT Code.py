import os
# Open the txt file in read mode
with open("G:/Georgetown Data/Discrete/Person.txt", 'r') as file:
  # Read the first line of the file (headers)
  headers = file.readline()
  # Print the headers
  #print(headers)

  # Ask the user for an input
  search_term = input("Enter a Patient ID #, First and Last name, or type Quit to Stop: ")
  split_search_term = search_term.split()

  # Read the rest of the lines in the file
  for line in file:
    # Split the line into a list of words
    words = line.split("|")
    # Check if the first word in the line matches the search term
    if words[0] == search_term:
      # If it does, print the entire line
      print(line)

      if search_term.lower() == "quit":
        break
      else:
        search_term = input("Enter another search term or Quit to Stop: ")

    elif words[2] == split_search_term[0] and words[5] == split_search_term[1]:
      print(line)

      if search_term.lower() == "quit":
        break
      
      else:
        search_term = input("Enter another search term or Quit to Stop: ")

        

  

  #just printing Patient ID, First Name, and Last Name
  #print(words[0],words[2],words[5])