import tkinter as tk

#initializing the window
main = tk.Tk()

#window size
main.geometry("1500x1000")

#window title
main.title("Patient Records Search")
main.configure(bg = "dark slate gray")

canvas = tk.Canvas(main, bg = "dark slate gray")
scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)

canvas.pack(side="right", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

for i in range(50):
    tk.Label(frame, text="This is a label {}".format(i), bg = "light grey").pack()

frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))


def printInput():
    first_name_input = first_inputtxt.get(1.0, "end-1c")
    last_name_input = last_inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Patient Name Entered: \n" + first_name_input + " " + last_name_input)
  
first_inputtxt = tk.Text(main, height = 2, width = 20, bg= "light grey")
last_inputtxt = tk.Text(main, height = 2, width = 20, bg= "light grey")

first_inputtxt.pack(anchor = tk.NW)
last_inputtxt.pack(anchor = tk.NW)
  
# Button Creation
printButton = tk.Button(main, text = "Search", command = printInput, bg = "grey", activebackground="dark slate gray", bd = 3)
printButton.pack(anchor = tk.NW)
  
# Label Creation
lbl = tk.Label(main, text = "Patient Name Entered: \n", bg = "light grey")
lbl.pack(anchor = tk.NW)

exit_button = tk.Button(main, text = "Exit", width = 10, height = 3, bg = "grey", activebackground = "dark slate gray", bd = 6, command = main.destroy)
exit_button.pack(anchor = tk.NW)


################################## Label Grid Creation #######################
person_id = tk.Label(main, text = "Person ID: \n", bg = "light grey").pack()############################ PERSON FILE

last_name = tk.Label(main, text = "Last Name: \n", bg = "light grey")
last_name.pack()

first_name = tk.Label(main, text = "First Name: \n", bg = "light grey")
first_name.pack()

middle_name_1 = tk.Label(main, text = "Middle Name 1: \n", bg = "light grey")
middle_name_1.pack()

nickname = tk.Label(main, text = "Nickname: \n", bg = "light grey")
nickname.pack()

date_of_birth = tk.Label(main, text = "Date Of Birth: \n", bg = "light grey")
date_of_birth.pack()

cell_phone_1 = tk.Label(main, text = "Cell Phone 1: \n", bg = "light grey")
cell_phone_1.pack()

last_name = tk.Label(main, text = "Last Name: \n", bg = "light grey")
last_name.pack()

email_1 = tk.Label(main, text = "Email 1: \n", bg = "light grey")
email_1.pack()

residential_address_id = tk.Label(main, text = "Residential Address ID: \n", bg = "light grey")
residential_address_id.pack()

billing_address_id = tk.Label(main, text = "Billing Address ID: \n", bg = "light grey")
billing_address_id.pack()

primary_phone = tk.Label(main, text = "Primary Phone: \n", bg = "light grey")
primary_phone.pack()

sexual_orientation_id = tk.Label(main, text = "Sexual Orientation ID: \n", bg = "light grey")
sexual_orientation_id.pack()

sexual_orientation_other = tk.Label(main, text = "Sexual Orientation Other: \n", bg = "light grey")
sexual_orientation_other.pack()

gender_identity_id = tk.Label(main, text = "Gender Identity ID: \n", bg = "light grey")
gender_identity_id.pack()

gender_identity_other = tk.Label(main, text = "Gender Identity Other: \n", bg = "light grey")
gender_identity_other.pack()

birth_sex_id = tk.Label(main, text = "Birth Sex ID: \n", bg = "light grey")
birth_sex_id.pack()

prefix_id = tk.Label(main, text = "Prefix ID: \n", bg = "light grey")
prefix_id.pack()

middle_name_2 = tk.Label(main, text = "Middle Name 2: \n", bg = "light grey")
middle_name_2.pack()

maiden_name = tk.Label(main, text = "Maiden Name: \n", bg = "light grey")
maiden_name.pack()

suffix_id = tk.Label(main, text = "Suffix ID: \n", bg = "light grey")
suffix_id.pack()

ssn = tk.Label(main, text = "SSN: \n", bg = "light grey")
ssn.pack()

birth_place = tk.Label(main, text = "Birth Place: \n", bg = "light grey")
birth_place.pack()

gender_id = tk.Label(main, text = "Gender ID: \n", bg = "light grey")
gender_id.pack()

marital_status_id = tk.Label(main, text = "Marital Status ID: \n", bg = "light grey")
marital_status_id.pack()


main.mainloop()