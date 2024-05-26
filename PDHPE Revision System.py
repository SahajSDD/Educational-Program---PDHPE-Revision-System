from tkinter import *
from customtkinter import *
import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3
from quiz_data_1 import quiz_data_1
from quiz_data_2 import quiz_data_2
from quiz_data_3 import quiz_data_3
from tkinter import messagebox, ttk

root = customtkinter.CTk()
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

# Small Size Function
def small():
    set_widget_scaling(0.75)
    root.minsize(600, 525)
    root.geometry("350x500")

# Medium Size Function
def medium():
    set_widget_scaling(1.0)
    root.minsize(800, 700)
    root.geometry("800x700")

# Large Size Function
def large():
    set_widget_scaling(1.05)
    root.minsize(800, 700)
    root.geometry("800x700")

# Switching Pages

# Removes any possible page on the screen packs the homepage back onto screen
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

# Opens Lesson Page
def lesson():
    lessonpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

# Opens Quiz List
def quiz(): 
    quizpage.pack(fill="both", expand = 1)
    homepage.pack_forget()

# Opens Scenario List
def scenario():
    scenariopage.pack(fill="both", expand = 1)
    homepage.pack_forget()

# opens lesson 1 page
def begin_lesson_1():
    lessonpage.pack_forget()
    lessonpage_1.pack(fill="both", expand = 1)

# opens lesson 2 page
def begin_lesson_2():
    lessonpage.pack_forget()
    lessonpage_2.pack(fill="both", expand = 1)

# opens lesson 3 page
def begin_lesson_3():
    lessonpage.pack_forget()
    lessonpage_3.pack(fill="both", expand = 1)

# opens quiz 2 page
def begin_quiz_1():
    quizpage.pack_forget()
    quizpage_1.pack(fill="both", expand = 1)

# opens quiz 2 page  
def begin_quiz_2():
    quizpage.pack_forget()
    quizpage_2.pack(fill="both", expand = 1)

# opens quiz 3 page
def begin_quiz_3():
    quizpage.pack_forget()
    quizpage_3.pack(fill="both", expand = 1)

# opens scenario 1 page
def begin_scenario_1():
    scenariopage.pack_forget()
    scenariopage_1.pack(fill="both", expand = 1)

# opens scenario 2 page
def begin_scenario_2():
    scenariopage.pack_forget()
    scenariopage_2.pack(fill="both", expand = 1)

# opens scenario 3 page
def begin_scenario_3():
    scenariopage.pack_forget()
    scenariopage_3.pack(fill="both", expand = 1)

# text to speech functions

# reads content on homepage
def homepage_tts():
    engine = pyttsx3.init()
    engine.say("PDHPE Revision System, First Aid, Lesson, Quiz, Scenario")
    engine.runAndWait()

# reads content on lesson page
def lessonpage_tts():
    engine = pyttsx3.init()
    engine.say("Lesson List, Inquiry Question 1: What are the main priorities for assessment and management of first aid patients, Inquiry Question 2: How should the major types of injuries and medical conditions be managed in first aid situations?, Inquiry Question 3: What does the individual need to consider in administering first aid?")
    engine.runAndWait()

# reads content on quiz page
def quizpage_tts():
    engine = pyttsx3.init()
    engine.say("Quiz List, Inquiry Question 1 Quiz, Inquiry Question 2 Quiz, Inquiry Question 3 Quiz")
    engine.runAndWait()

# reads content on scenario page
def scenariopage_tts():
    engine = pyttsx3.init()
    engine.say("Scenario List, Scenario 1, Scenario 2, Scenario 3")
    engine.runAndWait()

# reads lesson 1
def lessonpage_1_tts():
    # placing all text from widgets in an array
    lessonpage_1_content = ["Inquiry Question 1 Lesson", "When arriving at a scene of an incident in which First Aid is required, the first person's safety that should be ensured is yourself. Following this you should ensure the safety of the casualty and then any bystanders.", "DRSABCD", "The basic life management plan for First Aid is DRSABCD: Danger: Remove any elements of danger or future harm Response: Communicate to the casualty using the COWS method. Also involves recovery position (opens airways) Send for Help: Contact 000 or 112 Airways: Clear casualty's airways by scooping any foreign material out of their mouth Breathing: Look, listen and feel for breathing CPR: If not breathinng then, 30 Chest Compressions and 2 breaths Defibrillator: A device used when a casualty's heart stops beating", "Movement Methods", "There are four movement methods when moving a casualty, these are: Drag Method: Used when casualty is unconscious Human Crutch: Used when casualty is conscious but cannot walk Four Handed Seat: Requires two people to cross arms and use as a seat for casualty Chair Lift: Casualty sits on chair and two people lift chair to move", "STOP Regime", "The STOP regime is a method developed to assess the extent to the athelete's injury, it includes: Stop: Stop the athlete from moving Talk: Talk the athlete Observe: Observe athelete and injury site Prevent: Prevent Further Injury", "Bleeding", "The Treatment for Bleeding is PER management system which stands for: Pressure: Apply direct pressure to the wound using a bandage Elevate: Lie patient down and lift injured part above level of the heart Rest: Do not move injured part (apply bandage at this stage", "Shock", "Shock is a condition where the body closes off the blood off to the extremeties(arms and legs). Causes include: - heart attack - loss of fluids - loss of blood", "Neck and Spine", ". A neck or spine injury can be detrimental to a casualty. To ensure it doesn't lead to further injury such as paralysis, treatment must be done correctly. It differs from an unconscious and conscious patient: Conscious: Calm patient and loosen clothing, place neck and spine in neutral position and apply cerival collar if possible, contact 000 Unconscious: DRSABCD, place patient in recovery position and immobilise spine and neck, maintain open airway, contact 000", "Medical Referral", "A patient needs to be referred to professional medical serivces if either CPR needed to be performed or a serious conditons such a spine injury or heart attack is suspected. When informing 000, try to remember answer questions such as: - What happend? - How many casualties? - What injuries have they sustained? - What action have you taken? - What is the location" ]
    engine = pyttsx3.init()
    # engine.say() can only read up to 2-3 variables, for loop runs through the array so that all variables can be read
    for i in lessonpage_1_content:
        engine.say(i)
        engine.runAndWait()

