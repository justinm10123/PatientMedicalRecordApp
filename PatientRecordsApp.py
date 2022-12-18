#Georgetown Pediatrics Patient Medical Records Application
import os
import tkinter as tk


#file directory for all patient record txt files
text_file_directory = "G:/Georgetown Data/Discrete"
person_file = open("G:/Georgetown Data/Discrete/Person.txt","r")

search_term = input("Enter a Patient ID #, First and Last name, or type Quit to Stop: ")
split_search_term = search_term.split()

  # Read the rest of the lines in the file
for line in person_file:
    # Split the line into a list of words
    words = line.split("|")
    
    if search_term.lower() == "quit":
        break

    # Check if the first word in the line matches the search term
    elif (words[2].lower() == split_search_term[0].lower() and words[5].lower() == split_search_term[1].lower()) or (words[0].lower() == search_term.lower()):
      # If it does, print the entire line
      split_person_line = line.split("|")
      print(split_person_line)