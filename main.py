from tkinter import *
from PIL import Image, ImageTk
import json
from userdata_sql import SQL_Access
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from datetime import datetime


# --------------------- UI SETUP -------------------------#

window = Tk()
window.title("Python Fitness Tracker")
window.minsize(height=650, width=550)

# Make window expandable - this makes the window adapt to changing sizes
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# ---- frames (screens) ---- possibly each frame can be its own class here?
main_menu = Frame(window, bg="lightblue")
weight_frame = Frame(window, bg="lightgreen")
circumference_frame = Frame(window, bg="lightcoral")

for frame in (main_menu, weight_frame, circumference_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# ---- screen switch function ----
def show_frame(frame):
    frame.tkraise()

# ---- MAIN MENU WIDGETS ----
Label(main_menu, text="Python Fitness Tracker", font=("Impact", 35), bg="lightblue", fg= "white").grid(column=1, row=0, sticky="nsew")

#Picture on main menu
menu_img = ImageTk.PhotoImage(Image.open("workout-icon.png"))
menu_image_label = Label(main_menu, image=menu_img, bg="lightblue")
menu_image_label.image = menu_img
menu_image_label.grid(row=1, column=1, sticky="nsew")


# Variable to keep track of the options selected in OptionMenu
value_inside = StringVar(window)

# Set the default value of the variable
value_inside.set("View Measurements - Select Here")

# Create the list of options
options_list = [None, "Weight", "Waist Circumference"]

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
view_measurements_menu = OptionMenu(main_menu, value_inside, *options_list)
view_measurements_menu.grid(column=1, row=3)

# Function to get the choice and switch screens/frames
def menu_options():
    choice = value_inside.get()
    if choice == "Weight":
        show_frame(weight_frame)
    elif choice == "Waist Circumference":
        show_frame(circumference_frame)
    else:
        pass

# Submit button
# Whenever we click the submit button, our submitted option is sent to menu options function
submit_button = Button(main_menu, text='Submit', command=menu_options)
submit_button.grid(column=1, row=4)

#Log Off Button - Closes the app
def log_off():
    window.destroy()

exit_button = Button(main_menu, text="Log Off", command=log_off, highlightthickness=0, bg="red", fg="white")
exit_button.grid(column=1, row=5)



#WINDOW CONFIGURATIONS FOR LAYOUTS - NEED TO ADD FOR EVERY FRAME?
main_menu.grid_rowconfigure(0, weight=1)
main_menu.grid_rowconfigure(1, weight=1)
main_menu.grid_rowconfigure(2, weight=1)
main_menu.grid_rowconfigure(3, weight=1)
main_menu.grid_rowconfigure(4, weight=1)
main_menu.grid_columnconfigure(1, weight=1)
################################################################################################

################################################################################################

# WEIGHT FRAME MENU

sql = SQL_Access()

def insert_weight():
    sql.insert_weight(date_input.get(), weight_input.get())
    date_input.delete(0, END)
    weight_input.delete(0, END)

#WEIGHT FRAME LAYOUT
Label(weight_frame, text="Weight Measurements", font=("Impact", 25), bg="lightgreen", fg="white").grid(column=1, row=0, sticky="nsew", columnspan=2)
Button(weight_frame, text="Add Measurements", command=insert_weight).grid(column=1, row=2, sticky="es")

weight_input = Entry(weight_frame)
weight_input.grid(column=1, row=3, sticky="nw")
weight_input_label = Label(weight_frame, text="Weight (lbs):")
weight_input_label.grid(column=0, row=3, sticky="ne")

date_input = Entry(weight_frame)
date_input.grid(column=1, row=4, sticky="nw")
date_input_label = Label(weight_frame, text="Date (YYYY/MM/DD):")
date_input_label.grid(column=0, row=4, sticky="ne")

Button(weight_frame, text="Edit Measurements").grid(column=2, row=2, sticky="ws")
Button(weight_frame, text="Return to Main Menu", command=lambda: show_frame(main_menu)).grid(column=1, row=5, columnspan=2)


####################### TESTING ADDING A GRAPH

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)

dates = []
weight_values = []
data = sql.get_data()

for row in data:
    date_str = row[0]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    dates.append(date_obj)

    weight_values.append(row[1])

line, = ax.plot(dates, weight_values, linestyle='-', marker='o', color='blue', markersize=6)

ax.set_ylabel("Weight(lbs)")
ax.set_xticks(dates)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
fig.autofmt_xdate()  # Rotate date labels


canvas = FigureCanvasTkAgg(fig, master=weight_frame)
canvas.draw()
canvas.get_tk_widget().grid(column=1, row=1, columnspan=2)


# #Updating the graph
# #save this when first plotting the graph
# line, = ax.plot(dates, values)
#
# #when you want to update
# # dates.append(datetime(2025, 10, 4))
# # values.append(25)
#
# line.set_data(dates, values)
#
# ax.relim()          # Recalculate limits
# ax.autoscale_view() # Rescale axes
# canvas.draw()





#WINDOW CONFIGURATIONS FOR LAYOUTS - NEED TO ADD FOR EVERY FRAME?
weight_frame.grid_rowconfigure(0, weight=1)
weight_frame.grid_rowconfigure(1, weight=1)
weight_frame.grid_rowconfigure(2, weight=1)
weight_frame.grid_rowconfigure(3, weight=1)
weight_frame.grid_rowconfigure(4, weight=1)
weight_frame.grid_rowconfigure(5, weight=1)
weight_frame.grid_columnconfigure(0, weight=1)
weight_frame.grid_columnconfigure(1, weight=1)
weight_frame.grid_columnconfigure(2, weight=1)

###################################################################################
###################################################################################

#WAIST CIRCUMFERENCE MENU


Label(circumference_frame, text="Waist Circumfurence Measurements", font=("Arial", 16)).grid(column=1, row=0, sticky="nsew")
Button(circumference_frame, text="Return to Main Menu", command=lambda: show_frame(main_menu)).grid(column=1, row=2, sticky="nsew")



# waist_input = Entry(weight_frame)
# waist_input.grid(column=1, row=3, sticky="ne")
# waist_input_label = Label(weight_frame, text="Waist Circumference:")
# waist_input_label.grid(column=0, row=3, sticky="ne")





# ---- start on frame 1 ----
show_frame(main_menu)

window.mainloop()