# reads lesson 2
def lessonpage_2_tts():
    # placing all text from widgets in an array
    lessonpage_2_content = ["Inquiry Question 2", "Cuts and Lacerations", "The basic treatment for most cuts and lacerations include: - Sterilise wound - Apply pressure to wound - DRSABCD if necessary", "Fractures and Dislocations", "The basic treatment for most cuts and lacerations include: - DRSABCD - Apply sling or splint - Seek further medical attention - Apply Ice", "Head Injuries and Concussions", "The basic treatment for head injuries and concussions include: - DRSABCD - Support head or neck - Lay in lateral position - If skull fracture is suspected, do not apply pressure to head", "Burns", "The basic treatment for burns include: - Remove the casualty from the danger (fire, electrical wire) - DRSABCD - Hold Burnt are under cool running water - Remove any jewellery or clothing if its not stuck to skin - Do not break blisters or apply creams or dressings", "Chest Injuries", "Chest injuries can range from bruised or fractured ribs to lung injuries. The basic treatment for chest injuries include: - Place in a comfortable position - Encourage shallow breathing - Pad the injured area - Seek urgent medical advice", "Heart Attack and Stroke", "Heart attacks and strokes are life threatening conditions where blood supply is blocked to the heart and brain. When adressing a patient experiencing a heart attack or stroke, the best treatment is DRSABCD and seeking medical help", "Asthma", "Asthma is a conditon characterised by breathing difficulties due to the constriction of airways in the lungs. The basic treatment for asthma include: - Assisting with medication (puffer) - Monitor Breathing - Provide water to drink - Encourage controlled and relaxed breathing", "Diabetes", "Diabetes is a conditon where the body is unable to produce or regulate the insulin required to maintain regualar blood sugar levels. There are two types. Hypogycaemia (low blood sugar) and Hyperglycaemia (high blood sugar). The basic treatment for HYPOGLYCAEMIA includes: - DRSABCD - If conscious, administer glucose or a drink The basic treatment for HYPERGLYCAEMIA is: - DRSABCD - If conscious, allow for the self administration of insulin", "Epileptic Seizures", "Characterised by wild uncontrollled spasms of the body, the basic treatment for epileptic seizures include: - DRSABCD - Lateral recovery position - Remove dangerous objects around patient - Do not attempt to restrain patient", "Anaphylaxis", "Anaphylaxis is a severe allergic reaction to an allergen (such as nuts or bee stings). The basic treatment for anaphylaxis is: - DRSABCD - Remove the trigger - Administer Epipen - Seek Medical Help", "Poisons", "Poisoning should be handled with DRSABCD, but also the type of poison should be identified as well. The type of poison determines whether or not vomiting should be induced: - If substance is unknown or corrosive do not induce vomiting - If substance is medicinal or general, induce vomiting", "Bites and Stings", "The treatment for bites and stings differs on the animals that caused it. Generally the treatment for SNAKE BITES includes: - DRSABCD - Apply a pressure immobilisation bandage - Do not elevate - Call for medical help The basic treatment for INSECT BITES includes: - Remove stinger by scraping or flicking - Apply ice - Monitor for allergic reactions", "Hyperthermia", "Hyperthermia is an over exposure to heat. It can be characterised as heat stroke or heat exhaustion. The treatment for hyperthermia includes - DRSABCD - Rest in shade - Provide plenty of water - Cool the body with ice and wet towels", "Hypothermia", "Hypothermia is an over exposure to the cold. The basic treatment for hypothermia includes: - DRSABCD - Protect from the elements (wind, rain) - Remove any wet clothing and replace with warm blankets - Do not use artificial heating measures"]
    engine = pyttsx3.init()
    # engine.say() can only read up to 2-3 variables, for loop runs through the array so that all variables can be read
    for i in lessonpage_2_content:
        engine.say(i)
        engine.runAndWait()

# reads lesson 3
def lessonpage_3_tts():
    # placing all text from widgets in an array
    lessonpage_3_content = ["Inquiry Question 3", "Traffic Accidents", "When a rescuer arrives at a traffic accidents, strategies to help manage the situation and prevent further harm include: - Turning hazard lights on - sending a person up the road to warn traffic - Turn Ignition off - Light area with low beam if incident occurred at night - Contact medical help or roadside assistance", "Water Environment", "When performing a rescue in a water environment, a rescuer must be aware of: - Their own physical limitations - changes in weather - Hazardous objects under the water - Water temperature Protective strategies include: - Using ropes, branches, floatation devices - Sending for help immediately - Ensuring you can perform rescue without putting self at risk", "Electricity", "When performing a rescue in an environment with a live wire, strategies that should be utilised include: - Not touching objects that are in contact with electrical source - Turning off electricity at source - Not immediately touching and treating patient", "HIV, AIDS and Blood Borne Diseases", "HIV, AIDs and Blood Borne Diseases(hepatitis a, b, c) are diseases that can be transmitted during first aid treatment through contact with bodily fluids such as: - blood - semen - faces - mucus - vomit - saliva To prevent transmission, strategies that can be used include: - Using gloves - Cover casualty face with face mask before CPR - Wash hands before and after treatment", "Legal Implications", "In regard to First Aid, in law you face no litigation: - If you do not administer first aid to a casualty - If you use excessive force (appropriately) - If treatment was unconsensual (patient was unconscious)", "Debriefing", "DEBRIEFING is the process of obtaining information about the incident in which first aid was required. The rescuer will have to answer questions about what happened and describe the nature of the incident COUNSELLING is defined as services designed to help rescuers deal with the trauma experiences during treatment. If left untreated, rescuers can suffer from anxiety and depression"]
    engine = pyttsx3.init()
    # engine.say() can only read up to 2-3 variables, for loop runs through the array so that all variables can be read
    for i in lessonpage_3_content:
        engine.say(i)
        engine.runAndWait()

# reads scenario 1 description
def scenario_1_description_tts():
    engine = pyttsx3.init()
    engine.say("Scenario 1 Description, Johnny was playing near the lit gas stove. As he jumped around he leant over the stove and touched the open flame with his right arm. It appears as red and rashy and Johnny complains of an intense, sharp pain. He then passes out from exhaustion.")
    engine.runAndWait()

# reads scenario 1 questions
def scenario_1_questions_tts():
    scenario_1_questions = ["1) What Primary Injury has Johhny Suffered?", "a) Heart Attack b) Hyperthermia c) General Burns d) Shock", "2) How should the Primary injury be treated?", "a) Epipen b) Running hands under Cool Water c) Immediate Bandaging d) Lotions and Oils", "3) As Johnny has passed out, what is the first priority?", "a) Tend to Primary Injury b) Roll into Recovery Position c) Check for Breathing d) Turn off Stove", "4) Gas and smoke begin to fill the room, How should Johnny be carried out?", "a) Chair Lift Method b) Four-Handed Seat d) Any method is applicable d) Drag Method", "5) Is Medical Referal Necessary?", "a) Yes, in all cases b) No, there is no reason to c) Decided by Patient d) Unsure", "6) You were the only person around when Johhny got injured, Are you legally obliged to assist?", "a) Yes b) No c) If it were a situation of life or death d) Unsure"]
    engine = pyttsx3.init()
    for i in scenario_1_questions:
        engine.say(i)
        engine.runAndWait()

# reads scenario 2 description
def scenario_2_description_tts():
    engine = pyttsx3.init()
    engine.say("Scenario 2 Description, You are on a walking track at a park when you notice a young girl yelling for help. Upon inspection, you notice that she has two identical punctures next to each other on her leg.The area surrounding it has gone red and puffy.She says she cannot walk, and says the pain is immense. There are visible stingers protruding from the punctures.")
    engine.runAndWait()

# reads scenario 2 questions
def scenario_2_questions_tts():
    scenario_2_questions = [ "1) What is the girl's injury?", "a) Snake Bite b) Insect Sting c) Bleeding (stabbed) d) Leg Fracture", "2) Due to the puffiness and rashes around the wound what else may have occurred?", "a) Anaphylactic Reaction b) Burns c) Bruising d) Nervous Response", "3) How would you first treat the primary injury?", "a) Wetten Wound b) Bandage Wound c) Remove the Stingers d) Apply Blister Cream", "4) What medical instrument may be used in this treatment?", "a) Green Whistle b) Surgical Knife c) Medical Brush d) Epipen", "5) Assume the girl passes out, what should you do?", "a) Check for Breathing b) Check Pulse c) Shake Girl Awake Call Out for Help", "6) She regains consciousness and you call 000 for help, what part of DRSABCD is this?", "a) Danger b) Response c) Send for Help d) Airways"]
    engine = pyttsx3.init()
    for i in scenario_2_questions:
        engine.say(i)
        engine.runAndWait()


