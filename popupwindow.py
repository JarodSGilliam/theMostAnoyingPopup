#Imports
import sys
import tkinter as tk

#Error checking
if len(sys.argv) > 2:
    sys.exit("Error: Too many command line arguments!")
elif len(sys.argv) < 2:
    sys.exit("Error: Include in the command what you want the popup to say!")

#Creating the window
window = tk.Tk()
window.minsize(1000, 900)
greetings = tk.Label(text = sys.argv[1], font=("Arial", 25))
greetings.place(y=390, x=500, anchor="center")
button = tk.Button(text = "Task has been completed!", command=window.destroy, font=("Arial", 11))
button.place(y=460, x=500, anchor="center")

#Displaying the window
window.mainloop()
