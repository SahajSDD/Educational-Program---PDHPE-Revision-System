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
    root.minsize(870, 800)
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
quiz_1_question_1_title = CTkLabel(quizpage_1, text = "1)What does STOP stand for?", font = ("arial bold", 12))
quiz_1_question_1_title.place(x=5, y=10)

quiz_1_question_1_choices = CTkLabel(quizpage_1, text = "a)stop, talk, observe, prevent\nb)support, treat, observe, prevent\nc)save, treat, observe, prevent\nd)stop, talk, observe, place")
quiz_1_question_1_choices.place(x = 5, y = 35)

quiz_1_question_1_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_1_entry.place(x=25, y=105)

# quiz 1 question 2 widgets
quiz_1_question_2_title = CTkLabel(quizpage_1, text = "2) When would it be appropriate to commence CPR?", font = ("arial bold", 12))
quiz_1_question_2_title.place(x=225, y=10)

quiz_1_question_2_choices = CTkLabel(quizpage_1, text = "a) As soon as possible\nb) If patient is not breathing\nc) Never. Let professionals handle CPR\nd) If the patient is unconscious")
quiz_1_question_2_choices.place(x=245, y=35)

quiz_1_question_2_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_2_entry.place(x=305, y=105)

# quiz 1 question 3 widgets
quiz_1_question_3_title = CTkLabel(quizpage_1, text = "3) PER is used for what type of injury", font=("arial bold", 12))
quiz_1_question_3_title.place(x=550, y=10)

quiz_1_question_3_choices = CTkLabel(quizpage_1, text = "a)concussions\nb) fractures\nc) muscle tears\nd) bleeding")
quiz_1_question_3_choices.place(x=600, y=35)

quiz_1_question_3_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_3_entry.place(x=605, y=105)

# quiz 1 question 4 widgets
quiz_1_question_4_title = CTkLabel(quizpage_1, text = "4) Which is not a cause of shock?", font=("arial bold", 12))
quiz_1_question_4_title.place(x=5, y=200)

quiz_1_question_4_choices = CTkLabel(quizpage_1, text = "a) loss of blood\nb) blisters\nc) loss of fluids \nd) heart attack")
quiz_1_question_4_choices.place(x=15, y=225)

quiz_1_question_4_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_4_entry.place(x=20, y=295)

# quiz 1 question 5 widgets
quiz_1_question_5_title = CTkLabel(quizpage_1, text = "5) What is the management for neck and spinal injuries?", font=("arial bold", 12))
quiz_1_question_5_title.place(x=225, y=200)

quiz_1_question_5_choices = CTkLabel(quizpage_1, text = "a) massage therapy\nb) ice pack application\nc) immobilisation and transportation to medical facility\nd) dynamic stretching")
quiz_1_question_5_choices.place(x=230, y=225)

quiz_1_question_5_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_5_entry.place(x=305, y=295)

# quiz 1 question 6 widgets
quiz_1_question_6_title = CTkLabel(quizpage_1, text = "6) What movement method would\n be used for the unconscious", font=('arial bold', 12))
quiz_1_question_6_title.place(x=570, y=190)

quiz_1_question_6_choices = CTkLabel(quizpage_1, text = "a) drag method\nb) four handed seat method \nc) chair lift method\nd) human crutch")
quiz_1_question_6_choices.place(x=600, y=225)

quiz_1_question_6_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_6_entry.place(x=620, y=295)

# quiz 1 question 7 widgets
quiz_1_question_7_title = CTkLabel(quizpage_1, text = "7) When would there need to be medical referral", font=("arial bold", 12))
quiz_1_question_7_title.place(x=5, y=390)

quiz_1_question_7_choices = CTkLabel(quizpage_1, text = "a) CPR was required\nb) Open wound\nc) Patient is in distress\nd) medication was used")
quiz_1_question_7_choices.place(x=45, y=415)

quiz_1_question_7_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_7_entry.place(x=55, y=485)

