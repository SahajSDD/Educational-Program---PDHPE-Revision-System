from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3
from ttkbootstrap import Style
from quiz_data_1 import quiz_data_1
from quiz_data_2 import quiz_data_2
from quiz_data_3 import quiz_data_3
from tkinter import messagebox, ttk

root = CTk()
root.title("PDHPE Revision System - First Aid")
root.geometry("800x700")

# Creating Frames to represent different pages

homepage = CTkFrame(root, width = 500, height = 700)
homepage.pack(fill="both", expand = 1)
lessonpage = CTkFrame(root, width = 400, height = 400)
quizpage = CTkFrame(root, width = 400, height = 400)
scenariopage = CTkFrame(root, width = 400, height = 400)

# different lesson pages
lessonpage_1 = CTkFrame(root, width = 400, height = 400)
lessonpage_2 = CTkFrame(root, width = 400, height = 400)
lessonpage_3 = CTkFrame(root, width = 400, height = 400)

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
    root.minsize(870, 800)
    root.geometry("550x850")

# Switching Pages

def home():
    homepage.pack(fill="both", expand = 1)
    lessonpage.pack_forget()
    lessonpage_1.pack_forget()
    lessonpage_2.pack_forget()
    lessonpage_3.pack_forget()
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

def begin_lesson_1():
    lessonpage.pack_forget()
    lessonpage_1.pack(fill="both", expand = 1)

def begin_lesson_2():
    lessonpage.pack_forget()
    lessonpage_2.pack(fill="both", expand = 1)

def begin_lesson_3():
    lessonpage.pack_forget()
    lessonpage_3.pack(fill="both", expand = 1)

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

def homepage_tts():
    engine = pyttsx3.init()
    engine.say("PDHPE Revision System, First Aid, Lesson, Quiz, Scenario")
    engine.runAndWait()

talkbutton = CTkButton(homepage, text = "Read Page Aloud", command = homepage_tts, width=50, height=50)
talkbutton.place(x=600, y=200)

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

lesson_1 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 1", command=begin_lesson_1)
lesson_1.place(x=0, y=200)
lesson_2 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 2", command=begin_lesson_2)
lesson_2.place(x=0, y=300)
lesson_3 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 3", command=begin_lesson_3)
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

# Quiz 1 System (including marking)

# Function to display the current question and choices
def quiz_1_show_question():
    global question_1
    question_1 = quiz_data_1[quiz_1_current_question]
    question_1_label.configure(text=question_1["question"])
    
    choices = question_1["choices"]
    for i in range(4):
        quiz_1_choice_buttons[i].configure(text=choices[i], state="normal") 

    quiz_1_feedback_label.configure(text="")
    quiz_1_next_button.configure(state="disabled")

    text_to_speech_1.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_1_tts():
    engine = pyttsx3.init()
    engine.say(question_1)
    engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_1_check_answer(choice):
    question_1 = quiz_data_1[quiz_1_current_question]
    selected_choice = quiz_1_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question_1["answer"]:
        global quiz_1_score
        quiz_1_score += 1
        quiz_1_score_label.configure(text="Score: {}/{}".format(quiz_1_score, len(quiz_data_1)))
        quiz_1_feedback_label.configure(text="Correct!")
    else:
        quiz_1_feedback_label.configure(text="Incorrect! "+ question_1["answer"])
    
    # Disable all choice buttons and enable the next button
    for button_1 in quiz_1_choice_buttons:
        button_1.configure(state="disabled")
    quiz_1_next_button.configure(state="normal")

# Function to move to the next question
def next_question_1():
    global quiz_1_current_question
    quiz_1_current_question +=1

    if quiz_1_current_question < len(quiz_data_1):
        # If there are more questions, show the next question
        quiz_1_show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(quiz_1_score, len(quiz_data_1)))
        

# Quiz 1 Widgets

# Create the question label
question_1_label = CTkLabel(quizpage_1, anchor="center")
question_1_label.pack(pady=10)

# Create the choice buttons
quiz_1_choice_buttons = []
for i in range(4):
    button_1 = CTkButton(quizpage_1, height = 100, width = 200, command=lambda i=i: quiz_1_check_answer(i))
    button_1.pack(pady=5)
    quiz_1_choice_buttons.append(button_1)