# reads scenario 3 description
def scenario_3_description_tts():
    engine = pyttsx3.init()
    engine.say("Scenario 3 Description" + "You are out near a lake during winter, when you notice a man has fallen in. He manages to get out but is shivering and battling consciousness At this point in time it is also raining. You are the only person around at the time.")
    engine.runAndWait()

# reads scenario 3 questions
def scenario_3_questions_tts():
    scenario_3_questions = ["1) What condition can be associated with this man?", "a) Hyperthermia b) Hypothermia c) Coldstroke d) Shock", "2) What is the First Step of Treatment?", "a) Cover Man in Warm Garments b) Check his Breathing c) Seek Shelter from Rain d) Ask him How This Happened", "3) From Question 2, What Part of DRSABCD is this?", "a) Danger b) Response c) Breathing d) CPR", "4) What Treatment is Most Appropriate?", "a) Provide Blankets and Garments b) Provide a Lighter c) Provide Cool Water d) Provide Electric Heating", "5) The patient seems to still be struggling, but breathing is regular, is CPR necessary?", "a) Yes b) No c) Ask the Patient d) Unsure", "What else can be done for the patient?", "a) Encourage Passive Movement b) Directly Applying Heat c) Remove Wet Clothing d) Wrap Yourself Around Patient"]
    engine = pyttsx3.init()
    for i in scenario_3_questions:
        engine.say(i)
        engine.runAndWait()

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

homepage_tts_button = CTkButton(homepage, text = "Read Page Aloud", command = homepage_tts, width=50, height=50)
homepage_tts_button.place(x=600, y=200)

# Widgets for Lesson Page (lesson list)
lessonpage_title = CTkLabel(lessonpage, text="Lesson List", font=("arial", 25))
lessonpage_title.place(x=350, y=25)

lesson_1 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 1: What are the main priorities for assessment and management of first aid patients?", command=begin_lesson_1)
lesson_1.place(x=0, y=200)
lesson_2 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 2: How should the major types of injuries and medical conditions be managed in first aid situations?", command=begin_lesson_2)
lesson_2.place(x=0, y=300)
lesson_3 = CTkButton(lessonpage, width=800, height=100, text="Inquiry Question 3: What does the individual need to consider in administering first aid?", command=begin_lesson_3)
lesson_3.place(x=0, y=400) 

lessonpage_tts_button = CTkButton(lessonpage, text = "Read Page Aloud", command = lessonpage_tts)
lessonpage_tts_button.place(x=550, y = 25)

# Widgets for Quiz Page (quiz list)
quizpage_title = CTkLabel(quizpage, text="Quiz List", font=("arial", 25))
quizpage_title.place(x=350, y=25)

quiz_1 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 1 Quiz", command= begin_quiz_1)
quiz_1.place(x=0, y=200)
quiz_2 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 2 Quiz", command= begin_quiz_2)
quiz_2.place(x=0, y=300)
quiz_3 = CTkButton(quizpage, width=800, height=100, text="Inquiry Question 3 Quiz", command= begin_quiz_3)
quiz_3.place(x=0, y=400) 

quizpage_tts_button = CTkButton(quizpage, text = "Read Page Aloud", command = quizpage_tts)
quizpage_tts_button.place(x=550, y = 25)

# Widgets for Scenario Page (scenario list)

scenariopage_title = CTkLabel(scenariopage, text="Scenario List", font=("arial", 25))
scenariopage_title.place(x=350, y=25)

scenario_1 = CTkButton(scenariopage, width=800, height=100, text="Scenario 1", command= begin_scenario_1)
scenario_1.place(x=0, y=200)
scenario_2 = CTkButton(scenariopage, width=800, height=100, text="Scenario 2", command= begin_scenario_2)
scenario_2.place(x=0, y=300)
scenario_3 = CTkButton(scenariopage, width=800, height=100, text="Scenario 3", command= begin_scenario_3)
scenario_3.place(x=0, y=400) 

scenariopage_tts_button = CTkButton(scenariopage, text = "Read Page Aloud", command = scenariopage_tts)
scenariopage_tts_button.place(x = 550, y =25)


# scrollbars for lessonpages

scroll_frame_1 = customtkinter.CTkScrollableFrame(lessonpage_1)
scroll_frame_1.pack(fill = BOTH, expand = 1)

scroll_frame_2 = customtkinter.CTkScrollableFrame(lessonpage_2)
scroll_frame_2.pack(fill = BOTH, expand = 1)

scroll_frame_3 = customtkinter.CTkScrollableFrame(lessonpage_3)
scroll_frame_3.pack(fill = BOTH, expand = 1)



# Lesson 1 text

lesson_1_title = CTkLabel(scroll_frame_1, text = "Inquiry Question 1 Lesson", font=("arial bold", 20),justify ="left", anchor = W )
lesson_1_title.pack()
                     
priority_content = CTkLabel(scroll_frame_1, text="When arriving at a scene of an incident in which First Aid is required, the first person's safety that should be ensured is yourself.\n Following this you should ensure the safety of the casualty and then any bystanders.", justify = "left", anchor = W)
priority_content.pack()

DRSABCD_title = CTkLabel(scroll_frame_1, text = "DRSABCD", font=("arial bold", 14), justify ="left", anchor = W)
DRSABCD_title.pack()

DRSABCD_content = CTkLabel(scroll_frame_1, text = "The basic life management plan for First Aid is DRSABCD:\n Danger: Remove any elements of danger or future harm\nResponse: Communicate to the casualty using the COWS method. Also involves recovery position (opens airways) \nSend for Help: Contact 000 or 112\n Airways: Clear casualty's airways by scooping any foreign material out of their mouth\n Breathing: Look, listen and feel for breathing\n CPR: If not breathinng then, 30 Chest Compressions and 2 breaths\n Defibrillator: A device used when a casualty's heart stops beating", justify="left")
DRSABCD_content.pack()

movement_method_title = CTkLabel(scroll_frame_1, text = "Movement Methods",font=("arial bold", 14), justify = "left")
movement_method_title.pack()

movement_method_content = CTkLabel(scroll_frame_1, text="There are four movement methods when moving a casualty, these are:\n Drag Method: Used when casualty is unconscious\nHuman Crutch: Used when casualty is conscious but cannot walk\nFour Handed Seat: Requires two people to cross arms and use as a seat for casualty\nChair Lift: Casualty sits on chair and two people lift chair to move", justify = "left")
movement_method_content.pack()

STOP_title = CTkLabel(scroll_frame_1, text = "STOP Regime", font = ("arial bold", 14) )
STOP_title.pack()

STOP_content = CTkLabel(scroll_frame_1, text = "The STOP regime is a method developed to assess the extent to the athelete's injury, it includes:\n Stop: Stop the athlete from moving\nTalk: Talk the athlete\n Observe: Observe athelete and injury site\n Prevent: Prevent Further Injury", justify = "left")
STOP_content.pack()