# quiz 1 question 8 widgets
quiz_1_question_8_title = CTkLabel(quizpage_1, text = "8) What does the recovery position do for the patient?", font=("arial bold", 12))
quiz_1_question_8_title.place(x=280, y=390)

quiz_1_question_8_choices = CTkLabel(quizpage_1, text = "a) relaxes spine and vertebrae\nb) encourages healthy blood flow\nc) keeps airway clear and open\nd) stimulates nervous response")
quiz_1_question_8_choices.place(x=300, y=415)

quiz_1_question_8_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_8_entry.place(x=335, y=485)

# quiz 1 question 9 widgets
quiz_1_question_9_title = CTkLabel(quizpage_1, text = "9) Whose safety needs to be\n ensured first?", font=('arial bold', 12))
quiz_1_question_9_title.place(x=605, y=380)

quiz_1_question_9_choices = CTkLabel(quizpage_1, text = "a) the casualty\nb) bystanders\nc) yourself\nd) whoever is most at risk")
quiz_1_question_9_choices.place(x=610, y=415)

quiz_1_question_9_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_9_entry.place(x=615, y=485)

# quiz 1 question 10 widgets
quiz_1_question_10_title = CTkLabel(quizpage_1, text = "10) What is the correct order of the basic life action plan?", font = ("arial bold", 12))
quiz_1_question_10_title.place(x=5, y=550)

quiz_1_question_10_choices = CTkLabel(quizpage_1, text = "a) Response, send for help, danger, breathing, airways, defibrillation, compression\nb) Danger, breathing, response, airways, compression, defibrillation, send for help\nc) Danger, response, send for help, airways, breathing, compression, defibrillation\nd) Send for help, danger, response, breathing, airways, compression, defibrillation")
quiz_1_question_10_choices.place(x=5, y=575)

quiz_1_question_10_entry = CTkEntry(quizpage_1, width=100)
quiz_1_question_10_entry.place(x=100, y=645)

# marking quiz 1

def quiz_1_marking():
    score = 0
    if quiz_1_question_1_entry.get() == "a":
        score = score + 1
    if quiz_1_question_2_entry.get() == "b":
        score = score + 1
    if quiz_1_question_3_entry.get() == "d":
        score = score + 1
    if quiz_1_question_4_entry.get() == "b":
        score = score + 1
    if quiz_1_question_5_entry.get() == "c":
        score = score + 1
    if quiz_1_question_6_entry.get() == "a":
        score = score + 1
    if quiz_1_question_7_entry.get() == "a":
        score = score + 1
    if quiz_1_question_8_entry.get() == "c":
        score = score + 1
    if quiz_1_question_9_entry.get() == "c":
        score = score + 1
    if quiz_1_question_10_entry.get() == "c":
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
quiz_2_question_1_title = CTkLabel(quizpage_2, text = "1) What is the management of burns?", font=("arial bold", 12))
quiz_2_question_1_title.place(x=5, y=10)

quiz_2_question_1_choices = CTkLabel(quizpage_2, text = "a) hold under cool running water\nb) apply blister lotions\nc) hold under cold compress\nd) DRSABCD")
quiz_2_question_1_choices.place(x=5, y=35)


quiz_2_question_1_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_1_entry.place(x=45, y=105)


# quiz 2 question 2 widgets
quiz_2_question_2_title = CTkLabel(quizpage_2, text = "2) Which of these is not part of asthma treatment?", font=("arial bold", 12))
quiz_2_question_2_title.place(x=250, y=10)

quiz_2_question_2_choices = CTkLabel(quizpage_2, text = "a) provide water\nb) assist with medication\nc) encourage light movements \nd) breathing exercises")
quiz_2_question_2_choices.place(x=275, y=35)

quiz_2_question_2_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_2_entry.place(x=315, y=105)


# quiz 2 question 3 widgets
quiz_2_question_3_title = CTkLabel(quizpage_2, text = "3) Hypoglycaemia is characterised by: ", font=("arial bold", 12))
quiz_2_question_3_title.place(x=570, y=10)

