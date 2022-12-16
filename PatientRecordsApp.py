#Georgetown Pediatrics Patient Medical Records Application
import os
import tkinter as tk


#file directory for all patient record txt files
text_file_directory = "G:/Georgetown Data/Discrete"

readfile_Person = open("G:/Georgetown Data/Discrete/Person.txt","r")

readlinestest = readfile_Person.readlines()

for line in readlinestest:
    # split the line into words
    words = line.split("|")
    first_word = words[0:100]




print(first_word)