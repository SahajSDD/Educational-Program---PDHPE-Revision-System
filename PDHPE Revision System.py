from tkinter import *
from customtkinter import *
root = CTk()
root.title("PDHPE Revision System - First Aid")
root.geometry("800x700")

# Creating Frames to represent different pages

homepage = CTkFrame(root, width = 500, height = 700)
homepage.pack(fill="both", expand = 1)
lessonpage = CTkFrame(root, width = 400, height = 400)
quizpage = CTkFrame(root, width = 400, height = 400)
scenariopage = CTkFrame(root, width = 400, height = 400)

# different quiz pages
quizpage_1 = CTkFrame(root, width = 400, height = 400)
quizpage_2 = CTkFrame(root, width = 400, height = 400)
quizpage_3 = CTkFrame(root, width = 400, height = 400)

# result pages for quizzes
quiz_1_resultpage = CTkFrame(root, width = 400, height = 400)
quiz_2_resultpage = CTkFrame(root, width = 400, height = 400)
quiz_3_resultpage = CTkFrame(root, width = 400, height = 400)

# different scenario pages
scenariopage_1 = CTkFrame(root, width= 400, height = 400)
scenariopage_2 = CTkFrame(root, width= 400, height = 400)
scenariopage_3 = CTkFrame(root, width= 400, height = 400)

# result pages for scenarios
scenario_1_resultpage = CTkFrame(root,width = 400, height = 400)
scenario_2_resultpage = CTkFrame(root,width = 400, height = 400)
scenario_3_resultpage = CTkFrame(root,width = 400, height = 400)



# commands for size

def small():
    set_widget_scaling(0.75)
    root.minsize(600, 525)
    root.geometry("350x500")

def medium():
    set_widget_scaling(1.0)
    root.minsize(800, 700)
    root.geometry("800x700")

def large():
    set_widget_scaling(1.1)
    root.minsize(870, 880)
    root.geometry("550x850")

# Switching Pages

def home():
    homepage.pack(fill="both", expand = 1)
    lessonpage.pack_forget()
    quizpage.pack_forget()
    quizpage_1.pack_forget()
    quizpage_2.pack_forget()
    quizpage_3.pack_forget()
    quiz_1_resultpage.pack_forget()
    quiz_2_resultpage.pack_forget()
    quiz_3_resultpage.pack_forget()
    scenariopage.pack_forget()
    scenariopage_1.pack_forget()
    scenariopage_2.pack_forget()
    scenariopage_3.pack_forget()
    scenario_1_resultpage.pack_forget() 
    scenario_2_resultpage.pack_forget()
    scenario_3_resultpage.pack_forget()

def lesson():
    lessonpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

def quiz(): 
    quizpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

def scenario():
    scenariopage.pack(fill="both", expand = 1)
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

def begin_scenario_1():
    scenariopage.pack_forget()
    scenariopage_1.pack(fill="both", expand = 1)

def begin_scenario_2():
    scenariopage.pack_forget()
    scenariopage_2.pack(fill="both", expand = 1)

def begin_scenario_3():
    scenariopage.pack_forget()
    scenariopage_3.pack(fill="both", expand = 1)


# Widgets for Home Page

title_label = CTkLabel(homepage, text="PDHPE Revision System", font=("Arial bold", 25))
title_label.place(x=275, y=25)

subtitle_label = CTkLabel(homepage, text="First Aid", font=("Arial italic", 15))
subtitle_label.place(x=375, y=100)

lesson_button = CTkButton(homepage, width=200, height=100, text="Lesson", font=("Arial bold", 15), command = lesson)
lesson_button.place(x=305, y=150)

quiz_button = CTkButton(homepage, width=200, height=100, text="Quiz", font=("Arial bold", 15), command = quiz)
quiz_button.place(x=305, y=300)

scenario_button = CTkButton(homepage, width=200, height=100, text="Scenario", font=("Arial bold", 15), command = scenario)
scenario_button.place(x=305, y=450)

# Widgets for Lesson Page
lessonpage_title = CTkLabel(lessonpage, text="Lesson List", font=("arial", 25))
lessonpage_title.place(x=350, y=25)

