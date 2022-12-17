import os
# Open the txt file in read mode
with open("G:/Georgetown Data/Discrete/Person.txt", 'r') as file:
  # Read the first line of the file (headers)
  headers = file.readline()
  # Print the headers
  #print(headers)

  # Read the rest of the lines in the file
  for line in file:
    # Split the line into a list of words
    words = line.split("|")

    #asking for user input
    search_term = input("Enter a Patient ID #, First and Last name, or type Quit to Stop: ")
    split_search_term = search_term.split()


    # Check if the first word in the line matches the search term
    if words[0].lower() == search_term.lower() or (words[2].lower() == split_search_term[0].lower() and words[5].lower() == split_search_term[1].lower()):
      # If it does, print the entire line
      print(line)

    #if user input is quit is breaks the loop
    if search_term.lower() == "quit":
      break

    ############## need to figure out why it does not print line when first and last name are entered ###################
        

  

  #just printing Patient ID, First Name, and Last Name
  #print(words[0],words[2],words[5])