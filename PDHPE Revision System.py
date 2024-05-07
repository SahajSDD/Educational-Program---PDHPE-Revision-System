from tkinter import *
from customtkinter import *
root = CTk()
root.title("PDHPE Revision System - First Aid")
root.geometry("500x700")

# Creating Frames to represent different pages

homepage = CTkFrame(root, width = 500, height = 700)
homepage.pack(fill="both", expand = 1)
lessonpage = CTkFrame(root, width = 400, height = 400)

# commands for size

def small():
    set_widget_scaling(0.75)
    root.minsize(190, 260)
    root.geometry("350x500")

def medium():
    set_widget_scaling(1.0)
    root.minsize(345, 470)
    root.geometry("500x700")

def large():
    set_widget_scaling(1.1)
    root.minsize(470, 630)
    root.geometry("500x750")

# Switching Pages

def lesson():
    lessonpage.pack(fill="both", expand = 1)
    homepage.pack_forget()
   
def home():
    homepage.pack(fill="both", expand = 1)
    lessonpage.pack_forget()
    

# Widgets for Home Page

title_label = CTkLabel(homepage, text="PDHPE Revision System", font=("Arial", 25))
title_label.place(x=100, y=25)

subtitle_label = CTkLabel(homepage, text="First Aid", font=("Arial", 15))
subtitle_label.place(x=200, y=100)

lesson_button = CTkButton(homepage, width=200, height=100, text="Lesson", command = lesson)
lesson_button.place(x=130, y=150)

quiz_button = CTkButton(homepage, width=200, height=100, text="Quiz")
quiz_button.place(x=130, y=300)

scenario_button = CTkButton(homepage, width=200, height=100, text="Scenario")
scenario_button.place(x=130, y=450)

# Widgets for Lesson Page
lessonpage_title = CTkLabel(lessonpage, text="Lesson List", font=("arial", 25))
lessonpage_title.place(x=190, y=25)

lesson_1 = CTkButton(lessonpage, width=500, height=100, text="test")
lesson_1.place(x=0, y=200)
lesson_2 = CTkButton(lessonpage, width=500, height=100, text="test 2")
lesson_2.place(x=0, y=300)
lesson_3 = CTkButton(lessonpage, width=500, height=100, text="test 3")
lesson_3.place(x=0, y=400) 

# menubar

menubar = Menu(root)
root.configure(menu=menubar)

menuhome = Menu(menubar, tearoff = 0)
menusize = Menu(menubar, tearoff =0)
menutheme = Menu(menubar, tearoff = 0)
menutranslate = Menu(menubar, tearoff = 0)

menubar.add_cascade(label="Home", menu=menuhome)
menubar.add_cascade(label="Size", menu=menusize)
menubar.add_cascade(label="Theme", menu=menutheme)
menubar.add_cascade(label="Translate", menu=menutranslate)

# dropdowns for menubars

menuhome.add_cascade(label="Home", command = home)
menusize.add_command(label = "Small", command = small)
menusize.add_command(label = "Medium", command = medium)
menusize.add_command(label = "Large", command = large)

menutheme.add_command(label = "Dark", command=lambda: set_appearance_mode("dark"))
menutheme.add_command(label = "Light", command=lambda: set_appearance_mode("light"))

root.resizable(height=False, width=False)

root.mainloop()