bleeding_content = CTkLabel(scroll_frame_1, text = "Bleeding",font=("arial bold", 14))
bleeding_content.pack()
                            
bleeding_title = CTkLabel(scroll_frame_1, text = "The Treatment for Bleeding is PER management system which stands for:\n Pressure: Apply direct pressure to the wound using a bandage\n Elevate: Lie patient down and lift injured part above level of the heart\nRest: Do not move injured part (apply bandage at this stage", justify = "left")
bleeding_title.pack()

shock_title = CTkLabel(scroll_frame_1, text = "Shock", font=("arial bold", 14))
shock_title.pack()

shock_content = CTkLabel(scroll_frame_1, text = "Shock is a condition where the body closes off the blood off to the extremeties(arms and legs). Causes include:\n- heart attack\n- loss of fluids\n- loss of blood", justify = "left")
shock_content.pack()

neck_and_spine_title = CTkLabel(scroll_frame_1, text = "Neck and Spine", font=("arial bold", 14))
neck_and_spine_title.pack()

neck_and_spine_content = CTkLabel(scroll_frame_1, text=". A neck or spine injury can be detrimental to a casualty. To ensure it doesn't lead to\n further injury such as paralysis, treatment must be done correctly. It differs from an unconscious and conscious patient:\n Conscious: Calm patient and loosen clothing, place neck and spine in neutral position and apply cerival collar if possible, contact 000\n Unconscious: DRSABCD, place patient in recovery position and immobilise spine and neck, maintain open airway, contact 000", justify = "left")
neck_and_spine_content.pack()

medical_referral_title = CTkLabel(scroll_frame_1, text="Medical Referral", font=("arial bold", 14))
medical_referral_title.pack()

medical_referral_content = CTkLabel(scroll_frame_1, text="A patient needs to be referred to professional medical serivces if either CPR needed to be performed or a serious conditons\n such a spine injury or heart attack is suspected. When informing 000, try to remember answer questions such as:\n- What happend?\n- How many casualties?\n- What injuries have they sustained?\n- What action have you taken?\n- What is the location", justify="left")
medical_referral_content.pack()

# Lesson 1 Text to Speech

lessonpage_1_tts_button = CTkButton(scroll_frame_1, text = "Read Page Aloud", command = lessonpage_1_tts)
lessonpage_1_tts_button.place(x = 0 , y = 0)

# Lesson 2 text
lesson_2_title = CTkLabel(scroll_frame_2, text = "Inquiry Question 2",font=("arial bold", 20))
lesson_2_title.pack()

cuts_and_lacerations_title = CTkLabel(scroll_frame_2, text= "Cuts and Lacerations",font=("arial bold", 14))
cuts_and_lacerations_title.pack()

cuts_and_lacerations_content = CTkLabel(scroll_frame_2, text = "The basic treatment for most cuts and lacerations include:\n- Sterilise wound\n- Apply pressure to wound\n- DRSABCD if necessary", justify = "left" )
cuts_and_lacerations_content.pack()

fractures_and_dislocations_title = CTkLabel(scroll_frame_2, text = "Fractures and Dislocations", font=("arial bold", 14))
fractures_and_dislocations_title.pack()

fractures_and_dislocations_content = CTkLabel(scroll_frame_2, text="The basic treatment for most cuts and lacerations include:\n- DRSABCD\n- Apply sling or splint\n- Seek further medical attention\n- Apply Ice", justify="left")
fractures_and_dislocations_content.pack()

head_injuries_and_concussions_title = CTkLabel(scroll_frame_2, text = "Head Injuries and Concussions", font =("arial bold" ,14))
head_injuries_and_concussions_title.pack()

head_injuries_and_concussions_content = CTkLabel(scroll_frame_2, text = "The basic treatment for head injuries and concussions include:\n- DRSABCD\n- Support head or neck\n- Lay in lateral position\n- If skull fracture is suspected, do not apply pressure to head", justify="left")
head_injuries_and_concussions_content.pack()

burns_title = CTkLabel(scroll_frame_2, text = "Burns", font=("arial bold", 14))
burns_title.pack()

burns_content = CTkLabel(scroll_frame_2, text ="The basic treatment for burns include:\n- Remove the casualty from the danger (fire, electrical wire)\n- DRSABCD\n- Hold Burnt are under cool running water\n- Remove any jewellery or clothing if its not stuck to skin\n- Do not break blisters or apply creams or dressings",justify="left")
burns_content.pack()

chest_injuries_title = CTkLabel(scroll_frame_2, text = "Chest Injuries", font=("arial bold", 14))
chest_injuries_title.pack()

chest_injuries_content = CTkLabel(scroll_frame_2, text = "Chest injuries can range from bruised or fractured ribs to lung injuries. The basic treatment for chest injuries include:\n- Place in a comfortable position\n- Encourage shallow breathing\n- Pad the injured area\n- Seek urgent medical advice")
chest_injuries_content.pack()

heart_attack_and_stroke_title = CTkLabel(scroll_frame_2, text = "Heart Attack and Stroke", font=("arial bold", 14))
heart_attack_and_stroke_title.pack()

heart_attack_and_stroke_content = CTkLabel(scroll_frame_2, text="Heart attacks and strokes are life threatening conditions where blood supply is blocked to the heart and brain. When adressing a patient\n experiencing a heart attack or stroke, the best treatment is DRSABCD and seeking medical help", justify="left")
heart_attack_and_stroke_content.pack()

asthma_title = CTkLabel(scroll_frame_2, text = "Asthma", font=("arial bold", 14))
asthma_title.pack()

asthma_content = CTkLabel(scroll_frame_2, text = "Asthma is a conditon characterised by breathing difficulties due to the constriction of airways in the lungs.\n The basic treatment for asthma include:\n- Assisting with medication (puffer)\n- Monitor Breathing\n- Provide water to drink\n- Encourage controlled and relaxed breathing")
asthma_content.pack()

diabetes_title = CTkLabel(scroll_frame_2, text = "Diabetes", font=("arial bold", 14))
diabetes_title.pack()

diabetes_content = CTkLabel(scroll_frame_2, text = "Diabetes is a conditon where the body is unable to produce or regulate the insulin required\n to maintain regualar blood sugar levels. There are two types. Hypogycaemia (low blood sugar) and Hyperglycaemia (high blood sugar).\n The basic treatment for HYPOGLYCAEMIA includes:\n- DRSABCD\n- If conscious, administer glucose or a drink\n The basic treatment for HYPERGLYCAEMIA is:\n- DRSABCD\n- If conscious, allow for the self administration of insulin")
diabetes_content.pack()

epileptic_seizures_title = CTkLabel(scroll_frame_2, text = "Epileptic Seizures", font=("arial bold", 14))
epileptic_seizures_title.pack()

epileptic_seizures_content = CTkLabel(scroll_frame_2, text = "Characterised by wild uncontrollled spasms of the body, the basic treatment for epileptic seizures include:\n- DRSABCD\n- Lateral recovery position\n- Remove dangerous objects around patient\n- Do not attempt to restrain patient")
epileptic_seizures_content.pack()

