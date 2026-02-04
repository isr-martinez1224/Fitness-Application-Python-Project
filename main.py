from tkinter import *
from PIL import Image, ImageTk
import json

# --------------------- CONSTANTS -------------------------#
USER_DATA_FILE = "./data/fitness_data.json"

# --------------------- UI SETUP -------------------------#

window = Tk()
window.title("Python Fitness Tracker")
#window.geometry("450x350")
window.minsize(height=450, width=350)

# Make window expandable - this makes the window adapt to changing sizes
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ---- frames (screens) ----
main_menu = Frame(window, bg="lightblue")
frame2 = Frame(window, bg="lightgreen")
frame3 = Frame(window, bg="lightcoral")

for frame in (main_menu, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# ---- screen switch function ----
def show_frame(frame):
    frame.tkraise()

# ---- menu bar ----
menubar = Menu(window)
window.config(menu=menubar)

menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Screens", menu=menu)

menu.add_command(label="Go to Screen 1", command=lambda: show_frame(main_menu))
menu.add_command(label="Go to Screen 2", command=lambda: show_frame(frame2))
menu.add_command(label="Go to Screen 3", command=lambda: show_frame(frame3))




# ---- MAIN MENU WIDGETS ----
Label(main_menu, text="Python Fitness Tracker", font=("Impact", 35), bg="lightblue", fg= "white").grid(column=1, row=0, sticky="nsew")
#Button(main_menu, text="Go to Screen 2",command=lambda: show_frame(frame2)).grid(column=1, row=2)

#Picture on main menu
menu_img = ImageTk.PhotoImage(Image.open("workout-icon.png"))
menu_image_label = Label(main_menu, image=menu_img, bg="lightblue")
menu_image_label.image = menu_img
menu_image_label.grid(row=1, column=1, sticky="nsew")


#View Measurements
def view_measurements():
    pass

view_measurements_button = Button(main_menu, text="View Measurements", command=view_measurements, highlightthickness=0, bg="#44cfeb")
view_measurements_button.grid(column=1, row=3)

#Log Off Button - Closes the app
def log_off():
    window.destroy()

exit_button = Button(main_menu, text="Log Off", command=log_off, highlightthickness=0, bg="red", fg="white")
exit_button.grid(column=1, row=4)



########################################################

Label(frame2, text="Welcome to Screen 2", font=("Arial", 16)).grid(column=1, row=0, sticky="nsew")
Button(frame2, text="Go to Screen 3",command=lambda: show_frame(frame3)).grid(column=1, row=2, sticky="nsew")

Label(frame3, text="Welcome to Screen 3", font=("Arial", 16)).grid(column=1, row=0, sticky="nsew")
Button(frame3, text="Go to Screen 1",command=lambda: show_frame(main_menu)).grid(column=1, row=2, sticky="nsew")







main_menu.grid_rowconfigure(0, weight=1)
main_menu.grid_rowconfigure(1, weight=1)
main_menu.grid_rowconfigure(2, weight=1)
main_menu.grid_rowconfigure(3, weight=1)
main_menu.grid_rowconfigure(4, weight=1)
main_menu.grid_columnconfigure(1, weight=1)

# ---- start on frame 1 ----
show_frame(main_menu)

window.mainloop()







new_data = {
        "DATE": {
            "Weight": 180,
            "Waist Circumfurence": 37,
        }
    }
try:
    with open(USER_DATA_FILE, mode="r") as file:
        #Read old data
        data = json.load(file)
except FileNotFoundError:
    with open(USER_DATA_FILE, mode="w") as file:
        json.dump(new_data, file, indent=4)
else:
    #Update old data with new data
    data.update(new_data)

    with open(USER_DATA_FILE, mode="w") as file:
        #Saving updated data
        json.dump(data, file, indent=4)
