import os, csv, shutil, sys
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog  
from datetime import datetime

# Window Elements
win = tk.Tk()
win.title("Physics Assignment Generator")
winWidth = "500"
winLength = "350"
win.geometry('{}x{}'.format(winWidth, winLength))
top_frame = tk.Frame(win, bg='cyan')
center_frame = tk.Frame(win, bg='gray2')
bottom_frame = tk.Frame(win, bg='white')
working_dir = os.getcwd()

top_frame.pack(side = "top", fill = "x")
center_frame.pack()
bottom_frame.pack(side = "bottom", fill = "x")

# Top Frame Elements
tk.Label(top_frame, text = "Physics Assignment Generator").pack(anchor = "center")

# Center frame elements
tk.Label(center_frame, text = "class list csv:").grid(row = 0, column = 0)
csv_path = working_dir + "\\SPH3U1-01_2019_.csv"
classlist_var = tk.StringVar()
classlist = tk.Entry(center_frame, textvariable=classlist_var, bg = "light grey", width = 30).grid(row = 0, column = 1)
classlist_var.set(csv_path)

def populate_classlist(event):
    # Set up the student data and format the directories for student Data
    tk.messagebox.showinfo("Alert", "Select the TeachAssist Classlist")     
    classListPath = filedialog.askopenfilename(initialdir = os.getcwd(), 
                                            title = "Select Class list", 
                                            filetypes = (("CSV files", "*.csv"),
                                                        ("TXT files", "*.txt"), 
                                                        ("All files", "*.*"))  
                                                        )
    classlist_var.set(classListPath)
classlist_button = tk.Button(center_frame, text = "Select Class List")
classlist_button.bind("<Button-1>", populate_classlist)
classlist_button.grid(row = 0, column = 2)

# Temporarily make a Kinematics Generator
kinematic_topics = [["1D Displacement", "2D Displacement", "Average Velocity", 
                    "Instantanious Velocity", "Average Acceleration", "Instantanious Acceleration", 
                    "motion graphs (not working)", "Big 5 Equations", "Projectile Motion"]]
setup_var = [] 
for i in kinematic_topics[0]:
    setup_var.append(tk.IntVar())
kinematic_topics.append(setup_var)

tk.Label(center_frame, text="Kinematics Topics:").grid(row=1, sticky="w")
for i in range(len(kinematic_topics[0])):
    tk.Checkbutton(center_frame, text = kinematic_topics[0][i], variable = kinematic_topics[1][i]).grid(row = 2+ i)

def var_states():
    results = [value.get() for value in kinematic_topics[1]]
    print(results)

# Bottom Frame Elements
tk.Button(bottom_frame, text = "Generate Assessments", command = var_states).pack(anchor = "e")
tk.Button(bottom_frame, text = "Exit")

win.mainloop()