anapylaxis_title = CTkLabel(scroll_frame_2, text = "Anaphylaxis", font=("arial bold", 14))
anapylaxis_title.pack()

anaphylaxis_content = CTkLabel(scroll_frame_2, text = "Anaphylaxis is a severe allergic reaction to an allergen (such as nuts or bee stings). The basic treatment for anaphylaxis is:\n- DRSABCD\n- Remove the trigger\n- Administer Epipen\n- Seek Medical Help")
anaphylaxis_content.pack()

poisons_title = CTkLabel(scroll_frame_2, text = "Poisons", font=("arial bold", 14))
poisons_title.pack()

poisons_content = CTkLabel(scroll_frame_2, text = "Poisoning should be handled with DRSABCD, but also the type of poison should be identified as well. The type of poison determines\n whether or not vomiting should be induced:\n- If substance is unknown or corrosive do not induce vomiting\n- If substance is medicinal or general, induce vomiting")
poisons_content.pack()

bites_and_stings_title = CTkLabel(scroll_frame_2, text = "Bites and Stings", font=("arial bold", 14))
bites_and_stings_title.pack()

bites_and_stings_content = CTkLabel(scroll_frame_2, text="The treatment for bites and stings differs on the animals that caused it. Generally the treatment for SNAKE BITES includes:\n- DRSABCD\n- Apply a pressure immobilisation bandage\n- Do not elevate\n- Call for medical help\n The basic treatment for INSECT BITES includes:\n- Remove stinger by scraping or flicking\n- Apply ice\n- Monitor for allergic reactions")
bites_and_stings_content.pack()

hyperthermia_title = CTkLabel(scroll_frame_2, text = "Hyperthermia", font=("arial bold", 14))
hyperthermia_title.pack()

hyperthermia_content = CTkLabel(scroll_frame_2, text = "Hyperthermia is an over exposure to heat. It can be characterised as heat stroke or heat exhaustion. The treatment for hyperthermia includes\n- DRSABCD\n- Rest in shade\n- Provide plenty of water\n- Cool the body with ice and wet towels")
hyperthermia_content.pack()

hypothermia_title = CTkLabel(scroll_frame_2, text ="Hypothermia", font=("arial bold", 14))
hypothermia_title.pack()

hypothermia_content = CTkLabel(scroll_frame_2, text = "Hypothermia is an over exposure to the cold. The basic treatment for hypothermia includes:\n- DRSABCD\n- Protect from the elements (wind, rain)\n- Remove any wet clothing and replace with warm blankets\n- Do not use artificial heating measures")
hypothermia_content.pack()

# Lesson 2 Text to Speech

lessonpage_2_tts_button = CTkButton(scroll_frame_2, text = "Read Page Aloud", command = lessonpage_2_tts)
lessonpage_2_tts_button.place(x = 0 , y = 0)

# Lesson 3 text
lesson_3_title = CTkLabel(scroll_frame_3, text = "Inquiry Question 3",font=("arial bold", 20))
lesson_3_title.pack()

traffic_accidents_title = CTkLabel(scroll_frame_3, text = "Traffic Accidents", font=("arial bold", 14))
traffic_accidents_title.pack()

traffic_accidents_content = CTkLabel(scroll_frame_3, text = "When a rescuer arrives at a traffic accidents, strategies to help manage the situation and prevent further harm include:\n- Turning hazard lights on\n- sending a person up the road to warn traffic\n- Turn Ignition off\n- Light area with low beam if incident occurred at night\n- Contact medical help or roadside assistance")
traffic_accidents_content.pack()

water_environment_title = CTkLabel(scroll_frame_3, text = "Water Environment", font=("arial bold", 14))
water_environment_title.pack()

water_environment_content =  CTkLabel(scroll_frame_3, text = "When performing a rescue in a water environment, a rescuer must  be aware of:\n- Their own physical limitations\n- changes in weather\n- Hazardous objects under the water\n- Water temperature\n Protective strategies include:\n- Using ropes, branches, floatation devices\n- Sending for help immediately\n- Ensuring you can perform rescue without putting self at risk")
water_environment_content.pack()

electricity_title = CTkLabel(scroll_frame_3, text = "Electricity",font=("arial bold", 14) )
electricity_title.pack()

electricity_content = CTkLabel(scroll_frame_3, text = "When performing a rescue in an environment with a live wire, strategies that should be utilised include:\n- Not touching objects that are in contact with electrical source\n- Turning off electricity at source\n- Not immediately touching and treating patient")
electricity_content.pack()

hiv_aids_blood_borne_title = CTkLabel(scroll_frame_3, text = "HIV, AIDS and Blood Borne Diseases", font=("arial bold", 14))
hiv_aids_blood_borne_title.pack()

hiv_aids_blood_borne_content = CTkLabel(scroll_frame_3, text = "HIV, AIDs and Blood Borne Diseases(hepatitis a, b, c) are diseases that can be transmitted during first aid treatment through contact with bodily fluids such as:\n- blood\n- semen\n- faces\n- mucus\n- vomit\n- saliva\n To prevent transmission, strategies that can be used include:\n- Using gloves\n- Cover casualty face with face mask before CPR\n- Wash hands before and after treatment")
hiv_aids_blood_borne_content.pack()

legal_implications_title = CTkLabel(scroll_frame_3, text = "Legal Implications", font=('arial bold', 14))
legal_implications_title.pack()

legal_implications_content = CTkLabel(scroll_frame_3, text="In regard to First Aid, in law you face no litigation:\n- If you do not administer first aid to a casualty\n- If you use excessive force (appropriately)\n- If treatment was unconsensual (patient was unconscious)")
legal_implications_content.pack()

debriefing_and_counselling_title = CTkLabel(scroll_frame_3, text="Debriefing", font=("arial bold", 14))
debriefing_and_counselling_title.pack()

debriefing_and_counselling_content = CTkLabel(scroll_frame_3, text="DEBRIEFING is the process of obtaining information about the incident in which first aid was required.\n The rescuer will have to answer questions about what happened and describe the nature of the incident\n COUNSELLING is defined as services designed to help rescuers deal with the trauma experiences during treatment.\n If left untreated, rescuers can suffer from anxiety and depression")
debriefing_and_counselling_content.pack()

# Lesson 3 Text to Speech

lessonpage_3_tts_button = CTkButton(scroll_frame_3, text = "Read Page Aloud", command = lessonpage_3_tts)
lessonpage_3_tts_button.place(x=0, y=0)

# Quiz 1 System (including marking)


# Function to display the current question and choices
def quiz_1_show_question():
    global question_1
    question_1 = quiz_data_1[quiz_1_current_question]
    quiz_1_question_label.configure(text=question_1["question"])
    
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
quiz_1_question_label = CTkLabel(quizpage_1, anchor="center")
quiz_1_question_label.pack(pady=10)

# Create the choice buttons
quiz_1_choice_buttons = []
for i in range(4):
    button_1 = CTkButton(quizpage_1, height = 100, width = 200, command=lambda i=i: quiz_1_check_answer(i))
    button_1.pack(pady=5)
    quiz_1_choice_buttons.append(button_1)

# text to speech button for questions
text_to_speech_1 = CTkButton(quizpage_1, text="Read Question Aloud", command = quiz_1_tts)
text_to_speech_1.pack()