quiz_2_question_3_choices = CTkLabel(quizpage_2, text = "a) high blood sugar\nb) low blood sugar\nc) low insulin levels \nd) high insulin levels")
quiz_2_question_3_choices.place(x=625, y=35)

quiz_2_question_3_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_3_entry.place(x=625, y=105)


# quiz 2 question 4 widgets
quiz_2_question_4_title = CTkLabel(quizpage_2, text = "4) What medical condition includes\n an epipen in its treatment?", font=("arial bold", 12))
quiz_2_question_4_title.place(x=5, y=190)

quiz_2_question_4_title = CTkLabel(quizpage_2, text = "a) diabetes \nb) poisoning \nc) epileptic seizures \nd) anapylaxis")
quiz_2_question_4_title.place(x=30, y=225)

quiz_2_question_4_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_4_entry.place(x=45, y=295)


# quiz 2 question 5 widgets
quiz_2_question_5_title = CTkLabel(quizpage_2, text = "5) How would an area be adjusted \nfor a patient in an epileptic seizure?", font=("arial bold", 12))
quiz_2_question_5_title.place(x=280, y=180)

quiz_2_question_5_choices = CTkLabel(quizpage_2, text = "a) room temperature increased\nb) room temperature decreased\nc) clear the area around the patient\nd) all lights turned off")
quiz_2_question_5_choices.place(x=290, y=225)

quiz_2_question_5_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_5_entry.place(x=315, y=295)


# quiz 2 question 6 widgets
quiz_2_question_6_title = CTkLabel(quizpage_2, text = "6) If swallowed poison,\n when should you induce vomiting?", font=("arial bold", 12))
quiz_2_question_6_title.place(x=580, y=180)

quiz_2_question_6_choices = CTkLabel(quizpage_2, text = "a) when substance is medicinal \nb) when substance is corrosive\nc) when substance is unknown \nd) when substance is hot in temperature")
quiz_2_question_6_choices.place(x=560, y=225)

quiz_2_question_6_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_6_entry.place(x=625, y=295)


# quiz 2 question 7 widgets
quiz_2_question_7_title = CTkLabel(quizpage_2, text = "7) Which of these is not part\n of hypothermia treatment?", font=("arial bold", 12))
quiz_2_question_7_title.place(x=10, y=370)

quiz_2_question_7_choices = CTkLabel(quizpage_2, text = "a) drink warm fluids\nb) remove any wet clothing\nc) utilise artifical heating\nd) DRSABCD")
quiz_2_question_7_choices.place(x=15, y=415)

quiz_2_question_7_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_7_entry.place(x=45, y=485)


# quiz 2 question 8 widgets
quiz_2_question_8_title = CTkLabel(quizpage_2, text = "8) What type of bandage should\n be used for a snakebite?", font=("arial bold", 12))
quiz_2_question_8_title.place(x=300, y=370)

quiz_2_question_8_choices = CTkLabel(quizpage_2, text = "a) collar and cuff \nb) pressure immobilisation \nc) reptillian power wrap\nd) elastic bandaging")
quiz_2_question_8_choices.place(x=300, y=415)


quiz_2_question_8_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_8_entry.place(x=315, y=485)


# quiz 2 question 9 widgets
quiz_2_question_9_title = CTkLabel(quizpage_2, text = "1) What is RICER used for?", font=("arial bold", 12))
quiz_2_question_9_title.place(x=600, y=370)

quiz_2_question_9_choices = CTkLabel(quizpage_2, text = "a) concussions and head injuries \nb) eye injuries \nc) fractures and dislocations\nd) chemical burns")
quiz_2_question_9_choices.place(x=580, y=415)


quiz_2_question_9_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_9_entry.place(x=625, y=485)


# quiz 2 question 10 widgets
quiz_2_question_10_title = CTkLabel(quizpage_2, text = "1) What does RICER stand for?", font=("arial bold", 12))
quiz_2_question_10_title.place(x=5, y=550)

