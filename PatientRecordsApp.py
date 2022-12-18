#Georgetown Pediatrics Patient Medical Records Application
import os
import tkinter as tk


#file directory for all patient record txt files
text_file_directory = "G:/Georgetown Data/Discrete"

person_file = open("G:/Georgetown Data/Discrete/Person.txt","r")
patient_file = open("G:/Georgetown Data/Discrete/Patient.txt","r")
address_file = open("G:/Georgetown Data/Discrete/Address.txt","r")
allergy_file = open("G:/Georgetown Data/Discrete/Allergy.txt","r")
br_account_file = open("G:/Georgetown Data/Discrete/br_Account.txt","r")
clinical_vital_file = open("G:/Georgetown Data/Discrete/ClinicalVital.txt","r")
flag_file = open("G:/Georgetown Data/Discrete/Flag.txt","r")
ins_coverage_patient_file = open("G:/Georgetown Data/Discrete/InsCoveragePatient.txt","r")
insurance_coverage_file = open("G:/Georgetown Data/Discrete/InsuranceCoverage.txt","r")
insurance_plan_file = open("G:/Georgetown Data/Discrete/InsurancePlan.txt","r")
medications_file = open("G:/Georgetown Data/Discrete/Medications.txt","r")
migration_ins_export_file = open("G:/Georgetown Data/Discrete/MigrationInsExport.txt","r")
migration_proc_export_file = open("G:/Georgetown Data/Discrete/MigrationProcExport.txt","r")
migration_referring_export_file = open("G:/Georgetown Data/Discrete/MigrationReferringExport.txt","r")
migration_schedule_export_file = open("G:/Georgetown Data/Discrete/MigrationScheduleExport.txt","r")
next_of_kin_file = open("G:/Georgetown Data/Discrete/NextOfKin.txt","r")
orders_detail_tracking_file = open("G:/Georgetown Data/Discrete/OrdersDetailTracking.txt","r")
pat_hist_family_file = open("G:/Georgetown Data/Discrete/PatHistFamily.txt","r")
pat_hist_medical_file = open("G:/Georgetown Data/Discrete/PatHistMedical.txt","r")
pat_hist_social_file = open("G:/Georgetown Data/Discrete/PatHistSocial.txt","r")
pat_hist_surgical_file = open("G:/Georgetown Data/Discrete/PatHistSurgical.txt","r")
patient_flags_file = open("G:/Georgetown Data/Discrete/PatientFlags.txt","r")
patient_general_notes_file = open("G:/Georgetown Data/Discrete/PatientGeneralNotes.txt","r")
problem_list_file = open("G:/Georgetown Data/Discrete/ProblemList.txt","r")
vac_pat_file = open("G:/Georgetown Data/Discrete/VacPat.txt","r")

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