# Create the feedback label, score label and next buttom
quiz_1_feedback_label = CTkLabel(quizpage_1,anchor="center")
quiz_1_feedback_label.pack(pady=10)

quiz_1_score_label = CTkLabel(quizpage_1, text="Score: 0/{}".format(len(quiz_data_1)),anchor="center")
quiz_1_score_label.pack(pady=10)

quiz_1_next_button = CTkButton(quizpage_1, text="Next", command=next_question_1, state="disabled")
quiz_1_next_button.pack(pady=10)

# Initialise score and current question
quiz_1_score = 0
quiz_1_current_question = 0

# Show First Question
quiz_1_show_question()

# Quiz 2 System (including marking)

# Function to display the current question and choices
def quiz_2_show_question():
    global question_2
    question_2 = quiz_data_2[quiz_2_current_question]
    quiz_2_question_label.configure(text=question_2["question"])
   
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
quiz_2_question_label = CTkLabel(quizpage_2, anchor="center")
quiz_2_question_label.pack(pady=10)

# Create the choice buttons
quiz_2_choice_buttons = []
for i in range(4):
    button_2 = CTkButton(quizpage_2, height = 100, width = 200, command=lambda i=i: quiz_2_check_answer(i))
    button_2.pack(pady=5)
    quiz_2_choice_buttons.append(button_2)

# text to speech button for questions
text_to_speech_2 = CTkButton(quizpage_2, text="Read Question Aloud", command = quiz_2_tts)
text_to_speech_2.pack()

# Create the feedback label, score label and next button
quiz_2_feedback_label = CTkLabel(quizpage_2,anchor="center")
quiz_2_feedback_label.pack(pady=10)

quiz_2_score_label = CTkLabel(quizpage_2, text="Score: 0/{}".format(len(quiz_data_2)),anchor="center")
quiz_2_score_label.pack(pady=10)

quiz_2_next_button = CTkButton(quizpage_2, text="Next", command=next_question_2, state="disabled")
quiz_2_next_button.pack(pady=10)

# Initialise score and current question
quiz_2_score = 0
quiz_2_current_question = 0

# Show First Question
quiz_2_show_question()

# Quiz 3 System (including marking)

# Shows the current question and choice buttons
def quiz_3_show_question():
    global question_3
    question_3 = quiz_data_3[quiz_3_current_question]
    quiz_3_question_label.configure(text=question_3["question"])
   
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
quiz_3_question_label = CTkLabel(quizpage_3, anchor="center")
quiz_3_question_label.pack(pady=10)

# Create the choice buttons
quiz_3_choice_buttons = []
for i in range(4):
    button_3 = CTkButton(quizpage_3, height = 100, width = 300, command=lambda i=i: quiz_3_check_answer(i))
    button_3.pack(pady=5)
    quiz_3_choice_buttons.append(button_3)

# text to speech button for questions
text_to_speech_3 = CTkButton(quizpage_3, text="Read Question Aloud", command = quiz_3_tts)
text_to_speech_3.pack()

# Create the feedback label, score label and next button
quiz_3_feedback_label = CTkLabel(quizpage_3,anchor="center")
quiz_3_feedback_label.pack(pady=10)

quiz_3_score_label = CTkLabel(quizpage_3, text="Score: 0/{}".format(len(quiz_data_3)),anchor="center")
quiz_3_score_label.pack(pady=10)

quiz_3_next_button = CTkButton(quizpage_3, text="Next", command=next_question_3, state="disabled")
quiz_3_next_button.pack(pady=10)

# Initialise score and current question
quiz_3_score = 0
quiz_3_current_question = 0

# Show First Question
quiz_3_show_question()

# widgets for scenario 1

scenario_1_description_title = CTkLabel(scenariopage_1, text = "Scenario 1 Description:", font = ("arial bold", 20))
scenario_1_description_title.place(x = 15, y = 10)

scenario_1_description = CTkLabel(scenariopage_1, text = "Johnny was playing near the lit gas stove.\nAs he jumped around he leant over the stove and touched the open flame\nwith his right arm. It appears as red and rashy and Johnny complains\nof an intense, sharp pain. He then passes out from exhaustion." )
scenario_1_description.place( x = 10, y = 50)

# scenario 1 text to speech buttons

scenario_1_description_button = CTkButton(scenariopage_1, text = "Read Scenario Description Aloud", command = scenario_1_description_tts)
scenario_1_description_button.place(x = 550, y = 50 )

scenario_1_questions_tts_button = CTkButton(scenariopage_1, text = "Read Questions Aloud", command = scenario_1_questions_tts)
scenario_1_questions_tts_button.place(x = 550, y = 100)

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
    global scenario_1_score
    scenario_1_score = 0
    # checks if inputs to answers are a b c or d, if not an error comes up and stops marking
    valid_answers = {"a", "b", "c", "d", ""}
    for i in {scenario_1_question_1_entry, scenario_1_question_2_entry, scenario_1_question_3_entry, scenario_1_question_4_entry, scenario_1_question_5_entry, scenario_1_question_6_entry}:
        current_answer = i.get()
        if current_answer not in valid_answers:
            messagebox.showerror("Error", "Invalid Input. Please Enter Valid Answer (a, b, c, d)")
            return
    if scenario_1_question_1_entry.get() == "c" :
        scenario_1_score += 1
        scenario_1_feedback_1 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_1.place(x=60, y=300)
    else:
        scenario_1_feedback_1 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_1.place(x=15, y=300)

    if scenario_1_question_2_entry.get() == "b" :
        scenario_1_score += 1
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_2.place(x=350, y=300)
    else:
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_1_feedback_2.place(x=300, y=300)

    if scenario_1_question_3_entry.get() == "c" :
        scenario_1_score += 1
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_3.place(x=60, y=480)
    else:
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_3.place(x=15, y=480)

    if scenario_1_question_4_entry.get() == "d" :
        scenario_1_score += 1
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_4.place(x=350, y=480)
    else:
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_1_feedback_4.place(x=305, y=480)

    if scenario_1_question_5_entry.get() == "a" :
        scenario_1_score += 1
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_5.place(x=60, y=660)
    else:
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_1_feedback_5.place(x=15, y=660)

    if scenario_1_question_6_entry.get() == "b" :
        scenario_1_score += 1
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

scenario_2_description_title = CTkLabel(scenariopage_2, text = "Scenario 2 Description:", font = ("arial bold", 20))
scenario_2_description_title.place(x = 15, y = 10)

scenario_2_description = CTkLabel(scenariopage_2, text = "You are on a walking track at a park when you notice a young girl yelling for help.\nUpon inspection, you notice that she has two identical punctures next\n to eachother on her leg.The area surrounding it has gone red and puffy.\nShe says she cannot walk, and says the pain is immense.\n There are visible stingers protruding from the punctures." )
scenario_2_description.place( x = 10, y = 50)

# scenario 1 text to speech buttons

scenario_2_description_button = CTkButton(scenariopage_2, text = "Read Scenario Description Aloud", command = scenario_2_description_tts)
scenario_2_description_button.place(x = 550, y = 50 )

scenario_2_questions_tts_button = CTkButton(scenariopage_2, text = "Read Questions Aloud", command = scenario_2_questions_tts)
scenario_2_questions_tts_button.place(x = 550, y = 100)