lesson_1 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 1")
lesson_1.place(x=0, y=200)
lesson_2 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 2")
lesson_2.place(x=0, y=300)
lesson_3 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 3")
lesson_3.place(x=0, y=400) 

# Widgets for Quiz Page
quizpage_title = CTkLabel(quizpage, text="Quiz List", font=("arial", 25))
quizpage_title.place(x=350, y=25)

quiz_1 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 1 Quiz", command= begin_quiz_1)
quiz_1.place(x=0, y=200)
quiz_2 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 2 Quiz", command= begin_quiz_2)
quiz_2.place(x=0, y=300)
quiz_3 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 3 Quiz", command= begin_quiz_3)
quiz_3.place(x=0, y=400) 

# Widgets for Scenario Page

scenariopage_title = CTkLabel(scenariopage, text="Scenario List", font=("arial", 25))
scenariopage_title.place(x=350, y=25)

scenario_1 = CTkButton(scenariopage, width=800, height=100, text="Scenario 1", command= begin_scenario_1)
scenario_1.place(x=0, y=200)
scenario_2 = CTkButton(scenariopage, width=800, height=100, text="Scenario 2", command= begin_scenario_2)
scenario_2.place(x=0, y=300)
scenario_3 = CTkButton(scenariopage, width=800, height=100, text="Scenario 3", command= begin_scenario_3)
scenario_3.place(x=0, y=400) 


# widgets for quiz 1 

# quiz 1 question 1 widgets
quiz_1_question_1_title = CTkLabel(quizpage_1, text = "1)What does STOP stand for?\n\na)stop, talk, observe, prevent\nb)support, treat, observe, prevent\nc)save, treat, observe, prevent\nd)stop, talk, observe, place")
quiz_1_question_1_title.place(x=5, y=10)

quiz_1_question_1_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_1_entry.place(x=10, y=105)

# quiz 1 question 2 widgets
quiz_1_question_2_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_2_title.place(x=300, y=10)

quiz_1_question_2_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_2_entry.place(x=305, y=105)

# quiz 1 question 3 widgets
quiz_1_question_3_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_3_title.place(x=600, y=10)

quiz_1_question_3_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_3_entry.place(x=605, y=105)

# quiz 1 question 4 widgets
quiz_1_question_4_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_4_title.place(x=5, y=200)

quiz_1_question_4_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_4_entry.place(x=10, y=295)

# quiz 1 question 5 widgets
quiz_1_question_5_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_5_title.place(x=300, y=200)

quiz_1_question_5_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_5_entry.place(x=305, y=295)

# quiz 1 question 6 widgets
quiz_1_question_6_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_6_title.place(x=600, y=200)

quiz_1_question_6_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_6_entry.place(x=605, y=295)

# quiz 1 question 7 widgets
quiz_1_question_7_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_7_title.place(x=5, y=390)

quiz_1_question_7_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_7_entry.place(x=10, y=485)

# quiz 1 question 8 widgets
quiz_1_question_8_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_8_title.place(x=300, y=390)

quiz_1_question_8_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_8_entry.place(x=305, y=485)

# quiz 1 question 9 widgets
quiz_1_question_9_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_9_title.place(x=600, y=390)

quiz_1_question_9_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_9_entry.place(x=605, y=485)

