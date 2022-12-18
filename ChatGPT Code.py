import os
# Open the txt file in read mode
with open("G:/Georgetown Data/Discrete/Person.txt", 'r') as person_file, open("G:/Georgetown Data/Discrete/Patient.txt", "r") as patient_file:
  # Read the first line of the file (headers)
  headers = person_file.readline()
  # Print the headers
  #print(headers)

  # Read the rest of the lines in the file
  for line in person_file:
    # Split the line into a list of words
    words = line.split("|")

    #asking for user input
    ###################### Will be changing from an input question to a tkinter text box ########################
    search_term = input("Enter a Patient ID #, First and Last name, or type Quit to Stop: ")
    split_search_term = search_term.split()


    # Check if the first word in the line matches the search term
    if (words[0].lower() == search_term.lower()): #or (words[2].lower() == split_search_term[0].lower() and words[5].lower() == split_search_term[1].lower()):
      # If it does, print the entire line
      print(line)

      for line_1 in patient_file:
        words_1 = line.split("|")

        if words_1[0] == words[0]:
          print(line_1)

      
    #if user input is quit is breaks the loop
    elif search_term.lower() == "quit":
      break