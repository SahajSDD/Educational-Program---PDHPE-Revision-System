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
quizpage_2 = CTkFrame(root, width = 400, height = 400)
quizpage_3 = CTkFrame(root, width = 400, height = 400)


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
    quizpage_1.pack_forget()
    quizpage_2.pack_forget()
    quizpage_3.pack_forget()

def quiz(): 
    quizpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

def begin_quiz_1():
    quizpage.pack_forget()
    quizpage_1.pack(fill="both", expand = 1)

def begin_quiz_2():
    quizpage.pack_forget()
    quizpage_2.pack(fill="both", expand = 1)

def begin_quiz_3():
    quizpage.pack_forget()
    quizpage_3.pack(fill="both", expand = 1)




# Widgets for Home Page

title_label = CTkLabel(homepage, text="PDHPE Revision System", font=("Arial bold", 25))
title_label.place(x=100, y=25)

subtitle_label = CTkLabel(homepage, text="First Aid", font=("Arial italic", 15))
subtitle_label.place(x=200, y=100)

lesson_button = CTkButton(homepage, width=200, height=100, text="Lesson", font=("Arial bold", 15), command = lesson)
lesson_button.place(x=130, y=150)

quiz_button = CTkButton(homepage, width=200, height=100, text="Quiz", font=("Arial bold", 15), command = quiz)
quiz_button.place(x=130, y=300)

scenario_button = CTkButton(homepage, width=200, height=100, text="Scenario", font=("Arial bold", 15))
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
quiz_2 = CTkButton(quizpage, width=500, height=100, text="Inquiry Question 2 Quiz", command= begin_quiz_2)
quiz_2.place(x=0, y=300)
quiz_3 = CTkButton(quizpage, width=500, height=100, text="Inquiry Question 3 Quiz", command= begin_quiz_3)
quiz_3.place(x=0, y=400) 

# widgets for quiz 1 

# quiz 1 question 1 widgets
quiz_1_question_1_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_1_title.place(x=0, y=10)

quiz_1_question_1_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_1_entry.place(x=5, y=105)

# quiz 1 question 2 widgets
quiz_1_question_2_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_2_title.place(x=175, y=10)

quiz_1_question_2_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_2_entry.place(x=180, y=105)

# quiz 1 question 3 widgets
quiz_1_question_3_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_3_title.place(x=350, y=10)

quiz_1_question_3_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_3_entry.place(x=355, y=105)

# quiz 1 question 4 widgets
quiz_1_question_4_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_4_title.place(x=0, y=200)

quiz_1_question_4_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_4_entry.place(x=5, y=295)

# quiz 1 question 5 widgets
quiz_1_question_5_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_5_title.place(x=175, y=200)

quiz_1_question_5_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_5_entry.place(x=180, y=295)

# quiz 1 question 6 widgets
quiz_1_question_6_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_6_title.place(x=350, y=200)

quiz_1_question_6_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_6_entry.place(x=355, y=295)

# quiz 1 question 7 widgets
quiz_1_question_7_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_7_title.place(x=0, y=390)

quiz_1_question_7_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_7_entry.place(x=10, y=485)

# quiz 1 question 8 widgets
quiz_1_question_8_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_8_title.place(x=175, y=390)

quiz_1_question_8_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_8_entry.place(x=180, y=485)

# quiz 1 question 9 widgets
quiz_1_question_9_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_9_title.place(x=350, y=390)

quiz_1_question_9_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_9_entry.place(x=355, y=485)

# quiz 1 question 10 widgets
quiz_1_question_10_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_10_title.place(x=0, y=550)

quiz_1_question_10_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_10_entry.place(x=10, y=645)

# marking quiz 1

def quiz_1_marking():
    score = 0
    if quiz_1_question_1_entry.get() == "a":
        score = score + 1
    if quiz_1_question_2_entry.get() == "a":
        score = score + 1
    if quiz_1_question_3_entry.get() == "a":
        score = score + 1
    if quiz_1_question_4_entry.get() == "a":
        score = score + 1
    if quiz_1_question_5_entry.get() == "a":
        score = score + 1
    if quiz_1_question_6_entry.get() == "a":
        score = score + 1
    if quiz_1_question_7_entry.get() == "a":
        score = score + 1
    if quiz_1_question_8_entry.get() == "a":
        score = score + 1
    if quiz_1_question_9_entry.get() == "a":
        score = score + 1
    if quiz_1_question_10_entry.get() == "a":
        score = score + 1
    quiz_1_result = CTkLabel(quizpage_1, text = f"Your Score is : {score}", font=("arial", 25), bg_color = "green")
    quiz_1_result.place(x=220, y=545)

# submit button for quiz 1

quiz_1_submit = CTkButton(quizpage_1, text = "Submit", command = quiz_1_marking)
quiz_1_submit.place(x=350, y=650)

# widgets for quiz 2


# quiz 2 question 1 widgets
quiz_2_question_1_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_1_title.place(x=0, y=10)


quiz_2_question_1_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_1_entry.place(x=5, y=105)


# quiz 2 question 2 widgets
quiz_2_question_2_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_2_title.place(x=175, y=10)


quiz_2_question_2_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_2_entry.place(x=180, y=105)


# quiz 2 question 3 widgets
quiz_2_question_3_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_3_title.place(x=350, y=10)


quiz_2_question_3_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_3_entry.place(x=355, y=105)


# quiz 2 question 4 widgets
quiz_2_question_4_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_4_title.place(x=0, y=200)