# scenario 2 question 1 widgets

scenario_2_question_1_title = CTkLabel(scenariopage_2, text = "1) What is the girl's injury?", font = ("arial bold", 12))
scenario_2_question_1_title.place(x = 10, y = 175)

scenario_2_question_1_choices = CTkLabel(scenariopage_2, text = "a) Snake Bite\nb) Insect Sting\nc) Bleeding (stabbed) \nd) Leg Fracture")
scenario_2_question_1_choices.place(x = 10, y = 200)
                               
scenario_2_question_1_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_1_entry.place(x = 20, y = 270 )


# scenario 2 question 2 widgets

scenario_2_question_2_title = CTkLabel(scenariopage_2, text = "2) Due to the puffiness and rashes around the wound\n what else may have occured?", font = ("arial bold", 12))
scenario_2_question_2_title.place(x = 225, y = 165)
                               
scenario_2_question_2_choices = CTkLabel(scenariopage_2, text = "a) Anaphylactic Reaction\nb) Burns\nc) Bruising\nd) Nervous Response")
scenario_2_question_2_choices.place(x = 295, y = 200)

scenario_2_question_2_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_2_entry.place(x = 305, y = 270)


# scenario 2 question 3 widgets

scenario_2_question_3_title = CTkLabel(scenariopage_2, text = "3) How would you first\n treat the primary injury?", font=("arial bold", 12))
scenario_2_question_3_title.place(x = 10, y = 340)
                               
scenario_2_question_3_title = CTkLabel(scenariopage_2, text = "a) Wetten Wound\nb) Bandage Wound \nc) Remove the Stingers\nd) Apply Blister Cream")
scenario_2_question_3_title.place(x = 10, y = 375)

scenario_2_question_3_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_3_entry.place(x = 20, y = 445)


# scenario 2 question 4 widgets

scenario_2_question_4_title = CTkLabel(scenariopage_2, text = "4) What medical instrument may\n be used in this treatment?", font=("arial bold", 12))
scenario_2_question_4_title.place(x = 260, y = 340)

scenario_2_question_4_choices = CTkLabel(scenariopage_2, text = "a) Green Whistle\nb) Surgical Knife\nc) Medical Brush\nd) Epipen")
scenario_2_question_4_choices.place(x = 300, y = 375)
                               
scenario_2_question_4_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_4_entry.place(x = 305, y = 445)


# scenario 2 question 5 widgets

scenario_2_question_5_title = CTkLabel(scenariopage_2, text = "5) Assume the girl passes out,\n what should you do?", font=("arial bold", 12))
scenario_2_question_5_title.place(x = 10, y = 515)

scenario_2_question_5_choices = CTkLabel(scenariopage_2, text = "a) Check for Breathing\n b) Check Pulse\n c) Shake Girl Awake\n Call Out for Help")
scenario_2_question_5_choices.place(x = 10, y = 555)
                               
scenario_2_question_5_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_5_entry.place(x = 20, y = 620)

# scenario 2 question 6 widgets

scenario_2_question_6_title = CTkLabel(scenariopage_2, text = "6) She regains consciousness and you call\n 000 for help, what part of DRSABCD is this?", font=("arial bold", 12))
scenario_2_question_6_title.place(x = 260, y = 515)

scenario_2_question_6_title = CTkLabel(scenariopage_2, text = "a) Danger\nb) Response\nc) Send for Help\nd) Airways")
scenario_2_question_6_title.place(x = 300, y = 550)     

scenario_2_question_6_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_6_entry.place(x = 305, y = 620)

# scenario 2 image
Scenario_2_Image = Image.open("Scenario_2_Image.jpg").resize((300, 300))
image_tk = ImageTk.PhotoImage(Scenario_2_Image)
image_label_2 = tk.Label(scenariopage_2, text="", image = image_tk)
image_label_2.image = image_tk
image_label_2.place(x=650, y=240)

# scenario 2 marking

