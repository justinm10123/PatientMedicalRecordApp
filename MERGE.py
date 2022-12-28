import os
import tkinter as tk
from tkinter import filedialog

# Create the tkinter window
window = tk.Tk()
window.title("Patient Records Search")
window.configure(bg = "dark slate gray")
window.geometry("1500x1000")

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
      if parts13[0] == patient_id and parts13[1] == "Financially Responsible Party":
        # Zip the header words and line words together and add them to the output text
        result13 = ["{}: {}".format(h, p) for h, p in zip(header_words13, parts13)] ###################### Maybe only include financially responsible party???
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
          parts[8] = "Jr."
        elif parts[8] == "2":
          parts[8] = "Sr."
        elif parts[8] == "3":
          parts[8] = "I"
        elif parts[8] == "4":
          parts[8] = "II"
        elif parts[8] == "5":
          parts[8] = "III"
        elif parts[8] == "6":
          parts[8] = "IV"

        if parts[1] == "0": #Prefix ID
          parts[1] = ""

        if parts[13] == "0":   #Marriage Status
          parts[13] = "Unknown"
        elif parts[13] == "1":
          parts[13] = "Married"
        elif parts[13] == "2":
          parts[13] = "Single"
        elif parts[13] == "3":
          parts[13] = "Widowed"
        elif parts[13] == "4":
          parts[13] = "Divorced"
        elif parts[13] == "5":
          parts[13] = "Seperated"
        elif parts[13] == "6":
          parts[13] = "Other"
        elif parts[13] == "7":
          parts[13] = "Common Law"
        elif parts[13] == "8":
          parts[13] = "Living Together"
        elif parts[13] == "9":
          parts[13] = "Domestic Partner"
        elif parts[13] == "10":
          parts[13] = "Registered Domestic Partner"
        elif parts[13] == "11":
          parts[13] = "Legally Seperated"
        elif parts[13] == "12":
          parts[13] = "Annulled"
        elif parts[13] == "13":
          parts[13] = "Interlocutory"
        elif parts[13] == "14":
          parts[13] = "Unmarried"
        elif parts[13] == "15":
          parts[13] = "Unreported"

        if parts[19] == "1":   #Race ID
          parts[19] = "White"
        elif parts[19] == "2":
          parts[19] = "Black"
        elif parts[19] == "3":
          parts[19] = "Other"
        elif parts[19] == "4":
          parts[19] = "American Indian / Alaska Native"
        elif parts[19] == "5":
          parts[19] = "Asian"
        elif parts[19] == "7":
          parts[19] = "Nat Hawaiian / Pacific Islander"
        elif parts[19] == "8":
          parts[19] = "Declined"

        if parts[12] == "0":   #Gender ID
          parts[12] = "Unknown"
        elif parts[12] == "1":
          parts[12] = "Female"
        elif parts[12] == "2":
          parts[12] = "Male"
        elif parts[12] == "3":
          parts[12] = "Other"


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

  # Clear the text widget
  output_text_widget.delete("1.0", tk.END)
  # Insert the output text into the text widget
  output_text_widget.insert("1.0", output_text)


def patient_document_browser():
  filedialog.askopenfilenames(initialdir = patient_document_path, title = (full_name, "-", "Patient Document Browser"))

def sticky_notes_function():
  os.startfile(os.path.normpath("/Georgetown Data/StickyNotes/StickyNotes/" + sticky_note_check + ".pdf"))

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
reduced_search_button = tk.Button(window, text="REDUCED\nSEARCH", bg = "light gray", width = 14, height = 4, bd = 8, 
font = "Helvetica 14 bold", command=reduced_patient_search)

comprehensive_search_button = tk.Button(window, text="COMPREHENSIVE\nSEARCH", bg = "light gray", width = 14, height = 4, bd = 8, 
font = "Helvetica 14 bold", command=comprehensive_patient_search)

documents_button = tk.Button(window, text="PATIENT DOCUMENTS", bg = "light gray", width = 18, height = 3, bd = 8, 
font = "Helvetica 14 bold", command=patient_document_browser)

sticky_notes_button = tk.Button(window, text="OPEN STICKYNOTES", bg = "light gray", width = 16, height = 1, bd = 4, 
font = "Helvetica 7 bold", command= sticky_notes_function)

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
documents_button.place(x= 1200, y=8)
output_text_widget.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the tkinter event loop
window.mainloop()