# text to speech button for questions
text_to_speech_1 = CTkButton(quizpage_1, text="speak", command = quiz_1_tts)
text_to_speech_1.pack()

# Create the feedback label
quiz_1_feedback_label = CTkLabel(quizpage_1,anchor="center")
quiz_1_feedback_label.pack(pady=10)

quiz_1_score_label = CTkLabel(quizpage_1, text="Score: 0/{}".format(len(quiz_data_1)),anchor="center",)
quiz_1_score_label.pack(pady=10)

quiz_1_next_button = CTkButton(quizpage_1, text="Next", command=next_question_1, state="disabled")
quiz_1_next_button.pack(pady=10)

# Initialise score and current question
quiz_1_score = 0
quiz_1_current_question = 0

quiz_1_show_question()

# Quiz 2 System (including marking)

# Function to display the current question and choices
def quiz_2_show_question():
    global question_2
    question_2 = quiz_data_2[quiz_2_current_question]
    question_2_label.configure(text=question_2["question"])
   
    choices = question_2["choices"]
    for i in range(4):
        quiz_2_choice_buttons[i].configure(text=choices[i], state="normal")

    quiz_2_feedback_label.configure(text="")
    quiz_2_next_button.configure(state="disabled")

    text_to_speech_2.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_2_tts():
    engine = pyttsx3.init()
    engine.say(question_2)
    engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_2_check_answer(choice):
    question_2 = quiz_data_2[quiz_2_current_question]
    selected_choice = quiz_2_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question_2["answer"]:
        global quiz_2_score
        quiz_2_score += 1
        quiz_2_score_label.configure(text="Score: {}/{}".format(quiz_2_score, len(quiz_data_2)))
        quiz_2_feedback_label.configure(text="Correct!")
    else:
        quiz_2_feedback_label.configure(text="Incorrect! "+ question_2["answer"])
   
    # Disable all choice buttons and enable the next button
    for button_2 in quiz_2_choice_buttons:
        button_2.configure(state="disabled")
    quiz_2_next_button.configure(state="normal")

# Function to move to the next question
def next_question_2():
    global quiz_2_current_question
    quiz_2_current_question +=1

    if quiz_2_current_question < len(quiz_data_1):
        # If there are more questions, show the next question
        quiz_2_show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(quiz_2_score, len(quiz_data_2)))

# Quiz 2 Widgets

# Create the question label
question_2_label = CTkLabel(quizpage_2, anchor="center")
question_2_label.pack(pady=10)

# Create the choice buttons
quiz_2_choice_buttons = []
for i in range(4):
    button_2 = CTkButton(quizpage_2, height = 100, width = 200, command=lambda i=i: quiz_2_check_answer(i))
    button_2.pack(pady=5)
    quiz_2_choice_buttons.append(button_2)

# text to speech button for questions
text_to_speech_2 = CTkButton(quizpage_2, text="speak", command = quiz_2_tts)
text_to_speech_2.pack()

# Create the feedback label
quiz_2_feedback_label = CTkLabel(quizpage_2,anchor="center")
quiz_2_feedback_label.pack(pady=10)

quiz_2_score_label = CTkLabel(quizpage_2, text="Score: 0/{}".format(len(quiz_data_2)),anchor="center",)
quiz_2_score_label.pack(pady=10)

quiz_2_next_button = CTkButton(quizpage_2, text="Next", command=next_question_2, state="disabled")
quiz_2_next_button.pack(pady=10)

# Initialise score and current question
quiz_2_score = 0
quiz_2_current_question = 0

quiz_2_show_question()

# Quiz 3 System (including marking)

