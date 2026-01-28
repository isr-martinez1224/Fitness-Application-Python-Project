from tkinter import *

# --------------------- UI SETUP -------------------------#

window = Tk()
window.title("Python Fitness Tracker")
window.config(padx=20, pady=20)

# Canvas/Image setup
canvas = Canvas(width=260, height=260, highlightthickness=0)
logo_img = PhotoImage(file="workout-icon.png")
canvas.create_image(125, 125, image=logo_img)
canvas.grid(column=1, row=2)

title_label = Label(text="Python Fitness App", fg= "#44cfeb", font=("Impact", 35))
title_label.grid(column=1, row=0, sticky="EW")


#View Measurements
def view_measurements():
    pass

view_measurements_button = Button(text="View Measurements", command=view_measurements, highlightthickness=0, bg="#44eb5a")
view_measurements_button.grid(column=1, row=3, sticky="EW")

#Log Off Button - Closes the app
def log_off():
    window.destroy()

exit_button = Button(text="Log Off", command=log_off, highlightthickness=0, bg="red", fg="white")
exit_button.grid(column=1, row=4)



window.mainloop()