def scenario_2_marking():
    global scenario_2_score
    scenario_2_score = 0
    # checks if inputs to answers are a b c or d, if not an error comes up and stops marking 
    valid_answers = {"a", "b", "c", "d", ""}    
    for i in {scenario_2_question_1_entry, scenario_2_question_2_entry, scenario_2_question_3_entry, scenario_2_question_4_entry, scenario_2_question_5_entry, scenario_2_question_6_entry}:
        current_answer = i.get()
        if current_answer not in valid_answers:
            messagebox.showerror("Error", "Invalid Input. Please Enter Valid Answer (a, b, c, d)")
            return
    if scenario_2_question_1_entry.get() == "b" :
        scenario_2_score += 1
        scenario_2_feedback_1 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_1.place(x=60, y=300)
    else:
        scenario_2_feedback_1 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_2_feedback_1.place(x=15, y=300)
    if scenario_2_question_2_entry.get() == "a" :
        scenario_2_score += 1
        scenario_2_feedback_2 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_2.place(x=350, y=300)
    else:
        scenario_2_feedback_2 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_2_feedback_2.place(x=300, y=300)
    if scenario_2_question_3_entry.get() == "c" :
        scenario_2_score += 1
        scenario_2_feedback_3 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_3.place(x=60, y=480)
    else:
        scenario_2_feedback_3 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_2_feedback_3.place(x=15, y=480)
    if scenario_2_question_4_entry.get() == "d" :
        scenario_2_score += 1
        scenario_2_feedback_4 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_4.place(x=350, y=480)
    else:
        scenario_2_feedback_4 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_2_feedback_4.place(x=305, y=480)
    if scenario_2_question_5_entry.get() == "a" :
        scenario_2_score += 1
        scenario_2_feedback_5 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_5.place(x=60, y=660)
    else:
        scenario_2_feedback_5 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_2_feedback_5.place(x=15, y=660)
    if scenario_2_question_6_entry.get() == "c" :
        scenario_2_score += 1
        scenario_2_feedback_6 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_6.place(x=350, y=660)
    else:
        scenario_2_feedback_6 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_2_feedback_6.place(x=305, y=660)
    scenario_2_result_label = CTkLabel(scenariopage_2, text=f"Your Score is : {scenario_2_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_2_result_label.place(x = 600, y = 550)


# scenario 2 submit button

scenario_2_submit = CTkButton(scenariopage_2, text = "Submit", command = scenario_2_marking)
scenario_2_submit.place(x = 600, y = 620)

# widgets for scenario 3

scenario_3_description_title = CTkLabel(scenariopage_3, text = "Scenario 3 Description:", font = ("arial bold", 20))
scenario_3_description_title.place(x = 15, y = 10)

scenario_3_description = CTkLabel(scenariopage_3, text = " You are out near a lake during winter, when you notice a man has fallen\nin. He manages to get out but is shivering and battling consciousness\n At this point in time it is also raining. You are the only person around at the time." )
scenario_3_description.place( x = 10, y = 50)

# scenario 1 text to speech buttons

scenario_3_description_button = CTkButton(scenariopage_3, text = "Read Scenario Description Aloud", command = scenario_3_description_tts)
scenario_3_description_button.place(x = 550, y = 50 )

scenario_3_questions_tts_button = CTkButton(scenariopage_3, text = "Read Questions Aloud", command = scenario_3_questions_tts)
scenario_3_questions_tts_button.place(x = 550, y = 100)

# scenario 3 question 1 widgets

scenario_3_question_1_title = CTkLabel(scenariopage_3, text = "1) What condition can be\n associated with this man?", font=("arial bold", 12))
scenario_3_question_1_title.place(x = 10, y = 165)

scenario_3_question_1_choices = CTkLabel(scenariopage_3, text = "a) Hyperthermia\nb) Hypothermia\nc) Coldstroke\nd) Shock")
scenario_3_question_1_choices.place(x = 30, y = 200)
                               
scenario_3_question_1_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_1_entry.place(x = 20, y = 270 )


# scenario 3 question 2 widgets

scenario_3_question_2_title = CTkLabel(scenariopage_3, text = "2) What is the First Step of Treatment?", font=("arial bold", 12))
scenario_3_question_2_title.place(x = 260, y = 175)

scenario_3_question_2_choices = CTkLabel(scenariopage_3, text = "a) Cover Man in Warm Garments\n b) Check his Breathing\n c) Seek Shelter from Rain\n d) Ask him How This Happened")
scenario_3_question_2_choices.place(x = 260, y = 200)

scenario_3_question_2_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_2_entry.place(x = 305, y = 270)


# scenario 3 question 3 widgets

scenario_3_question_3_title = CTkLabel(scenariopage_3, text = "3) From Question 2, What Part of\n DRSABCD is this?", font=("arial bold", 12))
scenario_3_question_3_title.place(x = 5 , y = 340)

scenario_3_question_3_choices = CTkLabel(scenariopage_3, text = "a) Danger\nb) Response\nc) Breathing\nd) CPR")
scenario_3_question_3_choices.place(x = 30, y = 375)
                                         
scenario_3_question_3_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_3_entry.place(x = 20, y = 445)


# scenario 3 question 4 widgets

scenario_3_question_4_title = CTkLabel(scenariopage_3, text = "4) What Treatment is Most Appropriate?", font=("arial bold", 12))
scenario_3_question_4_title.place(x = 260, y = 350)

scenario_3_question_4_choices = CTkLabel(scenariopage_3, text = "a) Provide Blankets and Garments\nb) Provide a Lighter \nc) Provide Cool Water\nd) Provide Electric Heating")
scenario_3_question_4_choices.place(x = 260, y = 375)

scenario_3_question_4_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_4_entry.place(x = 305, y = 445)

# scenario 3 question 5 widgets

scenario_3_question_5_title = CTkLabel(scenariopage_3, text = "5) The patient seems to still\n be struggling, but breathing is\n regular, is CPR necessary?",font=("arial bold", 12) )
scenario_3_question_5_title.place(x = 10, y = 505)

scenario_3_question_5_choices = CTkLabel(scenariopage_3, text = "a) Yes\nb) No\nc) Ask the Patient\nd) Unsure")
scenario_3_question_5_choices.place(x = 10, y = 550)                
                               
scenario_3_question_5_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_5_entry.place(x = 20, y = 620)


# scenario 3 question 6 widgets

scenario_3_question_6_title = CTkLabel(scenariopage_3, text = "What else can be done for the patient?",font=("arial bold", 12) )
scenario_3_question_6_title.place(x = 260, y = 525)

scenario_3_question_6_choices = CTkLabel(scenariopage_3, text = "a) Encourage Passive Movement\nb) Directly Applying Heat\nc) Remove Wet Clothing\nd) Wrap Yourself Around Patient")
scenario_3_question_6_choices.place(x = 260, y = 550)
                               
scenario_3_question_6_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_6_entry.place(x = 305, y = 620)

# scenario 3 image
Scenario_3_Image = Image.open("Scenario_3_Image.jpg").resize((300, 300))
image_tk = ImageTk.PhotoImage(Scenario_3_Image)
image_label_3 = tk.Label(scenariopage_3, text="", image = image_tk)
image_label_3.image = image_tk
image_label_3.place(x=650, y=240)



# scenario 3 marking

def scenario_3_marking():
    global scenario_3_score
    scenario_3_score = 0
    # checks if inputs to answers are a b c or d, if not an error comes up and stops marking 
    valid_answers = {"a", "b", "c", "d", ""}
    for i in {scenario_3_question_1_entry, scenario_3_question_2_entry, scenario_3_question_3_entry, scenario_3_question_4_entry, scenario_3_question_5_entry, scenario_3_question_6_entry}:
        current_answer = i.get()
        if current_answer not in valid_answers:
            messagebox.showerror("Error", "Invalid Input. Please Enter Valid Answer (a, b, c, d)")
            return
    if scenario_3_question_1_entry.get() == "b" :
        scenario_3_score += 1
        scenario_3_feedback_1 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_1.place(x=60, y=300)
    else:
        scenario_3_feedback_1 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_3_feedback_1.place(x=15, y=300)
    if scenario_3_question_2_entry.get() == "c" :
        scenario_3_score += 1
        scenario_3_feedback_2 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_2.place(x=350, y=300)
    else:
        scenario_3_feedback_2 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_3_feedback_2.place(x=300, y=300)
    if scenario_3_question_3_entry.get() == "d" :
        scenario_3_score += 1
        scenario_3_feedback_3 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_3.place(x=60, y=475)
    else:
        scenario_3_feedback_3 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_3_feedback_3.place(x=15, y=475)
    if scenario_3_question_4_entry.get() == "a" :
        scenario_3_score += 1
        scenario_3_feedback_4 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_4.place(x=350, y=480)
    else:
        scenario_3_feedback_4 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_3_feedback_4.place(x=305, y=480)
    if scenario_3_question_5_entry.get() == "b" :
        scenario_3_score += 1
        scenario_3_feedback_5 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_5.place(x=60, y=660)
    else:
        scenario_3_feedback_5 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_3_feedback_5.place(x=15, y=660)
    if scenario_3_question_6_entry.get() == "c" :
        scenario_3_score += 1
        scenario_3_feedback_6 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_6.place(x=350, y=660)
    else:
        scenario_3_feedback_6 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_3_feedback_6.place(x=305, y=660)
    scenario_3_result_label = CTkLabel(scenariopage_3, text=f"Your Score is : {scenario_3_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_3_result_label.place(x = 600, y = 550)


# scenario 3 submit button

scenario_3_submit = CTkButton(scenariopage_3, text = "Submit", command = scenario_3_marking)
scenario_3_submit.place(x = 600, y = 620)

# menubar

menubar = Menu(root)
root.configure(menu=menubar)

menuhome = Menu(menubar, tearoff = 0)
menusize = Menu(menubar, tearoff = 0)
menutheme = Menu(menubar, tearoff = 0)

menubar.add_cascade(label="Home", menu=menuhome)
menubar.add_cascade(label="Size", menu=menusize)
menubar.add_cascade(label="Theme", menu=menutheme)

# dropdowns for menubars

menuhome.add_cascade(label="Home", command = home)
menusize.add_command(label = "Small", command = small)
menusize.add_command(label = "Medium", command = medium)
menusize.add_command(label = "Large", command = large)

menutheme.add_command(label = "Dark", command=lambda: set_appearance_mode("dark"))
menutheme.add_command(label = "Light", command=lambda: set_appearance_mode("light"))

root.resizable(height=False, width=False)
    
root.mainloop()