# quiz 1 question 10 widgets
quiz_1_question_10_title = CTkLabel(quizpage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_1_question_10_title.place(x=5, y=550)

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
    quiz_1_resultpage.pack(fill="both", expand = 1)
    quizpage_1.pack_forget()
    quiz_1_result = CTkLabel(quiz_1_resultpage, text = f"Your Score is : {score}/10", font=("arial", 50), bg_color = "green")
    quiz_1_result.place(x=175, y=250)

# submit button for quiz 1

quiz_1_submit = CTkButton(quizpage_1, text = "Submit", command = quiz_1_marking)
quiz_1_submit.place(x=600, y=650)

# widgets for quiz 2


# quiz 2 question 1 widgets
quiz_2_question_1_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_1_title.place(x=5, y=10)


quiz_2_question_1_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_1_entry.place(x=10, y=105)


# quiz 2 question 2 widgets
quiz_2_question_2_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_2_title.place(x=300, y=10)


quiz_2_question_2_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_2_entry.place(x=305, y=105)


# quiz 2 question 3 widgets
quiz_2_question_3_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_3_title.place(x=600, y=10)


quiz_2_question_3_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_3_entry.place(x=605, y=105)


# quiz 2 question 4 widgets
quiz_2_question_4_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_4_title.place(x=5, y=200)


quiz_2_question_4_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_4_entry.place(x=10, y=295)


# quiz 2 question 5 widgets
quiz_2_question_5_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_5_title.place(x=300, y=200)


quiz_2_question_5_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_5_entry.place(x=305, y=295)


# quiz 2 question 6 widgets
quiz_2_question_6_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_6_title.place(x=600, y=200)


quiz_2_question_6_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_6_entry.place(x=605, y=295)


# quiz 2 question 7 widgets
quiz_2_question_7_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_7_title.place(x=5, y=390)


quiz_2_question_7_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_7_entry.place(x=10, y=485)


# quiz 2 question 8 widgets
quiz_2_question_8_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_8_title.place(x=300, y=390)


quiz_2_question_8_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_8_entry.place(x=305, y=485)


# quiz 2 question 9 widgets
quiz_2_question_9_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_9_title.place(x=600, y=390)


quiz_2_question_9_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_9_entry.place(x=605, y=485)


# quiz 2 question 10 widgets
quiz_2_question_10_title = CTkLabel(quizpage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_2_question_10_title.place(x=5, y=550)


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
    quiz_2_resultpage.pack(fill="both", expand = 1)
    quizpage_2.pack_forget()
    quiz_2_result = CTkLabel(quiz_2_resultpage, text = f"Your Score is : {score}/10", font=("arial", 50), bg_color = "green")
    quiz_2_result.place(x=175, y=250)


# submit button for quiz 2

quiz_2_submit = CTkButton(quizpage_2, text = "Submit", command = quiz_2_marking)
quiz_2_submit.place(x=600, y=650)

# widgets for quiz 3


# quiz 3 question 1 widgets
quiz_3_question_1_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_1_title.place(x=5, y=10)


quiz_3_question_1_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_1_entry.place(x=10, y=105)


# quiz 3 question 2 widgets
quiz_3_question_2_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_2_title.place(x=300, y=10)


quiz_3_question_2_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_2_entry.place(x=305, y=105)


# quiz 3 question 3 widgets
quiz_3_question_3_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_3_title.place(x=600, y=10)


quiz_3_question_3_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_3_entry.place(x=605, y=105)


# quiz 3 question 4 widgets
quiz_3_question_4_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_4_title.place(x=5, y=200)


quiz_3_question_4_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_4_entry.place(x=10, y=295)


# quiz 3 question 5 widgets
quiz_3_question_5_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_5_title.place(x=300, y=200)


quiz_3_question_5_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_5_entry.place(x=305, y=295)


# quiz 3 question 6 widgets
quiz_3_question_6_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_6_title.place(x=600, y=200)


quiz_3_question_6_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_6_entry.place(x=605, y=295)


# quiz 3 question 7 widgets
quiz_3_question_7_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_7_title.place(x=5, y=390)


quiz_3_question_7_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_7_entry.place(x=10, y=485)


# quiz 3 question 8 widgets
quiz_3_question_8_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_8_title.place(x=300, y=390)


quiz_3_question_8_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_8_entry.place(x=305, y=485)


# quiz 3 question 9 widgets
quiz_3_question_9_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_9_title.place(x=600, y=390)


quiz_3_question_9_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_9_entry.place(x=605, y=485)


# quiz 3 question 10 widgets
quiz_3_question_10_title = CTkLabel(quizpage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
quiz_3_question_10_title.place(x=5, y=550)


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
    quiz_3_resultpage.pack(fill="both", expand = 1)
    quizpage_3.pack_forget()
    quiz_3_result = CTkLabel(quiz_3_resultpage, text = f"Your Score is : {score}/10", font=("arial", 50), bg_color = "green")
    quiz_3_result.place(x=175, y=250)

# submit button for quiz 3

quiz_3_submit = CTkButton(quizpage_3, text = "Submit", command = quiz_3_marking)
quiz_3_submit.place(x=600, y=650)

# widgets for scenario 1

scenario_1_description_title = CTkLabel(scenariopage_1, text = "Scenario 1 Description:", font = ("arial bold", 20))
scenario_1_description_title.place(x = 15, y = 10)

scenario_1_description = CTkLabel(scenariopage_1, text = "blahblahblahblahblahblahvblahblahblahb\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah" )
scenario_1_description.place( x = 10, y = 50)

# scenario 1 question 1 widgets

scenario_1_question_1_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_1_title.place(x = 10, y = 175)
                                
scenario_1_question_1_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_1_entry.place(x = 20, y = 270 )

# scenario 1 question 2 widgets

scenario_1_question_2_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_2_title.place(x = 300, y = 175)
                                
scenario_1_question_2_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_2_entry.place(x = 305, y = 270)

# scenario 1 question 3 widgets

scenario_1_question_3_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_3_title.place(x = 10, y = 350)
                                
scenario_1_question_3_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_3_entry.place(x = 20, y = 445)

# scenario 1 question 4 widgets

scenario_1_question_4_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_4_title.place(x = 300, y = 350)
                                
scenario_1_question_4_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_4_entry.place(x = 305, y = 445)

# scenario 1 question 5 widgets

scenario_1_question_5_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_5_title.place(x = 600, y = 350)
                                
scenario_1_question_5_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_5_entry.place(x = 605, y = 445)

# scenario 1 question 6 widgets

scenario_1_question_6_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_6_title.place(x = 10, y = 525)
                                
scenario_1_question_6_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_6_entry.place(x = 20, y = 620)

# scenario 1 question 7 widgets

scenario_1_question_7_title = CTkLabel(scenariopage_1, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_1_question_7_title.place(x = 300, y = 525)
                                
scenario_1_question_7_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_7_entry.place(x = 305, y = 620)

# scenario 1 marking

def scenario_1_marking():
    score = 0
    if scenario_1_question_1_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_2_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_3_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_4_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_5_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_6_entry.get() == "a" :
        score = score + 1
    if scenario_1_question_7_entry.get() == "a" :
        score = score + 1
    scenario_1_resultpage.pack(fill="both", expand = 1)
    scenariopage_1.pack_forget()
    scenario_1_result = CTkLabel(scenario_1_resultpage, text = f"Your Score is : {score}/7", font=("arial", 50), bg_color = "green")
    scenario_1_result.place(x=175, y=250)

# scenario 1 submit button

scenario_1_submit = CTkButton(scenariopage_1, text = "Submit", command = scenario_1_marking)
scenario_1_submit.place(x = 600, y = 620)

# widgets for scenario 2

scenario_2_description_title = CTkLabel(scenariopage_2, text = "scenario 2 Description:", font = ("arial bold", 20))
scenario_2_description_title.place(x = 15, y = 10)

scenario_2_description = CTkLabel(scenariopage_2, text = "blahblahblahblahblahblahvblahblahblahb\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah" )
scenario_2_description.place( x = 10, y = 50)


# scenario 2 question 1 widgets

scenario_2_question_1_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_1_title.place(x = 10, y = 175)
                               
scenario_2_question_1_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_1_entry.place(x = 20, y = 270 )


# scenario 2 question 2 widgets

scenario_2_question_2_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_2_title.place(x = 300, y = 175)
                               
scenario_2_question_2_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_2_entry.place(x = 305, y = 270)


# scenario 2 question 3 widgets

scenario_2_question_3_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_3_title.place(x = 10, y = 350)
                               
scenario_2_question_3_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_3_entry.place(x = 20, y = 445)


# scenario 2 question 4 widgets

scenario_2_question_4_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_4_title.place(x = 300, y = 350)
                               
scenario_2_question_4_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_4_entry.place(x = 305, y = 445)


# scenario 2 question 5 widgets

scenario_2_question_5_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_5_title.place(x = 600, y = 350)
                               
scenario_2_question_5_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_5_entry.place(x = 605, y = 445)


# scenario 2 question 6 widgets

scenario_2_question_6_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_6_title.place(x = 10, y = 525)
                               
scenario_2_question_6_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_6_entry.place(x = 20, y = 620)


# scenario 2 question 7 widgets

scenario_2_question_7_title = CTkLabel(scenariopage_2, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_2_question_7_title.place(x = 300, y = 525)
                               
scenario_2_question_7_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_7_entry.place(x = 305, y = 620)


# scenario 2 marking

def scenario_2_marking():
    score = 0
    if scenario_2_question_1_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_2_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_3_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_4_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_5_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_6_entry.get() == "a" :
        score = score + 1
    if scenario_2_question_7_entry.get() == "a" :
        score = score + 1
    scenario_2_resultpage.pack(fill="both", expand = 1)
    scenariopage_2.pack_forget()
    scenario_2_result = CTkLabel(scenario_2_resultpage, text = f"Your Score is : {score}/7", font=("arial", 50), bg_color = "green")
    scenario_2_result.place(x=175, y=250)


# scenario 2 submit button

scenario_2_submit = CTkButton(scenariopage_2, text = "Submit", command = scenario_2_marking)
scenario_2_submit.place(x = 600, y = 620)

# widgets for scenario 3

scenario_3_description_title = CTkLabel(scenariopage_3, text = "scenario 3 Description:", font = ("arial bold", 20))
scenario_3_description_title.place(x = 15, y = 10)


scenario_3_description = CTkLabel(scenariopage_3, text = "blahblahblahblahblahblahvblahblahblahb\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah\nlahblahblahblahblahblahblahblahblahblah" )
scenario_3_description.place( x = 10, y = 50)


# scenario 3 question 1 widgets

scenario_3_question_1_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_1_title.place(x = 10, y = 175)
                               
scenario_3_question_1_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_1_entry.place(x = 20, y = 270 )


# scenario 3 question 2 widgets

scenario_3_question_2_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_2_title.place(x = 300, y = 175)
                               
scenario_3_question_2_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_2_entry.place(x = 305, y = 270)


# scenario 3 question 3 widgets

scenario_3_question_3_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_3_title.place(x = 10, y = 350)
                               
scenario_3_question_3_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_3_entry.place(x = 20, y = 445)


# scenario 3 question 4 widgets

scenario_3_question_4_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_4_title.place(x = 300, y = 350)
                               
scenario_3_question_4_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_4_entry.place(x = 305, y = 445)


# scenario 3 question 5 widgets

scenario_3_question_5_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_5_title.place(x = 600, y = 350)
                               
scenario_3_question_5_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_5_entry.place(x = 605, y = 445)


# scenario 3 question 6 widgets

scenario_3_question_6_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_6_title.place(x = 10, y = 525)
                               
scenario_3_question_6_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_6_entry.place(x = 20, y = 620)


# scenario 3 question 7 widgets

scenario_3_question_7_title = CTkLabel(scenariopage_3, text = "1)what is the blah bah\n\na)the donkey\nb)the monkey\nc)the wonkey\nd)the jonkey")
scenario_3_question_7_title.place(x = 300, y = 525)
                               
scenario_3_question_7_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_7_entry.place(x = 305, y = 620)


# scenario 3 marking

def scenario_3_marking():
    score = 0
    if scenario_3_question_1_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_2_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_3_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_4_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_5_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_6_entry.get() == "a" :
        score = score + 1
    if scenario_3_question_7_entry.get() == "a" :
        score = score + 1
    scenario_3_resultpage.pack(fill="both", expand = 1)
    scenariopage_3.pack_forget()
    scenario_3_result = CTkLabel(scenario_3_resultpage, text = f"Your Score is : {score}/7", font=("arial", 50), bg_color = "green")
    scenario_3_result.place(x=175, y=250)


# scenario 3 submit button

scenario_3_submit = CTkButton(scenariopage_3, text = "Submit", command = scenario_3_marking)
scenario_3_submit.place(x = 600, y = 620)

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