quiz_2_question_4_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_4_entry.place(x=5, y=295)


# quiz 2 question 5 widgets
quiz_2_question_5_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_5_title.place(x=175, y=200)


quiz_2_question_5_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_5_entry.place(x=180, y=295)


# quiz 2 question 6 widgets
quiz_2_question_6_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_6_title.place(x=350, y=200)


quiz_2_question_6_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_6_entry.place(x=355, y=295)


# quiz 2 question 7 widgets
quiz_2_question_7_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_7_title.place(x=0, y=390)


quiz_2_question_7_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_7_entry.place(x=10, y=485)


# quiz 2 question 8 widgets
quiz_2_question_8_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_8_title.place(x=175, y=390)


quiz_2_question_8_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_8_entry.place(x=180, y=485)


# quiz 2 question 9 widgets
quiz_2_question_9_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_9_title.place(x=350, y=390)


quiz_2_question_9_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_9_entry.place(x=355, y=485)


# quiz 2 question 10 widgets
quiz_2_question_10_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_10_title.place(x=0, y=550)


quiz_2_question_10_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_10_entry.place(x=10, y=645)


# marking quiz 2


def quiz_2_marking():
    score = 0
    if quiz_2_question_1_entry.get() == "a":
        score = score + 1
    if quiz_2_question_2_entry.get() == "a":
        score = score + 1
    if quiz_2_question_3_entry.get() == "a":
        score = score + 1
    if quiz_2_question_4_entry.get() == "a":
        score = score + 1
    if quiz_2_question_5_entry.get() == "a":
        score = score + 1
    if quiz_2_question_6_entry.get() == "a":
        score = score + 1
    if quiz_2_question_7_entry.get() == "a":
        score = score + 1
    if quiz_2_question_8_entry.get() == "a":
        score = score + 1
    if quiz_2_question_9_entry.get() == "a":
        score = score + 1
    if quiz_2_question_10_entry.get() == "a":
        score = score + 1
    quiz_2_result = CTkLabel(quizpage_2, text = f"Your Score is : {score}", font=("arial", 25), bg_color = "green")
    quiz_2_result.place(x=220, y=545)


# submit button for quiz 2

quiz_2_submit = CTkButton(quizpage_2, text = "Submit", command = quiz_2_marking)
quiz_2_submit.place(x=350, y=650)

# widgets for quiz 3


# quiz 3 question 1 widgets
quiz_3_question_1_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_1_title.place(x=0, y=10)


quiz_3_question_1_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_1_entry.place(x=5, y=105)


# quiz 3 question 2 widgets
quiz_3_question_2_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_2_title.place(x=175, y=10)


quiz_3_question_2_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_2_entry.place(x=180, y=105)


# quiz 3 question 3 widgets
quiz_3_question_3_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_3_title.place(x=350, y=10)


quiz_3_question_3_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_3_entry.place(x=355, y=105)


# quiz 3 question 4 widgets
quiz_3_question_4_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_4_title.place(x=0, y=200)


quiz_3_question_4_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_4_entry.place(x=5, y=295)


# quiz 3 question 5 widgets
quiz_3_question_5_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_5_title.place(x=175, y=200)


quiz_3_question_5_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_5_entry.place(x=180, y=295)


# quiz 3 question 6 widgets
quiz_3_question_6_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_6_title.place(x=350, y=200)


quiz_3_question_6_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_6_entry.place(x=355, y=295)


# quiz 3 question 7 widgets
quiz_3_question_7_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_7_title.place(x=0, y=390)


quiz_3_question_7_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_7_entry.place(x=10, y=485)


# quiz 3 question 8 widgets
quiz_3_question_8_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_8_title.place(x=175, y=390)


quiz_3_question_8_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_8_entry.place(x=180, y=485)


# quiz 3 question 9 widgets
quiz_3_question_9_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_9_title.place(x=350, y=390)


quiz_3_question_9_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_9_entry.place(x=355, y=485)


# quiz 3 question 10 widgets
quiz_3_question_10_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_10_title.place(x=0, y=550)


quiz_3_question_10_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_10_entry.place(x=10, y=645)


# marking quiz 3


def quiz_3_marking():
    score = 0
    if quiz_3_question_1_entry.get() == "a":
        score = score + 1
    if quiz_3_question_2_entry.get() == "a":
        score = score + 1
    if quiz_3_question_3_entry.get() == "a":
        score = score + 1
    if quiz_3_question_4_entry.get() == "a":
        score = score + 1
    if quiz_3_question_5_entry.get() == "a":
        score = score + 1
    if quiz_3_question_6_entry.get() == "a":
        score = score + 1
    if quiz_3_question_7_entry.get() == "a":
        score = score + 1
    if quiz_3_question_8_entry.get() == "a":
        score = score + 1
    if quiz_3_question_9_entry.get() == "a":
        score = score + 1
    if quiz_3_question_10_entry.get() == "a":
        score = score + 1
    quiz_3_result = CTkLabel(quizpage_3, text = f"Your Score is : {score}", font=("arial", 25), bg_color = "green")
    quiz_3_result.place(x=220, y=545)

# submit button for quiz 3

quiz_3_submit = CTkButton(quizpage_3, text = "Submit", command = quiz_3_marking)
quiz_3_submit.place(x=350, y=650)

# menubar

menubar = Menu(root)
root.configure(menu=menubar)

menuhome = Menu(menubar, tearoff = 0)
menusize = Menu(menubar, tearoff = 0)
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

