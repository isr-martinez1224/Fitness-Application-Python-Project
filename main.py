from tkinter import *

# --------------------- UI SETUP -------------------------#

window = Tk()
window.title("Python Fitness Tracker")
window.minsize(width=600, height=450)
window.config(padx=20, pady=20)

# canvas = Canvas(width=600, height=450, highlightthickness=0)
# canvas_text = canvas.create_text(300, 75, text="Python Fitness App", fill="blue", font=("Impact", 25, "bold"))
# canvas.grid()

title_label = Label(text="Python Fitness App", fg= "blue", font=("Impact", 35))
title_label.grid(column=1, row=0)

def log_off():
    pass

exit_button = Button(text="Log Off", command=log_off, highlightthickness=0)
exit_button.grid(column=1, row=3)




window.mainloop()