quiz_2_question_10_choices = CTkLabel(quizpage_2, text = "a) Rest, Ice, Compress, Elevate, Referral \nb) Rest, Ice, Cover, Elevate, Re-Ice\nc) Rest, Ice, Compress, Extend, Referral\nd) Relieve, Ice, Comfort, Elevate, Referral")
quiz_2_question_10_choices.place(x=5, y=575)


quiz_2_question_10_entry = CTkEntry(quizpage_2, width=100)
quiz_2_question_10_entry.place(x=45, y=645)


# marking quiz 2


def quiz_2_marking():
    score = 0
    if quiz_2_question_1_entry.get() == "a":
        score = score + 1
    if quiz_2_question_2_entry.get() == "c":
        score = score + 1
    if quiz_2_question_3_entry.get() == "b":
        score = score + 1
    if quiz_2_question_4_entry.get() == "d":
        score = score + 1
    if quiz_2_question_5_entry.get() == "c":
        score = score + 1
    if quiz_2_question_6_entry.get() == "a":
        score = score + 1
    if quiz_2_question_7_entry.get() == "c":
        score = score + 1
    if quiz_2_question_8_entry.get() == "b":
        score = score + 1
    if quiz_2_question_9_entry.get() == "c":
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
quiz_3_question_1_title = CTkLabel(quizpage_3, text = "1) Which of these strategies are\n valid in managing a traffic accident", font=('arial bold', 12))
quiz_3_question_1_title.place(x=25, y=5)

quiz_3_question_1_choices = CTkLabel(quizpage_3, text = "a) Exiting the vehicle as soon as possible\nb) Making sure the car's ignition is on\nc) Sending a person up the road to warn traffic\nd) Lighting area with high beam lights")
quiz_3_question_1_choices.place(x=5, y=40)

quiz_3_question_1_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_1_entry.place(x=75, y=105)


# quiz 3 question 2 widgets
quiz_3_question_2_title = CTkLabel(quizpage_3, text = "2) Which of these are not part of managing\n an incident in a water environment", font=("arial bold", 12))
quiz_3_question_2_title.place(x=290, y=5)

quiz_3_question_2_choices = CTkLabel(quizpage_3, text = "a) Send for help immediately\nb) Using surrounding branches or environment\nc) Assessing self limitations \nd) Only engage in rescue with more than one person")
quiz_3_question_2_choices.place(x=280, y=40)

quiz_3_question_2_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_2_entry.place(x=355, y=105)


# quiz 3 question 3 widgets
quiz_3_question_3_title = CTkLabel(quizpage_3, text = "3) What is the first priority in\n giving treatment near a live wire", font=('arial bold', 12))
quiz_3_question_3_title.place(x=585, y=5)

quiz_3_question_3_choices = CTkLabel(quizpage_3, text = "a) Treat affected patient\nb) Turn off power source\nc) Clean any spilled liquids\nd) Turn off any lights in the room")
quiz_3_question_3_choices.place(x=600, y=35)

quiz_3_question_3_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_3_entry.place(x=645, y=105)


# quiz 3 question 4 widgets
quiz_3_question_4_title = CTkLabel(quizpage_3, text = "4) Which fluid can HIV/AIDS\n not be passed through?", font=('arial bold', 12) )
quiz_3_question_4_title.place(x=45, y=195)

quiz_3_question_4_choices = CTkLabel(quizpage_3, text = "a) blood \nb) urine \nc) semen \nd) mucus")
quiz_3_question_4_choices.place(x=90, y=225)


quiz_3_question_4_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_4_entry.place(x=75, y=295)


# quiz 3 question 5 widgets
quiz_3_question_5_title = CTkLabel(quizpage_3, text = "5) How can you prevent HIV transmission when performing CPR", font=('arial bold', 12))
quiz_3_question_5_title.place(x=225, y=200)

quiz_3_question_5_choices = CTkLabel(quizpage_3, text = "a) avoid contact as much as possible\nb) Cover patient face with face mask before CPR\nc) Use oils and lotions on hands as a barrier to infection\nd) perform hands-only CPR")
quiz_3_question_5_choices.place(x=250, y=225)


