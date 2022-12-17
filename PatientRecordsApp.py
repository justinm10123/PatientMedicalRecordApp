#Georgetown Pediatrics Patient Medical Records Application
import os
import tkinter as tk
import pandas as pd


#file directory for all patient record txt files
text_file_directory = "G:/Georgetown Data/Discrete"
person_text_file = "G:/Georgetown Data/Discrete/Person.txt"

readfile_Person = open("G:/Georgetown Data/Discrete/Person.txt","r")

#testing out reading each line 1 by 1
readlinestest = readfile_Person.readlines()

#splitting each line by the | character
for line in readlinestest:
    # split the line into words
    words = line.split("|")
    first_word = words[0:100]

#pandas reads in the person.txt file
pandas_person_read = pd.read_table(person_text_file, delimiter = "|")
print(pandas_person_read)


counter = 0
patient_ID_input = input("Enter a Patient ID: ")

#for loop that runs through and will print each line? had to break it cause it kept repeating
# index = x, row = y
for index, row in pandas_person_read.iterrows():
    print(row, "\n")
    counter += 1

    if counter >5:
        break

filtered_list = pandas_person_read[pandas_person_read["PersonID"].std.startswith(patient_ID_input)]
print(filtered_list)