def quiz_3_show_question():
    global question_3
    question_3 = quiz_data_3[quiz_3_current_question]
    question_3_label.configure(text=question_3["question"])
   
    choices = question_3["choices"]
    for i in range(4):
        quiz_3_choice_buttons[i].configure(text=choices[i], state="normal")

    quiz_3_feedback_label.configure(text="")
    quiz_3_next_button.configure(state="disabled")

    text_to_speech_3.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_3_tts():
    engine = pyttsx3.init()
    engine.say(question_3)
    engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_3_check_answer(choice):
    question_3 = quiz_data_3[quiz_3_current_question]
    selected_choice = quiz_3_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question_3["answer"]:
        global quiz_3_score
        quiz_3_score += 1
        quiz_3_score_label.configure(text="Score: {}/{}".format(quiz_3_score, len(quiz_data_3)))
        quiz_3_feedback_label.configure(text="Correct!")
    else:
        quiz_3_feedback_label.configure(text="Incorrect! "+ question_3["answer"])
   
    # Disable all choice buttons and enable the next button
    for button_3 in quiz_3_choice_buttons:
        button_3.configure(state="disabled")
    quiz_3_next_button.configure(state="normal")

# Function to move to the next question
def next_question_3():
    global quiz_3_current_question
    quiz_3_current_question +=1

    if quiz_3_current_question < len(quiz_data_3):
        # If there are more questions, show the next question
        quiz_3_show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(quiz_3_score, len(quiz_data_3)))

# Quiz 3 Widgets

# Create the question label
question_3_label = CTkLabel(quizpage_3, anchor="center")
question_3_label.pack(pady=10)

# Create the choice buttons
quiz_3_choice_buttons = []
for i in range(4):
    button_3 = CTkButton(quizpage_3, height = 100, width = 300, command=lambda i=i: quiz_3_check_answer(i))
    button_3.pack(pady=5)
    quiz_3_choice_buttons.append(button_3)

# text to speech button for questions
text_to_speech_3 = CTkButton(quizpage_3, text="speak", command = quiz_3_tts)
text_to_speech_3.pack()

# Create the feedback label
quiz_3_feedback_label = CTkLabel(quizpage_3,anchor="center")
quiz_3_feedback_label.pack(pady=10)

quiz_3_score_label = CTkLabel(quizpage_3, text="Score: 0/{}".format(len(quiz_data_3)),anchor="center",)
quiz_3_score_label.pack(pady=10)

quiz_3_next_button = CTkButton(quizpage_3, text="Next", command=next_question_3, state="disabled")
quiz_3_next_button.pack(pady=10)

# Initialise score and current question
quiz_3_score = 0
quiz_3_current_question = 0

quiz_3_show_question()

# widgets for scenario 1

scenario_1_description_title = CTkLabel(scenariopage_1, text = "Scenario 1 Description:", font = ("arial bold", 20))
scenario_1_description_title.place(x = 15, y = 10)

scenario_1_description = CTkLabel(scenariopage_1, text = "Johnny was playing near the lit gas stove.\nAs he jumped around he leant over the stove and touched the open flame\nwith his right arm. It appears as red and rashy and Johnny complains\nof an intense, sharp pain. He then passes out from exhaustion." )
scenario_1_description.place( x = 10, y = 50)

# scenario 1 question 1 widgets

scenario_1_question_1_title = CTkLabel(scenariopage_1, text = "1) What Primary Injury\n has Johhny Suffered?", font=("arial bold", 12))
scenario_1_question_1_title.place(x = 20, y = 165)

scenario_1_question_1_choices = CTkLabel(scenariopage_1, text = "a) Heart Attack\n b) Hyperthermia\n c) General Burns\n d) Shock ")
scenario_1_question_1_choices.place(x = 30, y = 210)
                                
scenario_1_question_1_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_1_entry.place(x = 30, y = 270 )

# scenario 1 question 2 widgets

scenario_1_question_2_title = CTkLabel(scenariopage_1, text = "2) How should the \nPrimary injury be treated?", font=("arial bold", 12))
scenario_1_question_2_title.place(x = 300, y = 165)

scenario_1_question_2_title = CTkLabel(scenariopage_1, text = "a) Epipen\n b) Running hands under Cool Water\n c) Immediate Bandaging\n d) Lotions and Oils" )
scenario_1_question_2_title.place(x = 260, y = 210)
                                
scenario_1_question_2_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_2_entry.place(x = 315, y = 270)

# scenario 1 question 3 widgets

scenario_1_question_3_title = CTkLabel(scenariopage_1, text = "3) As Johnny has passed out,\n what is the first priority?",font=("arial bold", 12))
scenario_1_question_3_title.place(x = 10, y = 335)