quiz_3_question_5_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_5_entry.place(x=355, y=295)


# quiz 3 question 6 widgets
quiz_3_question_6_title = CTkLabel(quizpage_3, text = "6) What is illegal in\n relation to First Aid?", font=('arial bold', 12))
quiz_3_question_6_title.place(x=645, y=195)

quiz_3_question_6_choices = CTkLabel(quizpage_3, text = "a) not acting to administer CPR\nb) unconsensual treatment\nc) using excessive force\nd) unqualified first aid")
quiz_3_question_6_choices.place(x=610, y=225)


quiz_3_question_6_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_6_entry.place(x=645, y=295)


# quiz 3 question 7 widgets
quiz_3_question_7_title = CTkLabel(quizpage_3, text = "7) What does debriefing involve?", font=("arial bold", 12))
quiz_3_question_7_title.place(x=55, y=390)

quiz_3_question_7_choices = CTkLabel(quizpage_3, text = "a) obtaining info about the incident requiring aid\nb) informing a patient of treatment procedure\nc) notifying any bystanders of circumstance\nd) contacting medical services for patient")
quiz_3_question_7_choices.place(x=15, y=415)

quiz_3_question_7_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_7_entry.place(x=75, y=485)


# quiz 3 question 8 widgets
quiz_3_question_8_title = CTkLabel(quizpage_3, text = "1) What are the effects of administering\n first aid on mental health?", font=("arial bold", 12))
quiz_3_question_8_title.place(x=315, y=380)

quiz_3_question_8_choices = CTkLabel(quizpage_3, text = "a) anxiety\nb) paralysis\nc) low brain stimulation\nd) inability to regulate hormones")
quiz_3_question_8_choices.place(x=330, y=415)


quiz_3_question_8_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_8_entry.place(x=355, y=485)


# quiz 3 question 9 widgets
quiz_3_question_9_title = CTkLabel(quizpage_3, text = "9) What is a method that can help\n first aiders deal with mental health?", font=("arial bold", 12))
quiz_3_question_9_title.place(x=580, y=380)

quiz_3_question_9_choices = CTkLabel(quizpage_3, text = "a) practicing treatment\nb) mentoring other first aiders\nc) medications\nd) counselling")
quiz_3_question_9_choices.place(x=600, y=415)

quiz_3_question_9_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_9_entry.place(x=645, y=485)


# quiz 3 question 10 widgets
quiz_3_question_10_title = CTkLabel(quizpage_3, text = "10) Hepatitis consists of which three viruses?", font=("arial bold", 12))
quiz_3_question_10_title.place(x=5, y=550)

quiz_3_question_10_choices = CTkLabel(quizpage_3, text = "a) Hepatitis A, Hepatitis C and Hepatitis D \nb) Hepatitis B, Hepatitis C and Hepatitis D\nc) Hepatitis A, Hepatitis B and Hepatitis E\nd) Hepatitis A, Hepatitis B and Hepatitis C ")
quiz_3_question_10_choices.place(x=5, y=575)


quiz_3_question_10_entry = CTkEntry(quizpage_3, width=100)
quiz_3_question_10_entry.place(x=75, y=645)


# marking quiz 3


def quiz_3_marking():
    score = 0
    if quiz_3_question_1_entry.get() == "c":
        score = score + 1
    if quiz_3_question_2_entry.get() == "d":
        score = score + 1
    if quiz_3_question_3_entry.get() == "b":
        score = score + 1
    if quiz_3_question_4_entry.get() == "b":
        score = score + 1
    if quiz_3_question_5_entry.get() == "b":
        score = score + 1
    if quiz_3_question_6_entry.get() == "d":
        score = score + 1
    if quiz_3_question_7_entry.get() == "a":
        score = score + 1
    if quiz_3_question_8_entry.get() == "a":
        score = score + 1
    if quiz_3_question_9_entry.get() == "d":
        score = score + 1
    if quiz_3_question_10_entry.get() == "d":
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

