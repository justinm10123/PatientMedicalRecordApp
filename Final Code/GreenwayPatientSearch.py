import os
import tkinter as tk
from tkinter import filedialog
import re
from datetime import datetime

# Create the tkinter window
window = tk.Tk()
window.title("Patient Records Search")
window.configure(bg = "#6e9887")
window.geometry("1600x750")

# Function to search for the name in the text file
def comprehensive_patient_search():
  # Get the user's first and last name
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  month = month_entry.get()
  day = day_entry.get()
  year = year_entry.get()
  date_of_birth = str(year + "-" + month + "-" + day)

  # Open the text file and search for the name
  with open("/Georgetown Data/Discrete/Person.txt", "r") as person_file:
    # Read the first line of the file (the header)
    header = person_file.readline().rstrip()
    # Split the header by the '|' character
    header_words = header.split("|")

    # Initialize the output text
    output_text = "BASIC DEMOGRAPHIC INFORMATION:---------------------------------------------------------------BASIC DEMOGRAPHIC INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line in person_file:
      # Split the line by the '|' character
      parts = line.split("|")
      # Check if the first and last name match the line
      if parts[2].lower() == first_name.lower() and parts[5].lower() == last_name.lower() and date_of_birth in parts[10]:
        # Zip the header words and line words together and add them to the output text
        if parts[8] == "0": #Suffix ID
          parts[8] = ""
        elif parts[8] == "1":
          parts[8] = "(1) Jr."
        elif parts[8] == "2":
          parts[8] = "(2) Sr."
        elif parts[8] == "3":
          parts[8] = "(3) I"
        elif parts[8] == "4":
          parts[8] = "(4) II"
        elif parts[8] == "5":
          parts[8] = "(5) III"
        elif parts[8] == "6":
          parts[8] = "(6) IV"

        if parts[1] == "0": #Prefix ID
          parts[1] = ""

        if parts[13] == "0":   #Marriage Status
          parts[13] = "(0) Unknown"
        elif parts[13] == "1":
          parts[13] = "(1) Married"
        elif parts[13] == "2":
          parts[13] = "(2) Single"
        elif parts[13] == "3":
          parts[13] = "(3) Widowed"
        elif parts[13] == "4":
          parts[13] = "(4) Divorced"
        elif parts[13] == "5":
          parts[13] = "(5) Seperated"
        elif parts[13] == "6":
          parts[13] = "(6) Other"
        elif parts[13] == "7":
          parts[13] = "(7) Common Law"
        elif parts[13] == "8":
          parts[13] = "(8) Living Together"
        elif parts[13] == "9":
          parts[13] = "(9) Domestic Partner"
        elif parts[13] == "10":
          parts[13] = "(10) Registered Domestic Partner"
        elif parts[13] == "11":
          parts[13] = "(11) Legally Seperated"
        elif parts[13] == "12":
          parts[13] = "(12) Annulled"
        elif parts[13] == "13":
          parts[13] = "(13) Interlocutory"
        elif parts[13] == "14":
          parts[13] = "(14) Unmarried"
        elif parts[13] == "15":
          parts[13] = "(15) Unreported"

        if parts[19] == "1":   #Race ID
          parts[19] = "(1) White"
        elif parts[19] == "2":
          parts[19] = "(2) Black"
        elif parts[19] == "3":
          parts[19] = "(3) Other"
        elif parts[19] == "4":
          parts[19] = "(4) American Indian / Alaska Native"
        elif parts[19] == "5":
          parts[19] = "(5) Asian"
        elif parts[19] == "7":
          parts[19] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts[19] == "8":
          parts[19] = "(8) Declined"

        if parts[12] == "0":   #Gender ID
          parts[12] = "(0) Unknown"
        elif parts[12] == "1":
          parts[12] = "(1) Female"
        elif parts[12] == "2":
          parts[12] = "(2) Male"
        elif parts[12] == "3":
          parts[12] = "(3) Other"
        
        if parts[36] == "0":   #Ethnicity
          parts[36] = "(0) Unknown"
        elif parts[36] == "1":
          parts[36] = "(1) Hispanic or Latino"
        elif parts[36] == "2":
          parts[36] = "(2) Not Hispanic or Latino"
        elif parts[36] == "3":
          parts[36] = "(3) Declined"

        if parts[21] == "0":   #Religion ID
          parts[21] = "(0) Unknown"
        elif parts[21] == "1":
          parts[21] = "(1) Protestant"
        elif parts[21] == "2":
          parts[21] = "(2) Catholic"
        elif parts[21] == "3":
          parts[21] = "(3) Buddhist"
        elif parts[21] == "4":
          parts[21] = "(4) Hindu"
        elif parts[21] == "5":
          parts[21] = "(5) Islam"
        elif parts[21] == "6":
          parts[21] = "(6) Other"
        elif parts[21] == "7":
          parts[21] = "(7) Jewish"
        elif parts[21] == "8":
          parts[21] = "(8) Jehovah's Witness"
        elif parts[21] == "9":
          parts[21] = "(9) Mormon"
        elif parts[21] == "99":
          parts[21] = "(99) N/A"

        if parts[17] == "0":   #Primary Language ID
          parts[17] = "(0) Unknown"
        elif parts[17] == "1":
          parts[17] = "(1) English"
        elif parts[17] == "2":
          parts[17] = "(2) Spanish"
        elif parts[17] == "3":
          parts[17] = "(3) French"
        elif parts[17] == "4":
          parts[17] = "(4) Japanese"
        elif parts[17] == "5":
          parts[17] = "(5) Chinese"
        elif parts[17] == "6":
          parts[17] = "(6) Vietnamese"
        elif parts[17] == "7":
          parts[17] = "(7) Russian"
        elif parts[17] == "8":
          parts[17] = "(8) Arabic"
        elif parts[17] == "9":
          parts[17] = "(9) Filipino"
        elif parts[17] == "10":
          parts[17] = "(10) German"
        elif parts[17] == "11":
          parts[17] = "(11) Greek"
        elif parts[17] == "12":
          parts[17] = "(12) Hindi"
        elif parts[17] == "13":
          parts[17] = "(13) Italian"
        elif parts[17] == "14":
          parts[17] = "(14) Korean"
        elif parts[17] == "15":
          parts[17] = "(15) Polish"
        elif parts[17] == "16":
          parts[17] = "(16) Portuguese"
        elif parts[17] == "17":
          parts[17] = "(17) Other"
        elif parts[17] == "18":
          parts[17] = "(18) Declined"
        else:
          parts[17] = "Other"

        if parts[18] == "0":   #Secondary Language ID
          parts[18] = "(0) Unknown"
        elif parts[18] == "1":
          parts[18] = "(1) English"
        elif parts[18] == "2":
          parts[18] = "(2) Spanish"
        elif parts[18] == "3":
          parts[18] = "(3) French"
        elif parts[18] == "4":
          parts[18] = "(4) Japanese"
        elif parts[18] == "5":
          parts[18] = "(5) Chinese"
        elif parts[18] == "6":
          parts[18] = "(6) Vietnamese"
        elif parts[18] == "7":
          parts[18] = "(7) Russian"
        elif parts[18] == "8":
          parts[18] = "(8) Arabic"
        elif parts[18] == "9":
          parts[18] = "(9) Filipino"
        elif parts[18] == "10":
          parts[18] = "(10) German"
        elif parts[18] == "11":
          parts[18] = "(11) Greek"
        elif parts[18] == "12":
          parts[18] = "(12) Hindi"
        elif parts[18] == "13":
          parts[18] = "(13) Italian"
        elif parts[18] == "14":
          parts[18] = "(14) Korean"
        elif parts[18] == "15":
          parts[18] = "(15) Polish"
        elif parts[18] == "16":
          parts[18] = "(16) Portuguese"
        elif parts[18] == "17":
          parts[18] = "(17) Other"
        elif parts[18] == "18":
          parts[18] = "(18) Declined"
        else:
          parts[18] = "Other"

        if parts[30] == "0":
          parts[30] = "(0) False"
        elif parts[30] == "1":
          parts[30] = "(1) True/Active"


        
        result = ["{}: {}".format(h, p) for h, p in zip(header_words, parts)]
        output_text += "\n".join(result) + "\n"
        patient_id = parts[0]
        address_id = parts[29]
        global full_name
        full_name = parts[2],parts[5]
        global patient_document_path
        patient_document_path = "/Georgetown Data/Docs - Exported/Document/Document/" + patient_id
        global sticky_note_check
        sticky_note_check = "StickyNotes_" + patient_id + "_" + last_name.strip().title() + ", " + first_name.strip().title() + "_" + month + "-" + day + "-" + year
        break
      else:
        pass

  sticky_notes_directory = "/Georgetown Data/StickyNotes/StickyNotes"
  sticky_notes_file_list = os.listdir(sticky_notes_directory)

  for x in sticky_notes_file_list:
    if sticky_note_check in x:
      sticky_notes_label.configure(text = "Sticky Note Found", bg = "SpringGreen2")
      break
    else:
      sticky_notes_label.configure(text = "No Sticky Note Found", bg = "Coral1")
  
  with open("/Georgetown Data/Discrete/Patient.txt", "r") as patient_file:
    # Read the first line of the file (the header)
    header2 = patient_file.readline().rstrip()
    # Split the header by the '|' character
    header_words2 = header2.split("|")

    output_text += "PATIENT INFORMATION:---------------------------------------------------------------PATIENT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line2 in patient_file:
      # Split the line by the '|' character
      parts2 = line2.split("|")
      # Check if the first and last name match the line
      if parts2[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        if parts2[13] == "0":     #Enabled True/False
          parts2[13] = "(0) False"
        elif parts2[13] == "1":
          parts2[13] = "(1) True/Active"

        if parts2[14] == "0":     #Is patient True/False
          parts2[14] = "(0) False"
        elif parts2[14] == "1":
          parts2[14] = "(1) True/Active"

        result2 = ["{}: {}".format(h, p) for h, p in zip(header_words2, parts2)]
        output_text += "\n".join(result2) + "\n"
        care_provider_id = parts2[19]
        break

  with open("/Georgetown Data/Discrete/Address.txt", "r") as address_file:
    # Read the first line of the file (the header)
    header3 = address_file.readline().rstrip()
    # Split the header by the '|' character
    header_words3 = header3.split("|")

    output_text += "ADDRESS INFORMATION:---------------------------------------------------------------ADDRESS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line3 in address_file:
      # Split the line by the '|' character
      parts3 = line3.split("|")
      # Check if the first and last name match the line
      if parts3[0] == address_id:
        # Zip the header words and line words together and add them to the output text

        if parts3[6] == "0":     #Country
          parts3[6] = "(0) Unknown"
        elif parts3[6] == "1":
          parts3[6] = "(1) United States"
        elif parts3[6] == "2":
          parts3[6] = "(2) Mexico"
        elif parts3[6] == "3":
          parts3[6] = "(3) Canada"
        elif parts3[6] == "4":
          parts3[6] = "(4) United States Military"


        result3 = ["{}: {}".format(h, p) for h, p in zip(header_words3, parts3)]
        output_text += "\n".join(result3) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Allergy.txt", "r") as allergy_file: ################################## MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header4 = allergy_file.readline().rstrip()
    # Split the header by the '|' character
    header_words4 = header4.split("|")

    output_text += "ALLERGY INFORMATION:---------------------------------------------------------------ALLERGY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line4 in allergy_file:
      # Split the line by the '|' character
      parts4 = line4.split("|")
      # Check if the first and last name match the line
      if parts4[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result4 = ["{}: {}".format(h, p) for h, p in zip(header_words4, parts4)]
        output_text += "\n".join(result4) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/br_Account.txt", "r") as br_account_file:
    # Read the first line of the file (the header)
    header5 = br_account_file.readline().rstrip()
    # Split the header by the '|' character
    header_words5 = header5.split("|")

    output_text += "BASIC ACCOUNT INFORMATION:---------------------------------------------------------------BASIC ACCOUNT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line5 in br_account_file:
      # Split the line by the '|' character
      parts5 = line5.split("|")
      # Check if the first and last name match the line
      if parts5[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result5 = ["{}: {}".format(h, p) for h, p in zip(header_words5, parts5)]
        output_text += "\n".join(result5) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/ClinicalVital.txt", "r") as clinical_vital_file: ######################################### MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header6 = clinical_vital_file.readline().rstrip()
    # Split the header by the '|' character
    header_words6 = header6.split("|")

    output_text += "CLINICAL VITALS INFORMATION:---------------------------------------------------------------CLINICAL VITALS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line6 in clinical_vital_file:
      # Split the line by the '|' character
      parts6 = line6.split("|")
      # Check if the first and last name match the line
      if parts6[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result6 = ["{}: {}".format(h, p) for h, p in zip(header_words6, parts6)]
        output_text += "\n".join(result6) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatientFlags.txt", "r") as patient_flags_file: ######################################### MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header7 = patient_flags_file.readline().rstrip()
    # Split the header by the '|' character
    header_words7 = header7.split("|")

    output_text += "PATIENT FLAGS INFORMATION:---------------------------------------------------------------PATIENT FLAGS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line7 in patient_flags_file:
      # Split the line by the '|' character
      parts7 = line7.split("|")
      # Check if the first and last name match the line
      if parts7[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result7 = ["{}: {}".format(h, p) for h, p in zip(header_words7, parts7)]
        output_text += "\n".join(result7) + "\n"
        flag_id = parts7[1]
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Flag.txt", "r") as flag_file:
    # Read the first line of the file (the header)
    header8 = flag_file.readline().rstrip()
    # Split the header by the '|' character
    header_words8 = header8.split("|")

    output_text += "FLAG INFORMATION:---------------------------------------------------------------FLAG INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line8 in flag_file:
      # Split the line by the '|' character
      parts8 = line8.split("|")
      # Check if the first and last name match the line
      if parts8[0] == flag_id:
        # Zip the header words and line words together and add them to the output text
        result8 = ["{}: {}".format(h, p) for h, p in zip(header_words8, parts8)]
        output_text += "\n".join(result8) + "\n"
        break

  with open("/Georgetown Data/Discrete/InsuranceCoverage.txt", "r") as insurance_coverage_file: ######################################### MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header9 = insurance_coverage_file.readline().rstrip()
    # Split the header by the '|' character
    header_words9 = header9.split("|")

    output_text += "INSURANCE COVERAGE INFORMATION:---------------------------------------------------------------INSURANCE COVERAGE INFORMATION:\n"
    
    insurance_coverage_plan_id_array = [] #array containing insurance coverage PLAN ID's
    insurance_coverage_ins_id_array = []

    # Search for the name in the remaining lines of the file
    for line9 in insurance_coverage_file:
      # Split the line by the '|' character
      parts9 = line9.split("|")
      
      # Check if the first and last name match the line
      if parts9[1] == patient_id:
        insurance_coverage_plan_id_array.append(parts9[2])
        insurance_coverage_ins_id_array.append(parts9[0])
        # Zip the header words and line words together and add them to the output text
        result9 = ["{}: {}".format(h, p) for h, p in zip(header_words9, parts9)]
        output_text += "\n".join(result9) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/InsurancePlan.txt", "r") as insurance_plan_file:
    # Read the first line of the file (the header)
    header10 = insurance_plan_file.readline().rstrip()
    # Split the header by the '|' character
    header_words10 = header10.split("|")

    output_text += "INSURANCE PLAN INFORMATION:---------------------------------------------------------------INSURANCE PLAN INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line10 in insurance_plan_file:
      # Split the line by the '|' character
      parts10 = line10.split("|")
      # Check if the first and last name match the line
      if parts10[0] in insurance_coverage_plan_id_array:
        # Zip the header words and line words together and add them to the output text
        result10 = ["{}: {}".format(h, p) for h, p in zip(header_words10, parts10)]
        output_text += "\n".join(result10) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/InsCoveragePatient.txt", "r") as ins_coverage_patient_file:
    # Read the first line of the file (the header)
    header11 = ins_coverage_patient_file.readline().rstrip()
    # Split the header by the '|' character
    header_words11 = header11.split("|")

    output_text += "PRIORITY OF PATIENT INSURANCE COVERAGE INFORMATION:---------------------------------------------------------------PRIORITY OF PATIENT INSURANCE COVERAGE INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line11 in ins_coverage_patient_file:
      # Split the line by the '|' character
      parts11 = line11.split("|")
      # Check if the first and last name match the line
      if parts11[1] in insurance_coverage_ins_id_array:
        # Zip the header words and line words together and add them to the output text
        result11 = ["{}: {}".format(h, p) for h, p in zip(header_words11, parts11)]
        output_text += "\n".join(result11) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Medications.txt", "r") as medications_file:
    # Read the first line of the file (the header)
    header12 = medications_file.readline().rstrip()
    # Split the header by the '|' character
    header_words12 = header12.split("|")

    output_text += "MEDICATIONS INFORMATION:---------------------------------------------------------------MEDICATIONS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line12 in medications_file:
      # Split the line by the '|' character
      parts12 = line12.split("|")
      # Check if the first and last name match the line
      if parts12[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result12 = ["{}: {}".format(h, p) for h, p in zip(header_words12, parts12)]
        output_text += "\n".join(result12) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/NextOfKin.txt", "r") as next_of_kin_file:
    # Read the first line of the file (the header)
    header13 = next_of_kin_file.readline().rstrip()
    # Split the header by the '|' character
    header_words13 = header13.split("|")

    output_text += "NEXT OF KIN INFORMATION:---------------------------------------------------------------NEXT OF KIN INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line13 in next_of_kin_file:
      # Split the line by the '|' character
      parts13 = line13.split("|")
      # Check if the first and last name match the line
      if parts13[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        if parts13[4] == "0":     #Enabled True/False
          parts13[4] = "(0) False"
        elif parts13[4] == "1":
          parts13[4] = "(1) True/Active"

        if parts13[10] == "0": #Prefix ID
          parts13[10] = ""

        if parts13[17] == "0": #Suffix ID
          parts13[17] = ""
        elif parts13[17] == "1":
          parts13[17] = "(1) Jr."
        elif parts13[17] == "2":
          parts13[17] = "(2) Sr."
        elif parts13[17] == "3":
          parts13[17] = "(3) I"
        elif parts13[17] == "4":
          parts13[17] = "(4) II"
        elif parts13[17] == "5":
          parts13[17] = "(5) III"
        elif parts13[17] == "6":
          parts13[17] = "(6) IV"

        if parts13[21] == "0": #Gender ID
          parts13[21] = "Unknown"
        elif parts13[21] == "1":
          parts13[21] = "(1) Female"
        elif parts13[21] == "2":
          parts13[21] = "(2) Male"
        elif parts13[21] == "3":
          parts13[21] = "(3) Other"

        if parts13[22] == "0":   #Marriage Status
          parts13[22] = "(0) Unknown"
        elif parts13[22] == "1":
          parts13[22] = "(1) Married"
        elif parts13[22] == "2":
          parts13[22] = "(2) Single"
        elif parts13[22] == "3":
          parts13[22] = "(3) Widowed"
        elif parts13[22] == "4":
          parts13[22] = "(4) Divorced"
        elif parts13[22] == "5":
          parts13[22] = "(5) Seperated"
        elif parts13[22] == "6":
          parts13[22] = "(6) Other"
        elif parts13[22] == "7":
          parts13[22] = "(7) Common Law"
        elif parts13[22] == "8":
          parts13[22] = "(8) Living Together"
        elif parts13[22] == "9":
          parts13[22] = "(9) Domestic Partner"
        elif parts13[22] == "10":
          parts13[22] = "(10) Registered Domestic Partner"
        elif parts13[22] == "11":
          parts13[22] = "(11) Legally Seperated"
        elif parts13[22] == "12":
          parts13[22] = "(12) Annulled"
        elif parts13[22] == "13":
          parts13[22] = "(13) Interlocutory"
        elif parts13[22] == "14":
          parts13[22] = "(14) Unmarried"
        elif parts13[22] == "15":
          parts13[22] = "(15) Unreported"

        if parts13[26] == "0":   #Primary Language ID
          parts13[26] = "(0) Unknown"
        elif parts13[26] == "1":
          parts13[26] = "(1) English"
        elif parts13[26] == "2":
          parts13[26] = "(2) Spanish"
        elif parts13[26] == "3":
          parts13[26] = "(3) French"
        elif parts13[26] == "4":
          parts13[26] = "(4) Japanese"
        elif parts13[26] == "5":
          parts13[26] = "(5) Chinese"
        elif parts13[26] == "6":
          parts13[26] = "(6) Vietnamese"
        elif parts13[26] == "7":
          parts13[26] = "(7) Russian"
        elif parts13[26] == "8":
          parts13[26] = "(8) Arabic"
        elif parts13[26] == "9":
          parts13[26] = "(9) Filipino"
        elif parts13[26] == "10":
          parts13[26] = "(10) German"
        elif parts13[26] == "11":
          parts13[26] = "(11) Greek"
        elif parts13[26] == "12":
          parts13[26] = "(12) Hindi"
        elif parts13[26] == "13":
          parts13[26] = "(13) Italian"
        elif parts13[26] == "14":
          parts13[26] = "(14) Korean"
        elif parts13[26] == "15":
          parts13[26] = "(15) Polish"
        elif parts13[26] == "16":
          parts13[26] = "(16) Portuguese"
        elif parts13[26] == "17":
          parts13[26] = "(17) Other"
        elif parts13[26] == "18":
          parts13[26] = "(18) Declined"
        else:
          parts13[26] = "Other"

        if parts13[27] == "0":   #Primary Language ID
          parts13[27] = "(0) Unknown"
        elif parts13[27] == "1":
          parts13[27] = "(1) English"
        elif parts13[27] == "2":
          parts13[27] = "(2) Spanish"
        elif parts13[27] == "3":
          parts13[27] = "(3) French"
        elif parts13[27] == "4":
          parts13[27] = "(4) Japanese"
        elif parts13[27] == "5":
          parts13[27] = "(5) Chinese"
        elif parts13[27] == "6":
          parts13[27] = "(6) Vietnamese"
        elif parts13[27] == "7":
          parts13[27] = "(7) Russian"
        elif parts13[27] == "8":
          parts13[27] = "(8) Arabic"
        elif parts13[27] == "9":
          parts13[27] = "(9) Filipino"
        elif parts13[27] == "10":
          parts13[27] = "(10) German"
        elif parts13[27] == "11":
          parts13[27] = "(11) Greek"
        elif parts13[27] == "12":
          parts13[27] = "(12) Hindi"
        elif parts13[27] == "13":
          parts13[27] = "(13) Italian"
        elif parts13[27] == "14":
          parts13[27] = "(14) Korean"
        elif parts13[27] == "15":
          parts13[27] = "(15) Polish"
        elif parts13[27] == "16":
          parts13[27] = "(16) Portuguese"
        elif parts13[27] == "17":
          parts13[27] = "(17) Other"
        elif parts13[27] == "18":
          parts13[27] = "(18) Declined"
        else:
          parts13[27] = "Other"

        if parts13[28] == "1":   #Race ID
          parts13[28] = "(1) White"
        elif parts13[28] == "2":
          parts13[28] = "(2) Black"
        elif parts13[28] == "3":
          parts13[28] = "(3) Other"
        elif parts13[28] == "4":
          parts13[28] = "(4) American Indian / Alaska Native"
        elif parts13[28] == "5":
          parts13[28] = "(5) Asian"
        elif parts13[28] == "7":
          parts13[28] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts13[28] == "8":
          parts13[28] = "(8) Declined"

        if parts13[30] == "0":   #Religion ID
          parts13[30] = "(0) Unknown"
        elif parts13[30] == "1":
          parts13[30] = "(1) Protestant"
        elif parts13[30] == "2":
          parts13[30] = "(2) Catholic"
        elif parts13[30] == "3":
          parts13[30] = "(3) Buddhist"
        elif parts13[30] == "4":
          parts13[30] = "(4) Hindu"
        elif parts13[30] == "5":
          parts13[30] = "(5) Islam"
        elif parts13[30] == "6":
          parts13[30] = "(6) Other"
        elif parts13[30] == "7":
          parts13[30] = "(7) Jewish"
        elif parts13[30] == "8":
          parts13[30] = "(8) Jehovah's Witness"
        elif parts13[30] == "9":
          parts13[30] = "(9) Mormon"
        elif parts13[30] == "99":
          parts13[30] = "(99) N/A"

        if parts13[39] == "0":     #Enabled True/False
          parts13[39] = "(0) False"
        elif parts13[39] == "1":
          parts13[39] = "(1) True/Active"

        if parts13[45] == "0":     #Ethnicity ID
          parts13[45] = "(0) Unknown"
        elif parts13[45] == "1":
          parts13[45] = "(1) Hispanic or Latino"
        elif parts13[45] == "2":
          parts13[45] = "(2) Not Hispanic or Latino"
        elif parts13[45] == "3":
          parts13[45] = "(3) Declined"

        if parts13[61] == "0":     #Country
          parts13[61] = "(0) Unknown"
        elif parts13[61] == "1":
          parts13[61] = "(1) United States"
        elif parts13[61] == "2":
          parts13[61] = "(2) Mexico"
        elif parts13[61] == "3":
          parts13[61] = "(3) Canada"
        elif parts13[61] == "4":
          parts13[61] = "(4) United States Military"
        result13 = ["{}: {}".format(h, p) for h, p in zip(header_words13, parts13)]
        output_text += "\n".join(result13) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/OrdersDetailTracking.txt", "r") as orders_detail_tracking_file:
    # Read the first line of the file (the header)
    header14 = orders_detail_tracking_file.readline().rstrip()
    # Split the header by the '|' character
    header_words14 = header14.split("|")

    output_text += "ORDERS DETAIL TRACKING INFORMATION:---------------------------------------------------------------ORDERS DETAIL TRACKING INFORMATION:\n"

    procedure_code_array = []

    # Search for the name in the remaining lines of the file
    for line14 in orders_detail_tracking_file:
      # Split the line by the '|' character
      parts14 = line14.split("|")
      # Check if the first and last name match the line
      if parts14[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result14 = ["{}: {}".format(h, p) for h, p in zip(header_words14, parts14)]
        output_text += "\n".join(result14) + "\n"
        procedure_code_array.append(parts14[7])
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/MigrationInsExport.txt", "r") as migration_ins_export_file:
    # Read the first line of the file (the header)
    header25 = migration_ins_export_file.readline().rstrip()
    # Split the header by the '|' character
    header_words25 = header25.split("|")

    output_text += "INSURANCE COMPANIES INFORMATION:---------------------------------------------------------------INSURANCE COMPANIES INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line25 in migration_ins_export_file:
      # Split the line by the '|' character
      parts25 = line25.split("|")
      # Check if the first and last name match the line
      if parts25[4] in insurance_coverage_plan_id_array:
        # Zip the header words and line words together and add them to the output text
        result25 = ["{}: {}".format(h, p) for h, p in zip(header_words25, parts25)]
        output_text += "\n".join(result25) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/MigrationProcExport.txt", "r") as migration_proc_export_file:
    # Read the first line of the file (the header)
    header22 = migration_proc_export_file.readline().rstrip()
    # Split the header by the '|' character
    header_words22 = header22.split("|")

    output_text += "PROCEDURE CODES INFORMATION:---------------------------------------------------------------PROCEDURE CODES INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line22 in migration_proc_export_file:
      # Split the line by the '|' character
      parts22 = line22.split("|")
      # Check if the first and last name match the line
      if parts22[0] in procedure_code_array:
        # Zip the header words and line words together and add them to the output text
        result22 = ["{}: {}".format(h, p) for h, p in zip(header_words22, parts22)]
        output_text += "\n".join(result22) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/MigrationReferringExport.txt", "r") as migration_referring_export_file:
    # Read the first line of the file (the header)
    header23 = migration_referring_export_file.readline().rstrip()
    # Split the header by the '|' character
    header_words23 = header23.split("|")

    output_text += "REFERRING PHYSICIANS INFORMATION:---------------------------------------------------------------REFERRING PHYSICIANS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line23 in migration_referring_export_file:
      # Split the line by the '|' character
      parts23 = line23.split("|")
      # Check if the first and last name match the line
      if parts23[0] == care_provider_id:
        # Zip the header words and line words together and add them to the output text
        result23 = ["{}: {}".format(h, p) for h, p in zip(header_words23, parts23)]
        output_text += "\n".join(result23) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/MigrationScheduleExport.txt", "r") as migration_schedule_export_file:
    # Read the first line of the file (the header)
    header24 = migration_schedule_export_file.readline().rstrip()
    # Split the header by the '|' character
    header_words24 = header24.split("|")

    output_text += "APPOINTMENTS INFORMATION:---------------------------------------------------------------APPOINTMENTS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line24 in migration_schedule_export_file:
      # Split the line by the '|' character
      parts24 = line24.split("|")
      # Check if the first and last name match the line
      if parts24[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result24 = ["{}: {}".format(h, p) for h, p in zip(header_words24, parts24)]
        output_text += "\n".join(result24) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistFamily.txt", "r") as pat_hist_family_file:
    # Read the first line of the file (the header)
    header15 = pat_hist_family_file.readline().rstrip()
    # Split the header by the '|' character
    header_words15 = header15.split("|")

    output_text += "FAMILY HISTORY INFORMATION:---------------------------------------------------------------FAMILY HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line15 in pat_hist_family_file:
      # Split the line by the '|' character
      parts15 = line15.split("|")
      # Check if the first and last name match the line
      if parts15[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result15 = ["{}: {}".format(h, p) for h, p in zip(header_words15, parts15)]
        output_text += "\n".join(result15) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistMedical.txt", "r") as pat_hist_medical_file:
    # Read the first line of the file (the header)
    header16 = pat_hist_medical_file.readline().rstrip()
    # Split the header by the '|' character
    header_words16 = header16.split("|")

    output_text += "PAST MEDICAL HISTORY INFORMATION:---------------------------------------------------------------PAST MEDICAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line16 in pat_hist_medical_file:
      # Split the line by the '|' character
      parts16 = line16.split("|")
      # Check if the first and last name match the line
      if parts16[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result16 = ["{}: {}".format(h, p) for h, p in zip(header_words16, parts16)]
        output_text += "\n".join(result16) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistSocial.txt", "r") as pat_hist_social_file:
    # Read the first line of the file (the header)
    header17 = pat_hist_social_file.readline().rstrip()
    # Split the header by the '|' character
    header_words17 = header17.split("|")

    output_text += "SOCIAL HISTORY INFORMATION:---------------------------------------------------------------SOCIAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line17 in pat_hist_social_file:
      # Split the line by the '|' character
      parts17 = line17.split("|")
      # Check if the first and last name match the line
      if parts17[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result17 = ["{}: {}".format(h, p) for h, p in zip(header_words17, parts17)]
        output_text += "\n".join(result17) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistSurgical.txt", "r") as pat_hist_surgical_file:
    # Read the first line of the file (the header)
    header18 = pat_hist_surgical_file.readline().rstrip()
    # Split the header by the '|' character
    header_words18 = header18.split("|")

    output_text += "PAST SURGICAL HISTORY INFORMATION:---------------------------------------------------------------PAST SURGICAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line18 in pat_hist_surgical_file:
      # Split the line by the '|' character
      parts18 = line18.split("|")
      # Check if the first and last name match the line
      if parts18[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result18 = ["{}: {}".format(h, p) for h, p in zip(header_words18, parts18)]
        output_text += "\n".join(result18) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatientGeneralNotes.txt", "r") as patient_general_notes_file:
    # Read the first line of the file (the header)
    header19 = patient_general_notes_file.readline().rstrip()
    # Split the header by the '|' character
    header_words19 = header19.split("|")

    output_text += "PATIENT GENERAL NOTES INFORMATION:---------------------------------------------------------------PATIENT GENERAL NOTES INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line19 in patient_general_notes_file:
      # Split the line by the '|' character
      parts19 = line19.split("|")
      # Check if the first and last name match the line
      if parts19[1] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result19 = ["{}: {}".format(h, p) for h, p in zip(header_words19, parts19)]
        output_text += "\n".join(result19) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/ProblemList.txt", "r") as problem_list_file:
    # Read the first line of the file (the header)
    header20 = problem_list_file.readline().rstrip()
    # Split the header by the '|' character
    header_words20 = header20.split("|")

    output_text += "PROBLEM LIST INFORMATION:---------------------------------------------------------------PROBLEM LIST INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line20 in problem_list_file:
      # Split the line by the '|' character
      parts20 = line20.split("|")
      # Check if the first and last name match the line
      if parts20[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result20 = ["{}: {}".format(h, p) for h, p in zip(header_words20, parts20)]
        output_text += "\n".join(result20) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/VacPat.txt", "r") as vac_pat_file:
    # Read the first line of the file (the header)
    header21 = vac_pat_file.readline().rstrip()
    # Split the header by the '|' character
    header_words21 = header21.split("|")

    output_text += "IMMUNIZATIONS INFORMATION:---------------------------------------------------------------IMMUNIZATIONS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line21 in vac_pat_file:
      # Split the line by the '|' character
      parts21 = line21.split("|")
      # Check if the first and last name match the line
      if parts21[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result21 = ["{}: {}".format(h, p) for h, p in zip(header_words21, parts21)]
        output_text += "\n".join(result21) + "\n"
      else:
        if output_text == "":
            break

  # Clear the text widget
  output_text_widget.delete("1.0", tk.END)
  # Insert the output text into the text widget
  output_text_widget.insert("1.0", output_text)







def reduced_patient_search():
  # Get the user's first and last name
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  month = month_entry.get()
  day = day_entry.get()
  year = year_entry.get()
  date_of_birth = str(year + "-" + month + "-" + day)

  # Open the text file and search for the name
  with open("/Georgetown Data/Discrete/Person.txt", "r") as person_file:
    # Read the first line of the file (the header)
    header = person_file.readline().rstrip()
    # Split the header by the '|' character
    header_words = header.split("|")

    # Initialize the output text
    output_text = "BASIC DEMOGRAPHIC INFORMATION:---------------------------------------------------------------BASIC DEMOGRAPHIC INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line in person_file:
      # Split the line by the '|' character
      parts = line.split("|")
      # Check if the first and last name match the line
      if parts[2].lower() == first_name.lower() and parts[5].lower() == last_name.lower() and date_of_birth in parts[10]:
        # Zip the header words and line words together and add them to the output text
          
        if parts[8] == "0": #Suffix ID
          parts[8] = ""
        elif parts[8] == "1":
          parts[8] = "(1) Jr."
        elif parts[8] == "2":
          parts[8] = "(2) Sr."
        elif parts[8] == "3":
          parts[8] = "(3) I"
        elif parts[8] == "4":
          parts[8] = "(4) II"
        elif parts[8] == "5":
          parts[8] = "(5) III"
        elif parts[8] == "6":
          parts[8] = "(6) IV"

        if parts[1] == "0": #Prefix ID
          parts[1] = ""

        if parts[13] == "0":   #Marriage Status
          parts[13] = "(0) Unknown"
        elif parts[13] == "1":
          parts[13] = "(1) Married"
        elif parts[13] == "2":
          parts[13] = "(2) Single"
        elif parts[13] == "3":
          parts[13] = "(3) Widowed"
        elif parts[13] == "4":
          parts[13] = "(4) Divorced"
        elif parts[13] == "5":
          parts[13] = "(5) Seperated"
        elif parts[13] == "6":
          parts[13] = "(6) Other"
        elif parts[13] == "7":
          parts[13] = "(7) Common Law"
        elif parts[13] == "8":
          parts[13] = "(8) Living Together"
        elif parts[13] == "9":
          parts[13] = "(9) Domestic Partner"
        elif parts[13] == "10":
          parts[13] = "(10) Registered Domestic Partner"
        elif parts[13] == "11":
          parts[13] = "(11) Legally Seperated"
        elif parts[13] == "12":
          parts[13] = "(12) Annulled"
        elif parts[13] == "13":
          parts[13] = "(13) Interlocutory"
        elif parts[13] == "14":
          parts[13] = "(14) Unmarried"
        elif parts[13] == "15":
          parts[13] = "(15) Unreported"

        if parts[19] == "1":   #Race ID
          parts[19] = "(1) White"
        elif parts[19] == "2":
          parts[19] = "(2) Black"
        elif parts[19] == "3":
          parts[19] = "(3) Other"
        elif parts[19] == "4":
          parts[19] = "(4) American Indian / Alaska Native"
        elif parts[19] == "5":
          parts[19] = "(5) Asian"
        elif parts[19] == "7":
          parts[19] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts[19] == "8":
          parts[19] = "(8) Declined"

        if parts[12] == "0":   #Gender ID
          parts[12] = "(0) Unknown"
        elif parts[12] == "1":
          parts[12] = "(1) Female"
        elif parts[12] == "2":
          parts[12] = "(2) Male"
        elif parts[12] == "3":
          parts[12] = "(3) Other"
        
        if parts[36] == "0":   #Ethnicity
          parts[36] = "(0) Unknown"
        elif parts[36] == "1":
          parts[36] = "(1) Hispanic or Latino"
        elif parts[36] == "2":
          parts[36] = "(2) Not Hispanic or Latino"
        elif parts[36] == "3":
          parts[36] = "(3) Declined"

        if parts[21] == "0":   #Religion ID
          parts[21] = "(0) Unknown"
        elif parts[21] == "1":
          parts[21] = "(1) Protestant"
        elif parts[21] == "2":
          parts[21] = "(2) Catholic"
        elif parts[21] == "3":
          parts[21] = "(3) Buddhist"
        elif parts[21] == "4":
          parts[21] = "(4) Hindu"
        elif parts[21] == "5":
          parts[21] = "(5) Islam"
        elif parts[21] == "6":
          parts[21] = "(6) Other"
        elif parts[21] == "7":
          parts[21] = "(7) Jewish"
        elif parts[21] == "8":
          parts[21] = "(8) Jehovah's Witness"
        elif parts[21] == "9":
          parts[21] = "(9) Mormon"
        elif parts[21] == "99":
          parts[21] = "(99) N/A"

        if parts[17] == "0":   #Primary Language ID
          parts[17] = "(0) Unknown"
        elif parts[17] == "1":
          parts[17] = "(1) English"
        elif parts[17] == "2":
          parts[17] = "(2) Spanish"
        elif parts[17] == "3":
          parts[17] = "(3) French"
        elif parts[17] == "4":
          parts[17] = "(4) Japanese"
        elif parts[17] == "5":
          parts[17] = "(5) Chinese"
        elif parts[17] == "6":
          parts[17] = "(6) Vietnamese"
        elif parts[17] == "7":
          parts[17] = "(7) Russian"
        elif parts[17] == "8":
          parts[17] = "(8) Arabic"
        elif parts[17] == "9":
          parts[17] = "(9) Filipino"
        elif parts[17] == "10":
          parts[17] = "(10) German"
        elif parts[17] == "11":
          parts[17] = "(11) Greek"
        elif parts[17] == "12":
          parts[17] = "(12) Hindi"
        elif parts[17] == "13":
          parts[17] = "(13) Italian"
        elif parts[17] == "14":
          parts[17] = "(14) Korean"
        elif parts[17] == "15":
          parts[17] = "(15) Polish"
        elif parts[17] == "16":
          parts[17] = "(16) Portuguese"
        elif parts[17] == "17":
          parts[17] = "(17) Other"
        elif parts[17] == "18":
          parts[17] = "(18) Declined"
        else:
          parts[17] = "Other"

        if parts[18] == "0":   #Secondary Language ID
          parts[18] = "(0) Unknown"
        elif parts[18] == "1":
          parts[18] = "(1) English"
        elif parts[18] == "2":
          parts[18] = "(2) Spanish"
        elif parts[18] == "3":
          parts[18] = "(3) French"
        elif parts[18] == "4":
          parts[18] = "(4) Japanese"
        elif parts[18] == "5":
          parts[18] = "(5) Chinese"
        elif parts[18] == "6":
          parts[18] = "(6) Vietnamese"
        elif parts[18] == "7":
          parts[18] = "(7) Russian"
        elif parts[18] == "8":
          parts[18] = "(8) Arabic"
        elif parts[18] == "9":
          parts[18] = "(9) Filipino"
        elif parts[18] == "10":
          parts[18] = "(10) German"
        elif parts[18] == "11":
          parts[18] = "(11) Greek"
        elif parts[18] == "12":
          parts[18] = "(12) Hindi"
        elif parts[18] == "13":
          parts[18] = "(13) Italian"
        elif parts[18] == "14":
          parts[18] = "(14) Korean"
        elif parts[18] == "15":
          parts[18] = "(15) Polish"
        elif parts[18] == "16":
          parts[18] = "(16) Portuguese"
        elif parts[18] == "17":
          parts[18] = "(17) Other"
        elif parts[18] == "18":
          parts[18] = "(18) Declined"
        else:
          parts[18] = "Other"

        if parts[30] == "0":     #Enabled True/False
          parts[30] = "(0) False"
        elif parts[30] == "1":
          parts[30] = "(1) True/Active"


        result = ["{}: {}".format(h, p) for h, p in zip(header_words, parts) if p] #################### added if p to remove any rows with no info
        output_text += "\n".join(result) + "\n"
        patient_id = parts[0]
        address_id = parts[29]
        global full_name
        full_name = parts[2],parts[5]
        global patient_document_path
        patient_document_path = "/Georgetown Data/Docs - Exported/Document/Document/" + patient_id
        global sticky_note_check
        sticky_note_check = "StickyNotes_" + patient_id + "_" + last_name.strip().title() + ", " + first_name.strip().title() + "_" + month + "-" + day + "-" + year
        break
      else:
        pass

  sticky_notes_directory = "/Georgetown Data/StickyNotes/StickyNotes"
  sticky_notes_file_list = os.listdir(sticky_notes_directory)

  for x in sticky_notes_file_list:
    if sticky_note_check in x:
      sticky_notes_label.configure(text = "Sticky Note Found", bg = "SpringGreen2")
      break
    else:
      sticky_notes_label.configure(text = "No Sticky Note Found", bg = "Coral1")
  
  with open("/Georgetown Data/Discrete/Patient.txt", "r") as patient_file:
    # Read the first line of the file (the header)
    header2 = patient_file.readline().rstrip()
    # Split the header by the '|' character
    header_words2 = header2.split("|")

    output_text += "PATIENT INFORMATION:---------------------------------------------------------------PATIENT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line2 in patient_file:
      # Split the line by the '|' character
      parts2 = line2.split("|")
      # Check if the first and last name match the line
      if parts2[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        if parts2[13] == "0":     #Enabled True/False
          parts2[13] = "(0) False"
        elif parts2[13] == "1":
          parts2[13] = "(1) True/Active"

        if parts2[14] == "0":     #Is patient True/False
          parts2[14] = "(0) False"
        elif parts2[14] == "1":
          parts2[14] = "(1) True/Active"


        result2 = ["{}: {}".format(h, p) for h, p in zip(header_words2, parts2) if p]
        output_text += "\n".join(result2) + "\n"
        care_provider_id = parts2[19]
        break

  with open("/Georgetown Data/Discrete/Address.txt", "r") as address_file:
    # Read the first line of the file (the header)
    header3 = address_file.readline().rstrip()
    # Split the header by the '|' character
    header_words3 = header3.split("|")

    output_text += "ADDRESS INFORMATION:---------------------------------------------------------------ADDRESS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line3 in address_file:
      # Split the line by the '|' character
      parts3 = line3.split("|")
      # Check if the first and last name match the line
      if parts3[0] == address_id:
        # Zip the header words and line words together and add them to the output text
          

        if parts3[6] == "0":     #Country
          parts3[6] = "(0) Unknown"
        elif parts3[6] == "1":
          parts3[6] = "(1) United States"
        elif parts3[6] == "2":
          parts3[6] = "(2) Mexico"
        elif parts3[6] == "3":
          parts3[6] = "(3) Canada"
        elif parts3[6] == "4":
          parts3[6] = "(4) United States Military"


        result3 = ["{}: {}".format(h, p) for h, p in zip(header_words3, parts3) if p]
        output_text += "\n".join(result3) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Allergy.txt", "r") as allergy_file: ################################## MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header4 = allergy_file.readline().rstrip()
    # Split the header by the '|' character
    header_words4 = header4.split("|")

    output_text += "ALLERGY INFORMATION:---------------------------------------------------------------ALLERGY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line4 in allergy_file:
      # Split the line by the '|' character
      parts4 = line4.split("|")
      # Check if the first and last name match the line
      if parts4[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
          
        result4 = ["{}: {}".format(h, p) for h, p in zip(header_words4, parts4) if p]
        output_text += "\n".join(result4) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/br_Account.txt", "r") as br_account_file:
    # Read the first line of the file (the header)
    header5 = br_account_file.readline().rstrip()
    # Split the header by the '|' character
    header_words5 = header5.split("|")

    output_text += "BASIC ACCOUNT INFORMATION:---------------------------------------------------------------BASIC ACCOUNT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line5 in br_account_file:
      # Split the line by the '|' character
      parts5 = line5.split("|")
      # Check if the first and last name match the line
      if parts5[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
          
        result5 = ["{}: {}".format(h, p) for h, p in zip(header_words5, parts5) if p]
        output_text += "\n".join(result5) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatientFlags.txt", "r") as patient_flags_file: ######################################### MULTIPLE ENTRIES
    # Read the first line of the file (the header)
    header7 = patient_flags_file.readline().rstrip()
    # Split the header by the '|' character
    header_words7 = header7.split("|")

    output_text += "PATIENT FLAGS INFORMATION:---------------------------------------------------------------PATIENT FLAGS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line7 in patient_flags_file:
      # Split the line by the '|' character
      parts7 = line7.split("|")
      # Check if the first and last name match the line
      if parts7[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        result7 = header_words7[2] + ": " + parts7[2]#["{}: {}".format(h, p) for h, p in zip(header_words7, parts7) if p]
        output_text += "".join(result7) + "\n"
        flag_id = parts7[1]
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Flag.txt", "r") as flag_file:
    # Read the first line of the file (the header)
    header8 = flag_file.readline().rstrip()
    # Split the header by the '|' character
    header_words8 = header8.split("|")

    output_text += "FLAG INFORMATION:---------------------------------------------------------------FLAG INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line8 in flag_file:
      # Split the line by the '|' character
      parts8 = line8.split("|")
      # Check if the first and last name match the line
      if parts8[0] == flag_id:
        # Zip the header words and line words together and add them to the output text
        parts8[3] = ""
          
        result8 = ["{}: {}".format(h, p) for h, p in zip(header_words8, parts8) if p]
        output_text += "\n".join(result8) + "\n"
        break

  with open("/Georgetown Data/Discrete/NextOfKin.txt", "r") as next_of_kin_file:
    # Read the first line of the file (the header)
    header13 = next_of_kin_file.readline().rstrip()
    # Split the header by the '|' character
    header_words13 = header13.split("|")

    output_text += "NEXT OF KIN INFORMATION:---------------------------------------------------------------NEXT OF KIN INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line13 in next_of_kin_file:
      # Split the line by the '|' character
      parts13 = line13.split("|")
      # Check if the first and last name match the line
      if parts13[0] == patient_id and parts13[1] == "Financially Responsible Party":
        # Zip the header words and line words together and add them to the output text

        if parts13[4] == "0":     #Enabled True/False
          parts13[4] = "(0) False"
        elif parts13[4] == "1":
          parts13[4] = "(1) True/Active"

        if parts13[10] == "0": #Prefix ID
          parts13[10] = ""

        if parts13[17] == "0": #Suffix ID
          parts13[17] = ""
        elif parts13[17] == "1":
          parts13[17] = "(1) Jr."
        elif parts13[17] == "2":
          parts13[17] = "(2) Sr."
        elif parts13[17] == "3":
          parts13[17] = "(3) I"
        elif parts13[17] == "4":
          parts13[17] = "(4) II"
        elif parts13[17] == "5":
          parts13[17] = "(5) III"
        elif parts13[17] == "6":
          parts13[17] = "(6) IV"

        if parts13[21] == "0": #Gender ID
          parts13[21] = "Unknown"
        elif parts13[21] == "1":
          parts13[21] = "(1) Female"
        elif parts13[21] == "2":
          parts13[21] = "(2) Male"
        elif parts13[21] == "3":
          parts13[21] = "(3) Other"

        if parts13[22] == "0":   #Marriage Status
          parts13[22] = "(0) Unknown"
        elif parts13[22] == "1":
          parts13[22] = "(1) Married"
        elif parts13[22] == "2":
          parts13[22] = "(2) Single"
        elif parts13[22] == "3":
          parts13[22] = "(3) Widowed"
        elif parts13[22] == "4":
          parts13[22] = "(4) Divorced"
        elif parts13[22] == "5":
          parts13[22] = "(5) Seperated"
        elif parts13[22] == "6":
          parts13[22] = "(6) Other"
        elif parts13[22] == "7":
          parts13[22] = "(7) Common Law"
        elif parts13[22] == "8":
          parts13[22] = "(8) Living Together"
        elif parts13[22] == "9":
          parts13[22] = "(9) Domestic Partner"
        elif parts13[22] == "10":
          parts13[22] = "(10) Registered Domestic Partner"
        elif parts13[22] == "11":
          parts13[22] = "(11) Legally Seperated"
        elif parts13[22] == "12":
          parts13[22] = "(12) Annulled"
        elif parts13[22] == "13":
          parts13[22] = "(13) Interlocutory"
        elif parts13[22] == "14":
          parts13[22] = "(14) Unmarried"
        elif parts13[22] == "15":
          parts13[22] = "(15) Unreported"

        if parts13[26] == "0":   #Primary Language ID
          parts13[26] = "(0) Unknown"
        elif parts13[26] == "1":
          parts13[26] = "(1) English"
        elif parts13[26] == "2":
          parts13[26] = "(2) Spanish"
        elif parts13[26] == "3":
          parts13[26] = "(3) French"
        elif parts13[26] == "4":
          parts13[26] = "(4) Japanese"
        elif parts13[26] == "5":
          parts13[26] = "(5) Chinese"
        elif parts13[26] == "6":
          parts13[26] = "(6) Vietnamese"
        elif parts13[26] == "7":
          parts13[26] = "(7) Russian"
        elif parts13[26] == "8":
          parts13[26] = "(8) Arabic"
        elif parts13[26] == "9":
          parts13[26] = "(9) Filipino"
        elif parts13[26] == "10":
          parts13[26] = "(10) German"
        elif parts13[26] == "11":
          parts13[26] = "(11) Greek"
        elif parts13[26] == "12":
          parts13[26] = "(12) Hindi"
        elif parts13[26] == "13":
          parts13[26] = "(13) Italian"
        elif parts13[26] == "14":
          parts13[26] = "(14) Korean"
        elif parts13[26] == "15":
          parts13[26] = "(15) Polish"
        elif parts13[26] == "16":
          parts13[26] = "(16) Portuguese"
        elif parts13[26] == "17":
          parts13[26] = "(17) Other"
        elif parts13[26] == "18":
          parts13[26] = "(18) Declined"
        else:
          parts13[26] = "Other"

        if parts13[27] == "0":   #Primary Language ID
          parts13[27] = "(0) Unknown"
        elif parts13[27] == "1":
          parts13[27] = "(1) English"
        elif parts13[27] == "2":
          parts13[27] = "(2) Spanish"
        elif parts13[27] == "3":
          parts13[27] = "(3) French"
        elif parts13[27] == "4":
          parts13[27] = "(4) Japanese"
        elif parts13[27] == "5":
          parts13[27] = "(5) Chinese"
        elif parts13[27] == "6":
          parts13[27] = "(6) Vietnamese"
        elif parts13[27] == "7":
          parts13[27] = "(7) Russian"
        elif parts13[27] == "8":
          parts13[27] = "(8) Arabic"
        elif parts13[27] == "9":
          parts13[27] = "(9) Filipino"
        elif parts13[27] == "10":
          parts13[27] = "(10) German"
        elif parts13[27] == "11":
          parts13[27] = "(11) Greek"
        elif parts13[27] == "12":
          parts13[27] = "(12) Hindi"
        elif parts13[27] == "13":
          parts13[27] = "(13) Italian"
        elif parts13[27] == "14":
          parts13[27] = "(14) Korean"
        elif parts13[27] == "15":
          parts13[27] = "(15) Polish"
        elif parts13[27] == "16":
          parts13[27] = "(16) Portuguese"
        elif parts13[27] == "17":
          parts13[27] = "(17) Other"
        elif parts13[27] == "18":
          parts13[27] = "(18) Declined"
        else:
          parts13[27] = "Other"

        if parts13[28] == "1":   #Race ID
          parts13[28] = "(1) White"
        elif parts13[28] == "2":
          parts13[28] = "(2) Black"
        elif parts13[28] == "3":
          parts13[28] = "(3) Other"
        elif parts13[28] == "4":
          parts13[28] = "(4) American Indian / Alaska Native"
        elif parts13[28] == "5":
          parts13[28] = "(5) Asian"
        elif parts13[28] == "7":
          parts13[28] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts13[28] == "8":
          parts13[28] = "(8) Declined"

        if parts13[30] == "0":   #Religion ID
          parts13[30] = "(0) Unknown"
        elif parts13[30] == "1":
          parts13[30] = "(1) Protestant"
        elif parts13[30] == "2":
          parts13[30] = "(2) Catholic"
        elif parts13[30] == "3":
          parts13[30] = "(3) Buddhist"
        elif parts13[30] == "4":
          parts13[30] = "(4) Hindu"
        elif parts13[30] == "5":
          parts13[30] = "(5) Islam"
        elif parts13[30] == "6":
          parts13[30] = "(6) Other"
        elif parts13[30] == "7":
          parts13[30] = "(7) Jewish"
        elif parts13[30] == "8":
          parts13[30] = "(8) Jehovah's Witness"
        elif parts13[30] == "9":
          parts13[30] = "(9) Mormon"
        elif parts13[30] == "99":
          parts13[30] = "(99) N/A"

        if parts13[39] == "0":     #Enabled True/False
          parts13[39] = "(0) False"
        elif parts13[39] == "1":
          parts13[39] = "(1) True/Active"

        if parts13[45] == "0":     #Ethnicity ID
          parts13[45] = "(0) Unknown"
        elif parts13[45] == "1":
          parts13[45] = "(1) Hispanic or Latino"
        elif parts13[45] == "2":
          parts13[45] = "(2) Not Hispanic or Latino"
        elif parts13[45] == "3":
          parts13[45] = "(3) Declined"

        if parts13[61] == "0":     #Country
          parts13[61] = "(0) Unknown"
        elif parts13[61] == "1":
          parts13[61] = "(1) United States"
        elif parts13[61] == "2":
          parts13[61] = "(2) Mexico"
        elif parts13[61] == "3":
          parts13[61] = "(3) Canada"
        elif parts13[61] == "4":
          parts13[61] = "(4) United States Military"


        parts13[2] = ""
        parts13[7] = ""
        parts13[8] = ""

        result13 = ["{}: {}".format(h, p) for h, p in zip(header_words13, parts13) if p]
        output_text += "\n".join(result13) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistMedical.txt", "r") as pat_hist_medical_file:
    # Read the first line of the file (the header)
    header16 = pat_hist_medical_file.readline().rstrip()
    # Split the header by the '|' character
    header_words16 = header16.split("|")

    output_text += "PAST MEDICAL HISTORY INFORMATION:---------------------------------------------------------------PAST MEDICAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line16 in pat_hist_medical_file:
      # Split the line by the '|' character
      parts16 = line16.split("|")
      # Check if the first and last name match the line
      if parts16[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result16 = ["{}: {}".format(h, p) for h, p in zip(header_words16, parts16) if p]
        output_text += "\n".join(result16) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistSurgical.txt", "r") as pat_hist_surgical_file:
    # Read the first line of the file (the header)
    header18 = pat_hist_surgical_file.readline().rstrip()
    # Split the header by the '|' character
    header_words18 = header18.split("|")

    output_text += "PAST SURGICAL HISTORY INFORMATION:---------------------------------------------------------------PAST SURGICAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line18 in pat_hist_surgical_file:
      # Split the line by the '|' character
      parts18 = line18.split("|")
      # Check if the first and last name match the line
      if parts18[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result18 = ["{}: {}".format(h, p) for h, p in zip(header_words18, parts18) if p]
        output_text += "\n".join(result18) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/ProblemList.txt", "r") as problem_list_file:
    # Read the first line of the file (the header)
    header20 = problem_list_file.readline().rstrip()
    # Split the header by the '|' character
    header_words20 = header20.split("|")

    output_text += "PROBLEM LIST INFORMATION:---------------------------------------------------------------PROBLEM LIST INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line20 in problem_list_file:
      # Split the line by the '|' character
      parts20 = line20.split("|")
      # Check if the first and last name match the line
      if parts20[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result20 = ["{}: {}".format(h, p) for h, p in zip(header_words20, parts20) if p]
        output_text += "\n".join(result20) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatientGeneralNotes.txt", "r") as patient_general_notes_file:
    # Read the first line of the file (the header)
    header19 = patient_general_notes_file.readline().rstrip()
    # Split the header by the '|' character
    header_words19 = header19.split("|")

    output_text += "PATIENT GENERAL NOTES INFORMATION:---------------------------------------------------------------PATIENT GENERAL NOTES INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line19 in patient_general_notes_file:
      # Split the line by the '|' character
      parts19 = line19.split("|")
      # Check if the first and last name match the line
      if parts19[1] == patient_id:
        # Zip the header words and line words together and add them to the output text
        result19 = ["{}: {}".format(h, p) for h, p in zip(header_words19, parts19) if p]
        output_text += "\n".join(result19) + "\n"
      else:
        if output_text == "":
            break

  # Clear the text widget
  output_text_widget.delete("1.0", tk.END)
  # Insert the output text into the text widget
  output_text_widget.insert("1.0", output_text)


def patient_document_browser():
  filedialog.askopenfilenames(initialdir = patient_document_path, title = (full_name, "-", "Patient Document Browser"))

def sticky_notes_function():
  os.startfile(os.path.normpath("/Georgetown Data/StickyNotes/StickyNotes/" + sticky_note_check + ".pdf"))


"""
def history_and_physical():
  history_and_physical_list = []
  file_names = os.listdir(patient_document_path)

  for files in file_names:
    if "History and Physical-" in files:
      history_and_physical_list.append(files)

  h_p_dates = []

  for h_p_files in history_and_physical_list:
    h_p_dates.append(h_p_files[21:23] + "-" + h_p_files[23:25] + "-" + h_p_files[25:29])

  datetimes = [datetime.strptime(z, "%m-%d-%Y") for z in h_p_dates]
  most_recent_date = max(datetimes)
  formatted_date = most_recent_date.strftime("%m%d%Y")
  date_directory = "History and Physical-" + str(formatted_date) + "-"

  for dates_list in history_and_physical_list:
    if date_directory in dates_list:
      health_and_physical_final_directory = dates_list

  os.startfile(os.path.normpath(patient_document_path + "/" + health_and_physical_final_directory))
  """

def history_and_physical():
  history_and_physical_list = []
  file_names = os.listdir(patient_document_path)
   
  for history_files in file_names:
    if "History and Physical-" in history_files:
      history_and_physical_list.append(history_files)

  for hist_files in history_and_physical_list:
    os.startfile(os.path.normpath(patient_document_path + "/" + hist_files))
  

def immunizations():
  immunizations_list = []
  file_names = os.listdir(patient_document_path)
   
  for immu_files in file_names:
    if "Immunization Records-" in immu_files:
      immunizations_list.append(immu_files)

  for imm_files in immunizations_list:
    os.startfile(os.path.normpath(patient_document_path + "/" + imm_files))

def growth_charts():
  growth_chart_list = []
  file_names = os.listdir(patient_document_path)
   
  for grow_files in file_names:
    if "Growth Charts-" in grow_files:
      growth_chart_list.append(grow_files)

  for gro_files in growth_chart_list:
    os.startfile(os.path.normpath(patient_document_path + "/" + gro_files))

def plan_summary():
  # Get the user's first and last name
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  month = month_entry.get()
  day = day_entry.get()
  year = year_entry.get()
  date_of_birth = str(year + "-" + month + "-" + day)

  # Open the text file and search for the name
  with open("/Georgetown Data/Discrete/Person.txt", "r") as person_file:
    # Read the first line of the file (the header)
    header = person_file.readline().rstrip()
    # Split the header by the '|' character
    header_words = header.split("|")

    # Initialize the output text
    output_text = "BASIC DEMOGRAPHIC INFORMATION:---------------------------------------------------------------BASIC DEMOGRAPHIC INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line in person_file:
      # Split the line by the '|' character
      parts = line.split("|")
      # Check if the first and last name match the line
      if parts[2].lower() == first_name.lower() and parts[5].lower() == last_name.lower() and date_of_birth in parts[10]:
        # Zip the header words and line words together and add them to the output text
          
        if parts[8] == "0": #Suffix ID
          parts[8] = ""
        elif parts[8] == "1":
          parts[8] = "(1) Jr."
        elif parts[8] == "2":
          parts[8] = "(2) Sr."
        elif parts[8] == "3":
          parts[8] = "(3) I"
        elif parts[8] == "4":
          parts[8] = "(4) II"
        elif parts[8] == "5":
          parts[8] = "(5) III"
        elif parts[8] == "6":
          parts[8] = "(6) IV"

        if parts[1] == "0": #Prefix ID
          parts[1] = ""

        if parts[13] == "0":   #Marriage Status
          parts[13] = "(0) Unknown"
        elif parts[13] == "1":
          parts[13] = "(1) Married"
        elif parts[13] == "2":
          parts[13] = "(2) Single"
        elif parts[13] == "3":
          parts[13] = "(3) Widowed"
        elif parts[13] == "4":
          parts[13] = "(4) Divorced"
        elif parts[13] == "5":
          parts[13] = "(5) Seperated"
        elif parts[13] == "6":
          parts[13] = "(6) Other"
        elif parts[13] == "7":
          parts[13] = "(7) Common Law"
        elif parts[13] == "8":
          parts[13] = "(8) Living Together"
        elif parts[13] == "9":
          parts[13] = "(9) Domestic Partner"
        elif parts[13] == "10":
          parts[13] = "(10) Registered Domestic Partner"
        elif parts[13] == "11":
          parts[13] = "(11) Legally Seperated"
        elif parts[13] == "12":
          parts[13] = "(12) Annulled"
        elif parts[13] == "13":
          parts[13] = "(13) Interlocutory"
        elif parts[13] == "14":
          parts[13] = "(14) Unmarried"
        elif parts[13] == "15":
          parts[13] = "(15) Unreported"

        if parts[19] == "1":   #Race ID
          parts[19] = "(1) White"
        elif parts[19] == "2":
          parts[19] = "(2) Black"
        elif parts[19] == "3":
          parts[19] = "(3) Other"
        elif parts[19] == "4":
          parts[19] = "(4) American Indian / Alaska Native"
        elif parts[19] == "5":
          parts[19] = "(5) Asian"
        elif parts[19] == "7":
          parts[19] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts[19] == "8":
          parts[19] = "(8) Declined"

        if parts[12] == "0":   #Gender ID
          parts[12] = "(0) Unknown"
        elif parts[12] == "1":
          parts[12] = "(1) Female"
        elif parts[12] == "2":
          parts[12] = "(2) Male"
        elif parts[12] == "3":
          parts[12] = "(3) Other"
        
        if parts[36] == "0":   #Ethnicity
          parts[36] = "(0) Unknown"
        elif parts[36] == "1":
          parts[36] = "(1) Hispanic or Latino"
        elif parts[36] == "2":
          parts[36] = "(2) Not Hispanic or Latino"
        elif parts[36] == "3":
          parts[36] = "(3) Declined"

        if parts[21] == "0":   #Religion ID
          parts[21] = "(0) Unknown"
        elif parts[21] == "1":
          parts[21] = "(1) Protestant"
        elif parts[21] == "2":
          parts[21] = "(2) Catholic"
        elif parts[21] == "3":
          parts[21] = "(3) Buddhist"
        elif parts[21] == "4":
          parts[21] = "(4) Hindu"
        elif parts[21] == "5":
          parts[21] = "(5) Islam"
        elif parts[21] == "6":
          parts[21] = "(6) Other"
        elif parts[21] == "7":
          parts[21] = "(7) Jewish"
        elif parts[21] == "8":
          parts[21] = "(8) Jehovah's Witness"
        elif parts[21] == "9":
          parts[21] = "(9) Mormon"
        elif parts[21] == "99":
          parts[21] = "(99) N/A"

        if parts[17] == "0":   #Primary Language ID
          parts[17] = "(0) Unknown"
        elif parts[17] == "1":
          parts[17] = "(1) English"
        elif parts[17] == "2":
          parts[17] = "(2) Spanish"
        elif parts[17] == "3":
          parts[17] = "(3) French"
        elif parts[17] == "4":
          parts[17] = "(4) Japanese"
        elif parts[17] == "5":
          parts[17] = "(5) Chinese"
        elif parts[17] == "6":
          parts[17] = "(6) Vietnamese"
        elif parts[17] == "7":
          parts[17] = "(7) Russian"
        elif parts[17] == "8":
          parts[17] = "(8) Arabic"
        elif parts[17] == "9":
          parts[17] = "(9) Filipino"
        elif parts[17] == "10":
          parts[17] = "(10) German"
        elif parts[17] == "11":
          parts[17] = "(11) Greek"
        elif parts[17] == "12":
          parts[17] = "(12) Hindi"
        elif parts[17] == "13":
          parts[17] = "(13) Italian"
        elif parts[17] == "14":
          parts[17] = "(14) Korean"
        elif parts[17] == "15":
          parts[17] = "(15) Polish"
        elif parts[17] == "16":
          parts[17] = "(16) Portuguese"
        elif parts[17] == "17":
          parts[17] = "(17) Other"
        elif parts[17] == "18":
          parts[17] = "(18) Declined"
        else:
          parts[17] = "Other"

        if parts[18] == "0":   #Secondary Language ID
          parts[18] = "(0) Unknown"
        elif parts[18] == "1":
          parts[18] = "(1) English"
        elif parts[18] == "2":
          parts[18] = "(2) Spanish"
        elif parts[18] == "3":
          parts[18] = "(3) French"
        elif parts[18] == "4":
          parts[18] = "(4) Japanese"
        elif parts[18] == "5":
          parts[18] = "(5) Chinese"
        elif parts[18] == "6":
          parts[18] = "(6) Vietnamese"
        elif parts[18] == "7":
          parts[18] = "(7) Russian"
        elif parts[18] == "8":
          parts[18] = "(8) Arabic"
        elif parts[18] == "9":
          parts[18] = "(9) Filipino"
        elif parts[18] == "10":
          parts[18] = "(10) German"
        elif parts[18] == "11":
          parts[18] = "(11) Greek"
        elif parts[18] == "12":
          parts[18] = "(12) Hindi"
        elif parts[18] == "13":
          parts[18] = "(13) Italian"
        elif parts[18] == "14":
          parts[18] = "(14) Korean"
        elif parts[18] == "15":
          parts[18] = "(15) Polish"
        elif parts[18] == "16":
          parts[18] = "(16) Portuguese"
        elif parts[18] == "17":
          parts[18] = "(17) Other"
        elif parts[18] == "18":
          parts[18] = "(18) Declined"
        else:
          parts[18] = "Other"

        if parts[30] == "0":     #Enabled True/False
          parts[30] = "(0) False"
        elif parts[30] == "1":
          parts[30] = "(1) True/Active"

        num_list = [2,3,5,6,10,12,24,26,34,35]
        result = []

        for nums in num_list:
          initial_result = header_words[nums] + ": " + parts[nums]
          result.append(initial_result)

        output_text += "\n".join(result) + "\n"

        patient_id = parts[0]
        address_id = parts[29]
        global full_name
        full_name = parts[2],parts[5]
        global patient_document_path
        patient_document_path = "/Georgetown Data/Docs - Exported/Document/Document/" + patient_id
        global sticky_note_check
        sticky_note_check = "StickyNotes_" + patient_id + "_" + last_name.strip().title() + ", " + first_name.strip().title() + "_" + month + "-" + day + "-" + year
        break
      else:
        pass

  sticky_notes_directory = "/Georgetown Data/StickyNotes/StickyNotes"
  sticky_notes_file_list = os.listdir(sticky_notes_directory)

  for x in sticky_notes_file_list:
    if sticky_note_check in x:
      sticky_notes_label.configure(text = "Sticky Note Found", bg = "SpringGreen2")
      break
    else:
      sticky_notes_label.configure(text = "No Sticky Note Found", bg = "Coral1")
  
  with open("/Georgetown Data/Discrete/Patient.txt", "r") as patient_file:
    # Read the first line of the file (the header)
    header2 = patient_file.readline().rstrip()
    # Split the header by the '|' character
    header_words2 = header2.split("|")

    output_text += "\nPATIENT INFORMATION:---------------------------------------------------------------PATIENT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line2 in patient_file:
      # Split the line by the '|' character
      parts2 = line2.split("|")
      # Check if the first and last name match the line
      if parts2[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        if parts2[13] == "0":     #Enabled True/False
          parts2[13] = "(0) False"
        elif parts2[13] == "1":
          parts2[13] = "(1) True/Active"

        if parts2[14] == "0":     #Is patient True/False
          parts2[14] = "(0) False"
        elif parts2[14] == "1":
          parts2[14] = "(1) True/Active"

        num_list2 = [0,1,8,17,18,21,24]
        result2 = []

        for nums2 in num_list2:
          initial_result2 = header_words2[nums2] + ": " + parts2[nums2]
          result2.append(initial_result2)

        output_text += "\n".join(result2) + "\n"

        care_provider_id = parts2[19]
        break

  with open("/Georgetown Data/Discrete/Address.txt", "r") as address_file:
    # Read the first line of the file (the header)
    header3 = address_file.readline().rstrip()
    # Split the header by the '|' character
    header_words3 = header3.split("|")

    output_text += "\nADDRESS INFORMATION:---------------------------------------------------------------ADDRESS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line3 in address_file:
      # Split the line by the '|' character
      parts3 = line3.split("|")
      # Check if the first and last name match the line
      if parts3[0] == address_id:
        # Zip the header words and line words together and add them to the output text
          

        if parts3[6] == "0":     #Country
          parts3[6] = "(0) Unknown"
        elif parts3[6] == "1":
          parts3[6] = "(1) United States"
        elif parts3[6] == "2":
          parts3[6] = "(2) Mexico"
        elif parts3[6] == "3":
          parts3[6] = "(3) Canada"
        elif parts3[6] == "4":
          parts3[6] = "(4) United States Military"


        result3 = ["{}: {}".format(h, p) for h, p in zip(header_words3, parts3) if p]
        output_text += "\n".join(result3) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Allergy.txt", "r") as allergy_file:
    # Read the first line of the file (the header)
    header4 = allergy_file.readline().rstrip()
    # Split the header by the '|' character
    header_words4 = header4.split("|")

    output_text += "\nALLERGY INFORMATION:---------------------------------------------------------------ALLERGY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line4 in allergy_file:
      # Split the line by the '|' character
      parts4 = line4.split("|")
      # Check if the first and last name match the line
      if parts4[0] == patient_id:
        # Zip the header words and line words together and add them to the output text
          
        result4 = ["{}: {}".format(h, p) for h, p in zip(header_words4, parts4) if p]
        output_text += "\n".join(result4) + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/br_Account.txt", "r") as br_account_file:
    # Read the first line of the file (the header)
    header5 = br_account_file.readline().rstrip()
    # Split the header by the '|' character
    header_words5 = header5.split("|")

    output_text += "\nBASIC ACCOUNT INFORMATION:---------------------------------------------------------------BASIC ACCOUNT INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line5 in br_account_file:
      # Split the line by the '|' character
      parts5 = line5.split("|")
      # Check if the first and last name match the line
      if parts5[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list5 = [9,10,11,12,13,14,18]
        result5 = []

        for nums5 in num_list5:
          initial_result5 = header_words5[nums5] + ": " + parts5[nums5]
          result5.append(initial_result5)

        output_text += "\n".join(result5) + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/ClinicalVital.txt", "r") as clinical_vital_file:
    # Read the first line of the file (the header)
    header6 = clinical_vital_file.readline().rstrip()
    # Split the header by the '|' character
    header_words6 = header6.split("|")

    output_text += "\nCLINICAL VITALS INFORMATION:---------------------------------------------------------------CLINICAL VITALS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line6 in clinical_vital_file:
      # Split the line by the '|' character
      parts6 = line6.split("|")
      # Check if the first and last name match the line
      if parts6[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        if header_words6[3]:
          header_words6[3] = "Temperature (Fahrenheit)"
        if header_words6[4]:
          header_words6[4] = "Height (Inch)"
        if header_words6[5]:
          header_words6[5] = "Weight (Lbs)"
        if header_words6[16]:
          header_words6[16] = "Head Circumference (Inch)"

        if parts6[3]:
          parts6[3] = str((float(parts6[3]) * 9/5) + 32)

        else:
          pass

        if parts6[4]:
          parts6[4] = str((float(parts6[4]) / 2.54))
          height_var = float(parts6[4])
          string_height = str(height_var)
          feet = int(height_var) / 12
          inch = int(height_var) % 12
          final_feet = str(feet)
          final_inch = str(inch)

        else:
          string_height = "00.00"
          final_feet = "0"
          final_inch = "0"

        if parts6[5]:
          parts6[5] = str((float(parts6[5]) / 453.6))

        else:
          pass

        if parts6[16]:
          parts6[16] = str((float(parts6[16]) / 25.4))

        else:
          pass

        result6 = header_words6[2] + ": " + parts6[2] + "\n" + header_words6[3] + ": " + (parts6[3])[0:5] + "\n" + header_words6[4] + ": " + string_height[0:4] + " (" + final_feet[0] + " ft. " + final_inch[0] + "in." + ")" + "\n" + header_words6[5] + ": " + (parts6[5])[0:5] + "\n" + header_words6[6] + ": " + parts6[6] + "\n" + header_words6[8] + ": " + parts6[8]+ "\n" + header_words6[9] + ": " + parts6[9] + "\n" + header_words6[16] + ": " + (parts6[16])[0:5]

        output_text += "".join(result6) + "\n" + '\n'

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/Medications.txt", "r") as medications_file:
    # Read the first line of the file (the header)
    header12 = medications_file.readline().rstrip()
    # Split the header by the '|' character
    header_words12 = header12.split("|")

    output_text += "\nMEDICATIONS INFORMATION:---------------------------------------------------------------MEDICATIONS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line12 in medications_file:
      # Split the line by the '|' character
      parts12 = line12.split("|")
      # Check if the first and last name match the line
      if parts12[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list12 = [3,4,7,11,13,14,15,17,18,19,21,24]
        result12 = []

        for nums12 in num_list12:
          initial_result12 = header_words12[nums12] + ": " + parts12[nums12]
          result12.append(initial_result12)

        output_text += "\n".join(result12) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/NextOfKin.txt", "r") as next_of_kin_file:
    # Read the first line of the file (the header)
    header13 = next_of_kin_file.readline().rstrip()
    # Split the header by the '|' character
    header_words13 = header13.split("|")

    output_text += "\nNEXT OF KIN INFORMATION:---------------------------------------------------------------NEXT OF KIN INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line13 in next_of_kin_file:
      # Split the line by the '|' character
      parts13 = line13.split("|")
      # Check if the first and last name match the line
      if parts13[0] == patient_id and parts13[1] == "Financially Responsible Party":
        # Zip the header words and line words together and add them to the output text

        if parts13[4] == "0":     #Enabled True/False
          parts13[4] = "(0) False"
        elif parts13[4] == "1":
          parts13[4] = "(1) True/Active"

        if parts13[10] == "0": #Prefix ID
          parts13[10] = ""

        if parts13[17] == "0": #Suffix ID
          parts13[17] = ""
        elif parts13[17] == "1":
          parts13[17] = "(1) Jr."
        elif parts13[17] == "2":
          parts13[17] = "(2) Sr."
        elif parts13[17] == "3":
          parts13[17] = "(3) I"
        elif parts13[17] == "4":
          parts13[17] = "(4) II"
        elif parts13[17] == "5":
          parts13[17] = "(5) III"
        elif parts13[17] == "6":
          parts13[17] = "(6) IV"

        if parts13[21] == "0": #Gender ID
          parts13[21] = "Unknown"
        elif parts13[21] == "1":
          parts13[21] = "(1) Female"
        elif parts13[21] == "2":
          parts13[21] = "(2) Male"
        elif parts13[21] == "3":
          parts13[21] = "(3) Other"

        if parts13[22] == "0":   #Marriage Status
          parts13[22] = "(0) Unknown"
        elif parts13[22] == "1":
          parts13[22] = "(1) Married"
        elif parts13[22] == "2":
          parts13[22] = "(2) Single"
        elif parts13[22] == "3":
          parts13[22] = "(3) Widowed"
        elif parts13[22] == "4":
          parts13[22] = "(4) Divorced"
        elif parts13[22] == "5":
          parts13[22] = "(5) Seperated"
        elif parts13[22] == "6":
          parts13[22] = "(6) Other"
        elif parts13[22] == "7":
          parts13[22] = "(7) Common Law"
        elif parts13[22] == "8":
          parts13[22] = "(8) Living Together"
        elif parts13[22] == "9":
          parts13[22] = "(9) Domestic Partner"
        elif parts13[22] == "10":
          parts13[22] = "(10) Registered Domestic Partner"
        elif parts13[22] == "11":
          parts13[22] = "(11) Legally Seperated"
        elif parts13[22] == "12":
          parts13[22] = "(12) Annulled"
        elif parts13[22] == "13":
          parts13[22] = "(13) Interlocutory"
        elif parts13[22] == "14":
          parts13[22] = "(14) Unmarried"
        elif parts13[22] == "15":
          parts13[22] = "(15) Unreported"

        if parts13[26] == "0":   #Primary Language ID
          parts13[26] = "(0) Unknown"
        elif parts13[26] == "1":
          parts13[26] = "(1) English"
        elif parts13[26] == "2":
          parts13[26] = "(2) Spanish"
        elif parts13[26] == "3":
          parts13[26] = "(3) French"
        elif parts13[26] == "4":
          parts13[26] = "(4) Japanese"
        elif parts13[26] == "5":
          parts13[26] = "(5) Chinese"
        elif parts13[26] == "6":
          parts13[26] = "(6) Vietnamese"
        elif parts13[26] == "7":
          parts13[26] = "(7) Russian"
        elif parts13[26] == "8":
          parts13[26] = "(8) Arabic"
        elif parts13[26] == "9":
          parts13[26] = "(9) Filipino"
        elif parts13[26] == "10":
          parts13[26] = "(10) German"
        elif parts13[26] == "11":
          parts13[26] = "(11) Greek"
        elif parts13[26] == "12":
          parts13[26] = "(12) Hindi"
        elif parts13[26] == "13":
          parts13[26] = "(13) Italian"
        elif parts13[26] == "14":
          parts13[26] = "(14) Korean"
        elif parts13[26] == "15":
          parts13[26] = "(15) Polish"
        elif parts13[26] == "16":
          parts13[26] = "(16) Portuguese"
        elif parts13[26] == "17":
          parts13[26] = "(17) Other"
        elif parts13[26] == "18":
          parts13[26] = "(18) Declined"
        else:
          parts13[26] = "Other"

        if parts13[27] == "0":   #Primary Language ID
          parts13[27] = "(0) Unknown"
        elif parts13[27] == "1":
          parts13[27] = "(1) English"
        elif parts13[27] == "2":
          parts13[27] = "(2) Spanish"
        elif parts13[27] == "3":
          parts13[27] = "(3) French"
        elif parts13[27] == "4":
          parts13[27] = "(4) Japanese"
        elif parts13[27] == "5":
          parts13[27] = "(5) Chinese"
        elif parts13[27] == "6":
          parts13[27] = "(6) Vietnamese"
        elif parts13[27] == "7":
          parts13[27] = "(7) Russian"
        elif parts13[27] == "8":
          parts13[27] = "(8) Arabic"
        elif parts13[27] == "9":
          parts13[27] = "(9) Filipino"
        elif parts13[27] == "10":
          parts13[27] = "(10) German"
        elif parts13[27] == "11":
          parts13[27] = "(11) Greek"
        elif parts13[27] == "12":
          parts13[27] = "(12) Hindi"
        elif parts13[27] == "13":
          parts13[27] = "(13) Italian"
        elif parts13[27] == "14":
          parts13[27] = "(14) Korean"
        elif parts13[27] == "15":
          parts13[27] = "(15) Polish"
        elif parts13[27] == "16":
          parts13[27] = "(16) Portuguese"
        elif parts13[27] == "17":
          parts13[27] = "(17) Other"
        elif parts13[27] == "18":
          parts13[27] = "(18) Declined"
        else:
          parts13[27] = "Other"

        if parts13[28] == "1":   #Race ID
          parts13[28] = "(1) White"
        elif parts13[28] == "2":
          parts13[28] = "(2) Black"
        elif parts13[28] == "3":
          parts13[28] = "(3) Other"
        elif parts13[28] == "4":
          parts13[28] = "(4) American Indian / Alaska Native"
        elif parts13[28] == "5":
          parts13[28] = "(5) Asian"
        elif parts13[28] == "7":
          parts13[28] = "(7) Nat Hawaiian / Pacific Islander"
        elif parts13[28] == "8":
          parts13[28] = "(8) Declined"

        if parts13[30] == "0":   #Religion ID
          parts13[30] = "(0) Unknown"
        elif parts13[30] == "1":
          parts13[30] = "(1) Protestant"
        elif parts13[30] == "2":
          parts13[30] = "(2) Catholic"
        elif parts13[30] == "3":
          parts13[30] = "(3) Buddhist"
        elif parts13[30] == "4":
          parts13[30] = "(4) Hindu"
        elif parts13[30] == "5":
          parts13[30] = "(5) Islam"
        elif parts13[30] == "6":
          parts13[30] = "(6) Other"
        elif parts13[30] == "7":
          parts13[30] = "(7) Jewish"
        elif parts13[30] == "8":
          parts13[30] = "(8) Jehovah's Witness"
        elif parts13[30] == "9":
          parts13[30] = "(9) Mormon"
        elif parts13[30] == "99":
          parts13[30] = "(99) N/A"

        if parts13[39] == "0":     #Enabled True/False
          parts13[39] = "(0) False"
        elif parts13[39] == "1":
          parts13[39] = "(1) True/Active"

        if parts13[45] == "0":     #Ethnicity ID
          parts13[45] = "(0) Unknown"
        elif parts13[45] == "1":
          parts13[45] = "(1) Hispanic or Latino"
        elif parts13[45] == "2":
          parts13[45] = "(2) Not Hispanic or Latino"
        elif parts13[45] == "3":
          parts13[45] = "(3) Declined"

        if parts13[61] == "0":     #Country
          parts13[61] = "(0) Unknown"
        elif parts13[61] == "1":
          parts13[61] = "(1) United States"
        elif parts13[61] == "2":
          parts13[61] = "(2) Mexico"
        elif parts13[61] == "3":
          parts13[61] = "(3) Canada"
        elif parts13[61] == "4":
          parts13[61] = "(4) United States Military"


        parts13[2] = ""
        parts13[7] = ""
        parts13[8] = ""

        num_list13 = [1,5,11,14,19,21,33,35,56,58,59,60,62]
        result13 = []

        for nums13 in num_list13:
          initial_result13 = header_words13[nums13] + ": " + parts13[nums13]
          result13.append(initial_result13)

        output_text += "\n".join(result13) + "\n" + "\n"
      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/OrdersDetailTracking.txt", "r") as orders_detail_tracking_file:
    # Read the first line of the file (the header)
    header14 = orders_detail_tracking_file.readline().rstrip()
    # Split the header by the '|' character
    header_words14 = header14.split("|")

    output_text += "\nORDERS DETAIL TRACKING INFORMATION:---------------------------------------------------------------ORDERS DETAIL TRACKING INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line14 in orders_detail_tracking_file:
      # Split the line by the '|' character
      parts14 = line14.split("|")
      # Check if the first and last name match the line
      if parts14[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list14 = [2,3,7,9,13,14,15,17]
        result14 = []

        for nums14 in num_list14:
          initial_result14 = header_words14[nums14] + ": " + parts14[nums14]
          result14.append(initial_result14)

        output_text += "\n".join(result14) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistFamily.txt", "r") as pat_hist_family_file:
    # Read the first line of the file (the header)
    header15 = pat_hist_family_file.readline().rstrip()
    # Split the header by the '|' character
    header_words15 = header15.split("|")

    output_text += "\nFAMILY HISTORY INFORMATION:---------------------------------------------------------------FAMILY HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line15 in pat_hist_family_file:
      # Split the line by the '|' character
      parts15 = line15.split("|")
      # Check if the first and last name match the line
      if parts15[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list15 = [1,3,4,6,7]
        result15 = []

        for nums15 in num_list15:
          initial_result15 = header_words15[nums15] + ": " + parts15[nums15]
          result15.append(initial_result15)

        output_text += "\n".join(result15) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistMedical.txt", "r") as pat_hist_medical_file:
    # Read the first line of the file (the header)
    header16 = pat_hist_medical_file.readline().rstrip()
    # Split the header by the '|' character
    header_words16 = header16.split("|")

    output_text += "\nPAST MEDICAL HISTORY INFORMATION:---------------------------------------------------------------PAST MEDICAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line16 in pat_hist_medical_file:
      # Split the line by the '|' character
      parts16 = line16.split("|")
      # Check if the first and last name match the line
      if parts16[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list16 = [1,2,3,5,7]
        result16 = []

        for nums16 in num_list16:
          initial_result16 = header_words16[nums16] + ": " + parts16[nums16]
          result16.append(initial_result16)

        output_text += "\n".join(result16) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/PatHistSocial.txt", "r") as pat_hist_social_file:
    # Read the first line of the file (the header)
    header17 = pat_hist_social_file.readline().rstrip()
    # Split the header by the '|' character
    header_words17 = header17.split("|")

    output_text += "\nSOCIAL HISTORY INFORMATION:---------------------------------------------------------------SOCIAL HISTORY INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line17 in pat_hist_social_file:
      # Split the line by the '|' character
      parts17 = line17.split("|")
      # Check if the first and last name match the line
      if parts17[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list17 = [1,2,4,5,6,7]
        result17 = []

        for nums17 in num_list17:
          initial_result17 = header_words17[nums17] + ": " + parts17[nums17]
          result17.append(initial_result17)

        output_text += "\n".join(result17) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/ProblemList.txt", "r") as problem_list_file:
    # Read the first line of the file (the header)
    header20 = problem_list_file.readline().rstrip()
    # Split the header by the '|' character
    header_words20 = header20.split("|")

    output_text += "\nPROBLEM LIST INFORMATION:---------------------------------------------------------------PROBLEM LIST INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line20 in problem_list_file:
      # Split the line by the '|' character
      parts20 = line20.split("|")
      # Check if the first and last name match the line
      if parts20[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list20 = [2,5,6]
        result20 = []

        for nums20 in num_list20:
          initial_result20 = header_words20[nums20] + ": " + parts20[nums20]
          result20.append(initial_result20)

        output_text += "\n".join(result20) + "\n" + "\n"

      else:
        if output_text == "":
            break

  with open("/Georgetown Data/Discrete/VacPat.txt", "r") as vac_pat_file:
    # Read the first line of the file (the header)
    header21 = vac_pat_file.readline().rstrip()
    # Split the header by the '|' character
    header_words21 = header21.split("|")

    output_text += "\nIMMUNIZATIONS INFORMATION:---------------------------------------------------------------IMMUNIZATIONS INFORMATION:\n"

    # Search for the name in the remaining lines of the file
    for line21 in vac_pat_file:
      # Split the line by the '|' character
      parts21 = line21.split("|")
      # Check if the first and last name match the line
      if parts21[0] == patient_id:
        # Zip the header words and line words together and add them to the output text

        num_list21 = [2,3,5,6,7,8,9,10]
        result21 = []

        for nums21 in num_list21:
          initial_result21 = header_words21[nums21] + ": " + parts21[nums21]
          result21.append(initial_result21)

        output_text += "\n".join(result21) + "\n" + "\n"

      else:
        if output_text == "":
            break



  # Clear the text widget
  output_text_widget.delete("1.0", tk.END)
  # Insert the output text into the text widget
  output_text_widget.insert("1.0", output_text)




# Create the label and entry widgets for the first name
first_name_label = tk.Label(window, text="First Name:")
first_name_label.configure(bg = "light gray")
first_name_entry = tk.Entry(window)
first_name_entry.configure(bg = "light gray")

# Create the label and entry widgets for the last name
last_name_label = tk.Label(window, text="Last Name:")
last_name_label.configure(bg = "light gray")
last_name_entry = tk.Entry(window)
last_name_entry.configure(bg = "light gray")

month_label = tk.Label(window, text="Month (mm):")
month_label.configure(bg = "light gray")
month_entry = tk.Entry(window)
month_entry.configure(bg = "light gray")

day_label = tk.Label(window, text="Day (dd):")
day_label.configure(bg = "light gray")
day_entry = tk.Entry(window)
day_entry.configure(bg = "light gray")

year_label = tk.Label(window, text="Year (yyyy):")
year_label.configure(bg = "light gray")
year_entry = tk.Entry(window)
year_entry.configure(bg = "light gray")

dob_label = tk.Label(window, text="Date Of Birth:")
dob_label.configure(bg = "light gray")

sticky_notes_label = tk.Label(window, text="STICKY NOTE STATUS")
sticky_notes_label.configure(bg = "Plum1")

# Create the search button
reduced_search_button = tk.Button(window, text="REDUCED\nSEARCH", bg = "#04a777", width = 14, height = 4, bd = 8, 
font = "Helvetica 14 bold", command=reduced_patient_search)

comprehensive_search_button = tk.Button(window, text="COMPREHENSIVE\nSEARCH", bg = "#e86252", width = 14, height = 4, bd = 8, 
font = "Helvetica 14 bold", command=comprehensive_patient_search)

documents_button = tk.Button(window, text="PATIENT \nDOCUMENTS", bg = "#FBB13C", width = 16, height = 3, bd = 8, 
font = "Helvetica 14 bold", command=patient_document_browser)

sticky_notes_button = tk.Button(window, text="OPEN STICKYNOTES", bg = "light gray", width = 16, height = 1, bd = 4, 
font = "Helvetica 7 bold", command= sticky_notes_function)

plan_summary_button = tk.Button(window, text="PLAN\nSUMMARY", bg = "#a83294", width = 10, height = 4, bd = 8, 
font = "Helvetica 14 bold", command= plan_summary) #####################################################

history_and_physical_button = tk.Button(window, text="HISTORY/PHYSICAL", bg = "#a480cf", width = 14, height = 1, bd = 8, 
font = "Helvetica 8 bold", command= history_and_physical) #####################################################

immunizations_button = tk.Button(window, text="IMMUNIZATIONS", bg = "#779be7", width = 14, height = 1, bd = 8, 
font = "Helvetica 8 bold", command= immunizations) #####################################################

growth_chart_button = tk.Button(window, text="GROWTH CHARTS", bg = "#49b6ff", width = 14, height = 1, bd = 8, 
font = "Helvetica 8 bold", command= growth_charts) #####################################################

# Create the text widget for the output
output_text_widget = tk.Text(window)

# Create the scrollbar
scrollbar = tk.Scrollbar(window, orient="vertical", command=output_text_widget.yview)
output_text_widget.configure(yscrollcommand=scrollbar.set, bg = "snow3", font = "Helvetica 12 bold")

# Pack the widgets into the window
first_name_label.place(x=10,y=10)
first_name_entry.place(x=80,y=11)
last_name_label.place(x=11,y=40)
last_name_entry.place(x=80,y=40)
dob_label.place(x=300,y=10)
month_entry.place(x=400,y=40)
month_label.place(x=300,y=40)
day_entry.place(x=400,y=65)
day_label.place(x=324,y=65)
year_entry.place(x=400,y=90)
year_label.place(x=311,y=90)
sticky_notes_label.place(x=10,y=80)
sticky_notes_button.place(x=135,y=80)
reduced_search_button.place(x=900,y=0)
comprehensive_search_button.pack()
documents_button.place(x= 1100, y=8)
plan_summary_button.place(x=560,y=0)
history_and_physical_button.place(x=1350,y=0)
immunizations_button.place(x=1350,y=35)
growth_chart_button.place(x=1350,y=70)
output_text_widget.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the tkinter event loop
window.mainloop()