scenario_1_question_3_choices = CTkLabel(scenariopage_1, text = "a) Tend to Primary Injury\n b) Roll into Recovery Position\nc) Check for Breathing\n d) Turn off Stove")
scenario_1_question_3_choices.place(x = 10, y = 375)
                                
scenario_1_question_3_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_3_entry.place(x = 30, y = 445)

# scenario 1 question 4 widgets

scenario_1_question_4_title = CTkLabel(scenariopage_1, text = "4) Gas and smoke begin to fill the room,\nHow should Johnny be carried out?", font=("arial bold", 12))
scenario_1_question_4_title.place(x = 260, y = 340)

scenario_1_question_4_choices = CTkLabel(scenariopage_1, text = "a) Chair Lift Method\nb) Four-Handed Seat\nd) Any method is applicable\nd) Drag Method")
scenario_1_question_4_choices.place(x = 280, y = 375)
                                
                                
scenario_1_question_4_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_4_entry.place(x = 305, y = 445)

# scenario 1 question 5 widgets

scenario_1_question_5_title = CTkLabel(scenariopage_1, text = "5) Is Medical Referal Necessary?", font=("arial bold", 12))
scenario_1_question_5_title.place(x = 10, y = 525)

scenario_1_question_5_choices = CTkLabel(scenariopage_1, text = "a) Yes, in all cases\nb) No, there is no reason to\nc) Decided by Patient\nd) Unsure")
scenario_1_question_5_choices.place(x = 10, y = 550)
                                
scenario_1_question_5_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_5_entry.place(x = 30, y = 620)


# scenario 1 question 6 widgets

scenario_1_question_6_title = CTkLabel(scenariopage_1, text = "6) You were the only person around when Johhny got\n injured, Are you legally obliged to assist?", font=("arial bold", 12))
scenario_1_question_6_title.place(x = 240, y = 515)

scenario_1_question_6_choices = CTkLabel(scenariopage_1, text = "a) Yes\nb) No\nc) If it were a situation of life or death\nd) Unsure")
scenario_1_question_6_choices.place(x = 250, y = 550)
                                
scenario_1_question_6_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_6_entry.place(x = 305, y = 620)

#scenario 1 image
Scenario_1_Image = Image.open("Scenario_1_Image.jpg").resize((300, 300))
image_tk = ImageTk.PhotoImage(Scenario_1_Image)
image_label_1 = tk.Label(scenariopage_1, text="", image = image_tk)
image_label_1.image = image_tk
image_label_1.place(x=650, y=200)

# scenario 1 marking

def scenario_1_marking():
    scenario_1_score = 0
    if scenario_1_question_1_entry.get() == "c" :
        scenario_1_score =+ 1
        scenario_1_feedback_1 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_1.place(x=60, y=300)
    else:
        scenario_1_feedback_1 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_1.place(x=15, y=300)
    if scenario_1_question_2_entry.get() == "b" :
        scenario_1_score =+ 1
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_2.place(x=350, y=300)
    else:
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_1_feedback_2.place(x=300, y=300)
    if scenario_1_question_3_entry.get() == "c" :
        scenario_1_score =+ 1
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_3.place(x=60, y=480)
    else:
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_3.place(x=15, y=480)
    if scenario_1_question_4_entry.get() == "d" :
        scenario_1_score =+ 1
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_4.place(x=350, y=480)
    else:
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_1_feedback_4.place(x=305, y=480)
    if scenario_1_question_5_entry.get() == "a" :
        scenario_1_score =+ 1
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_5.place(x=60, y=660)
    else:
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_1_feedback_5.place(x=15, y=660)
    if scenario_1_question_6_entry.get() == "b" :
        scenario_1_score =+ 1
        scenario_1_feedback_6 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_6.place(x=350, y=660)
    else:
        scenario_1_feedback_6 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_1_feedback_6.place(x=305, y=660)
    scenario_1_result_label = CTkLabel(scenariopage_1, text=f"Your Score is : {scenario_1_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_1_result_label.place(x = 600, y = 550)
    
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

doggy = Image.open("Frog.PNG").resize((100, 100))
image_tk = ImageTk.PhotoImage(doggy)
image_label = tk.Label(root, text="", image = image_tk)
image_label.image = image_tk
image_label.place(x=0, y=0)


    
root.mainloop()

