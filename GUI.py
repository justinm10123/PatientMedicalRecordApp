import tkinter as tk

#initializing the window
main = tk.Tk()

#window size
main.geometry("600x338")

#window title
main.title("Patient Records Search")
main.configure(bg = "dark slate gray")


def printInput():
    text_input = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: " + text_input)
  
inputtxt = tk.Text(main, height = 3, width = 10, bg= "light grey")
  
inputtxt.pack()
  
# Button Creation
printButton = tk.Button(main,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = tk.Label(main, text = "")
lbl.pack()

exit_button = tk.Button(main, text = "Exit", width = 10, height = 3, bg = "grey", activebackground = "dark slate gray", bd = 6, command = main.destroy)
exit_button.pack()



main.mainloop()