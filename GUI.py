import tkinter as tk

#initializing the window
main = tk.Tk()

#window size
main.geometry("1500x1000")

#window title
main.title("Patient Records Search")
main.configure(bg = "dark slate gray")


def printInput():
    text_input = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Patient Name Entered: \n" + text_input)
  
inputtxt = tk.Text(main, height = 2, width = 20, bg= "light grey")
  
inputtxt.pack(anchor = tk.NW)
  
# Button Creation
printButton = tk.Button(main, text = "Search", command = printInput, bg = "grey", activebackground="dark slate gray", bd = 3)
printButton.pack(anchor = tk.NW)
  
# Label Creation
lbl = tk.Label(main, text = "Please Enter a First and Last name \n in the text box above.", bg = "light grey")
lbl.pack(anchor = tk.NW)

exit_button = tk.Button(main, text = "Exit", width = 10, height = 3, bg = "grey", activebackground = "dark slate gray", bd = 6, command = main.destroy)
exit_button.pack(anchor = tk.NW)



main.mainloop()