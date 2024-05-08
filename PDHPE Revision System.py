from tkinter import *
from customtkinter import *
root = CTk()
root.title("PDHPE Revision System - First Aid")
root.geometry("500x700")

# Creating Frames to represent different pages

homepage = CTkFrame(root, width = 500, height = 700)
homepage.pack(fill="both", expand = 1)
lessonpage = CTkFrame(root, width = 400, height = 400)
quizpage = CTkFrame(root, width = 400, height = 400)

# different quiz pages
quizpage_1 = CTkFrame(root, width = 400, height = 400)


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
    root.geometry("550x750")

# Switching Pages

def lesson():
    lessonpage.pack(fill="both", expand = 1)
    homepage.pack_forget()
   
def home():
    homepage.pack(fill="both", expand = 1)
    lessonpage.pack_forget()
    quizpage.pack_forget()

def quiz(): 
    quizpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

def begin_quiz_1():
    quizpage.pack_forget()
    quizpage_1.pack(fill="both", expand = 1)




# Widgets for Home Page

title_label = CTkLabel(homepage, text="PDHPE Revision System", font=("Arial", 25))
title_label.place(x=100, y=25)

subtitle_label = CTkLabel(homepage, text="First Aid", font=("Arial", 15))
subtitle_label.place(x=200, y=100)

lesson_button = CTkButton(homepage, width=200, height=100, text="Lesson", command = lesson)
lesson_button.place(x=130, y=150)

quiz_button = CTkButton(homepage, width=200, height=100, text="Quiz", command = quiz)
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

# Widgets for Quiz Page
quizpage_title = CTkLabel(quizpage, text="Quiz List", font=("arial", 25))
quizpage_title.place(x=190, y=25)

quiz_1 = CTkButton(quizpage, width=500, height=100, text="Inquiry Question 1 Quiz", command= begin_quiz_1)
quiz_1.place(x=0, y=200)
quiz_2 = CTkButton(quizpage, width=500, height=100, text="Inquiry Question 2 Quiz")
quiz_2.place(x=0, y=300)
quiz_3 = CTkButton(quizpage, width=500, height=100, text="Inquiry Question 3 Quiz")
quiz_3.place(x=0, y=400) 

# widgets for quiz 1 

# quiz 1 question 1 widgets
question_1_title = CTkLabel(quizpage_1, text = "what is the blah bah")
question_1_title.place(x=0, y=0)

question_1_choice_1 = CTkLabel(quizpage_1, text = "a) the donkey")
question_1_choice_1.place(x=0, y=20)
question_1_choice_2 = CTkLabel(quizpage_1, text = "b) the monkey")
question_1_choice_2.place(x=0, y=40)
question_1_choice_3 = CTkLabel(quizpage_1, text = "c) the wonkey")
question_1_choice_3.place(x=0, y=60)
question_1_choice_4 = CTkLabel(quizpage_1, text = "d) the jonkey")
question_1_choice_4.place(x=0, y=80)

question_1_entry = CTkEntry(quizpage_1, width=100)
question_1_entry.place(x=0, y=105)

# marking quiz 1

def quiz_1_marking():
    score = 0
    if question_1_entry.get() == "a":
        score = score + 1
    quiz_1_result = CTkLabel(quizpage_1, text = ("you got", score))
    quiz_1_result.pack()


question_2_entry = CTkEntry(quizpage_1, width=100)
question_2_entry.place(x=200, y=105)

question_3_entry = CTkEntry(quizpage_1, width=100)
question_3_entry.place(x=400, y=105)

# submit button for quiz 1

quiz_1_submit = CTkButton(quizpage_1, text = "Submit", command = quiz_1_marking)
quiz_1_submit.place(x=350, y=650)





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

