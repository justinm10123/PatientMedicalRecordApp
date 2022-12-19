#Georgetown Pediatrics Patient Medical Records Application
import os
import tkinter as tk

# ALL INITIAL FILE DIRECORIES WILL NEED TO CHANGE WHEN HAND OFF HARD DRIVE IS CREATED #
person_file = open("G:/Georgetown Data/Discrete/Person.txt","r") #done
patient_file = open("G:/Georgetown Data/Discrete/Patient.txt","r") #done
address_file = open("G:/Georgetown Data/Discrete/Address.txt","r") #done
allergy_file = open("G:/Georgetown Data/Discrete/Allergy.txt","r") #done
br_account_file = open("G:/Georgetown Data/Discrete/br_Account.txt","r") #done
clinical_vital_file = open("G:/Georgetown Data/Discrete/ClinicalVital.txt","r") #done
flag_file = open("G:/Georgetown Data/Discrete/Flag.txt","r") #dont think this is needed, only contains flag id/translations
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
patient_flags_file = open("G:/Georgetown Data/Discrete/PatientFlags.txt","r") #done
patient_general_notes_file = open("G:/Georgetown Data/Discrete/PatientGeneralNotes.txt","r")
problem_list_file = open("G:/Georgetown Data/Discrete/ProblemList.txt","r")
vac_pat_file = open("G:/Georgetown Data/Discrete/VacPat.txt","r")



search_term = input("Enter a Patient ID # or First and Last name: ")
split_search_term = search_term.split()

patient_id = ""

  # Read the rest of the lines in the file
for line in person_file:
    # Split the line into a list of words
    words = line.split("|")
    
    if (words[2].lower() == split_search_term[0].lower() and words[5].lower() == split_search_term[1].lower()) or (words[0].lower() == search_term.lower()):
      split_person_line = line.split("|")

      #assigning array 0 of person.txt line files to the patient id
      patient_id = split_person_line[0]
      address_id = split_person_line[29]

      #testing print statements, wont need in final code
      print("\n", split_person_line)
      print("\n", "Patient ID: ", patient_id)

for line1 in patient_file:
    words1 = line1.split("|")

    if words1[1] == patient_id:
        print("\n", line1)

for line2 in address_file:
    words2 = line2.split("|")

    if words2[0] == address_id:
        print("\n", line2)

for line3 in allergy_file:
    words3 = line3.split("|")

    if words3[0] == patient_id:
        print("\n", line3)

for line4 in br_account_file:
    words4 = line4.split("|")

    if words4[0] == patient_id:
        print("\n", line4)

for line5 in clinical_vital_file:
    words5 = line5.split("|")

    if words5[0] == patient_id:
        print("\n", line5)

for line6 in patient_flags_file:
    words6 = line6.split("|")

    if words6[0] == patient_id:
        print("\n", line6)

for line7 in insurance_coverage_file:
    words7 = line7.split("|")

    if words7[1] == patient_id:
        print("\n", line7)

        #consider using a loop to create an array and append each plan id to the array
        insurance_plan_id = [words7[2]]
        print(insurance_plan_id) # may have multiple insurance plan id's and will need to include them all

for line8 in insurance_plan_file:
    words8 = line8.split("|")

    if words8[0] == insurance_plan_id: # will probably need to use array to check each plan id and pull info
        print("\n", line8)