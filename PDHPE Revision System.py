from tkinter import *
from customtkinter import *
import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3
from lesson_data_1 import lesson_data_1
from lesson_data_2 import lesson_data_2
from lesson_data_3 import lesson_data_3
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

# different scenario pages
scenariopage_1 = CTkFrame(root, width= 400, height = 400)
scenariopage_2 = CTkFrame(root, width= 400, height = 400)
scenariopage_3 = CTkFrame(root, width= 400, height = 400)

# result pages for scenarios
scenario_1_resultpage = CTkFrame(root,width = 400, height = 400)
scenario_2_resultpage = CTkFrame(root,width = 400, height = 400)
scenario_3_resultpage = CTkFrame(root,width = 400, height = 400)

# resize and move images

def resize_and_move_scenario_image_1(new_width_1, new_height_1, new_x_1, new_y_1):
    
    resized_image_1 = Scenario_1_Image.resize((new_width_1, new_height_1))
    
    # Update the PhotoImage object
    global image_tk_1
    image_tk_1 = ImageTk.PhotoImage(resized_image_1)
    image_label_1.configure(image=image_tk_1)
    
    # Move the label to the new position
    image_label_1.place(x=new_x_1, y=new_y_1)

def resize_and_move_scenario_image_2(new_width_2, new_height_2, new_x_2, new_y_2):
    resized_image_2 = Scenario_2_Image.resize((new_width_2, new_height_2))
    
    # Update the PhotoImage object
    global image_tk_2
    image_tk_2 = ImageTk.PhotoImage(resized_image_2)
    image_label_2.configure(image=image_tk_2)
    
    # Move the label to the new position
    image_label_2.place(x=new_x_2, y=new_y_2)

def resize_and_move_scenario_image_3(new_width_3, new_height_3, new_x_3, new_y_3):
    resized_image_3 = Scenario_3_Image.resize((new_width_3, new_height_3))
    
    # Update the PhotoImage object
    global image_tk_3
    image_tk_3 = ImageTk.PhotoImage(resized_image_3)
    image_label_3.configure(image=image_tk_3)
    
    # Move the label to the new position
    image_label_3.place(x=new_x_3, y=new_y_3)

# commands for theme

def dark_theme():
    set_appearance_mode("dark")
    bg_light_label_homepage.place_forget()
    bg_light_label_lessonpage.place_forget()
    bg_light_label_lessonpage_1.place_forget()
    bg_light_label_lessonpage_2.place_forget()
    bg_light_label_lessonpage_3.place_forget()
    bg_light_label_quizpage.place_forget()
    bg_light_label_quizpage_1.place_forget()
    bg_light_label_quizpage_2.place_forget()
    bg_light_label_quizpage_3.place_forget()
    bg_light_label_scenariopage.place_forget()
    bg_light_label_scenariopage_1.place_forget()
    bg_light_label_scenariopage_2.place_forget()
    bg_light_label_scenariopage_3.place_forget()
    bg_dark_label_homepage.place(x=0, y=0)
    bg_dark_label_lessonpage.place(x = 0, y = 0)
    bg_dark_label_lessonpage_1.place(x = 0, y = 0)
    bg_dark_label_lessonpage_2.place(x = 0, y = 0)
    bg_dark_label_lessonpage_3.place(x = 0, y = 0)
    bg_dark_label_quizpage.place(x = 0, y = 0)
    bg_dark_label_quizpage_1.place(x = 0, y = 0)
    bg_dark_label_quizpage_2.place(x = 0, y = 0)
    bg_dark_label_quizpage_3.place(x = 0, y = 0)
    bg_dark_label_scenariopage.place(x = 0, y = 0)
    bg_dark_label_scenariopage_1.place(x = 0, y = 0)
    bg_dark_label_scenariopage_2.place(x = 0, y = 0)
    bg_dark_label_scenariopage_3.place(x = 0, y = 0)

    
def light_theme():
    set_appearance_mode("light")
    bg_dark_label_homepage.place_forget()
    bg_dark_label_lessonpage.place_forget()
    bg_dark_label_lessonpage_1.place_forget()
    bg_dark_label_lessonpage_2.place_forget()
    bg_dark_label_lessonpage_3.place_forget()
    bg_dark_label_quizpage.place_forget()
    bg_dark_label_quizpage_1.place_forget()
    bg_dark_label_quizpage_2.place_forget()
    bg_dark_label_quizpage_3.place_forget()
    bg_dark_label_scenariopage.place_forget()
    bg_dark_label_scenariopage_1.place_forget()
    bg_dark_label_scenariopage_2.place_forget()
    bg_dark_label_scenariopage_3.place_forget()
    bg_light_label_homepage.place(x=0, y=0)
    bg_light_label_lessonpage.place(x = 0, y = 0)
    bg_light_label_lessonpage_1.place(x = 0, y = 0)
    bg_light_label_lessonpage_2.place(x = 0, y = 0)
    bg_light_label_lessonpage_3.place(x = 0, y = 0)
    bg_light_label_quizpage.place(x = 0, y = 0)
    bg_light_label_quizpage_1.place(x = 0, y = 0)
    bg_light_label_quizpage_2.place(x = 0, y = 0)
    bg_light_label_quizpage_3.place(x = 0, y = 0)
    bg_light_label_scenariopage.place(x = 0, y = 0)
    bg_light_label_scenariopage_1.place(x = 0, y = 0)
    bg_light_label_scenariopage_2.place(x = 0, y = 0)
    bg_light_label_scenariopage_3.place(x = 0, y = 0)




# commands for size

# Small Size Function
def small():
    set_widget_scaling(0.75)
    root.minsize(600, 525)
    root.geometry("350x500")
    resize_and_move_scenario_image_1(200, 200, 500, 200)
    resize_and_move_scenario_image_2(200, 200, 500, 200)
    resize_and_move_scenario_image_3(200, 200, 500, 200)

# Medium Size Function
def medium():
    set_widget_scaling(1.0)
    root.minsize(800, 700)
    root.geometry("800x700")
    resize_and_move_scenario_image_1(300, 300, 650, 200)
    resize_and_move_scenario_image_2(300, 300, 650, 200)
    resize_and_move_scenario_image_3(300, 300, 650, 200)

# Large Size Function
def large():
    set_widget_scaling(1.05)
    root.minsize(850, 750)
    root.geometry("850x750")
    resize_and_move_scenario_image_1(350, 350, 675, 200)
    resize_and_move_scenario_image_2(350, 350, 675, 200)
    resize_and_move_scenario_image_3(350, 350, 675, 200)

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

# back buttons

def lessonpage_to_homepage():
    lessonpage.pack_forget()
    homepage.pack(fill="both", expand = 1)

def quizpage_to_homepage():
    quizpage.pack_forget()
    homepage.pack(fill="both", expand = 1)

def quiz_1_to_quizpage():
    quizpage_1.pack_forget()
    quizpage.pack(fill="both", expand = 1)
    global quiz_1_score, quiz_1_current_question
    quiz_1_score = 0
    quiz_1_current_question = 0
    quiz_1_score_label.configure(text="Score: 0/{}".format(len(quiz_data_1)))
    quiz_1_show_question()

def quiz_2_to_quizpage():
    quizpage_2.pack_forget()
    quizpage.pack(fill="both", expand = 1)
    global quiz_2_score, quiz_2_current_question
    quiz_2_score = 0
    quiz_2_current_question = 0
    quiz_2_score_label.configure(text="Score: 0/{}".format(len(quiz_data_2)))
    quiz_2_show_question()

def quiz_3_to_quizpage():
    quizpage_3.pack_forget()
    quizpage.pack(fill="both", expand = 1)
    global quiz_3_score, quiz_3_current_question
    quiz_3_score = 0
    quiz_3_current_question = 0
    quiz_3_score_label.configure(text="Score: 0/{}".format(len(quiz_data_3)))
    quiz_3_show_question()
    
def scenariopage_to_homepage():
    scenariopage.pack_forget()
    homepage.pack(fill="both", expand = 1)

def scenario_1_to_scenariopage():
    scenariopage_1.pack_forget()
    scenariopage.pack(fill="both", expand = 1)
    global scenario_1_feedback_1
    global scenario_1_feedback_2
    global scenario_1_feedback_3
    global scenario_1_feedback_4
    global scenario_1_feedback_5
    global scenario_1_feedback_6
    global scenario_1_result_label
    scenario_1_feedback_1.place_forget()
    scenario_1_feedback_2.place_forget()
    scenario_1_feedback_3.place_forget()
    scenario_1_feedback_4.place_forget()
    scenario_1_feedback_5.place_forget()
    scenario_1_feedback_6.place_forget()
    scenario_1_result_label.place_forget()
    
    


def scenario_2_to_scenariopage():
    scenariopage_2.pack_forget()
    scenariopage.pack(fill="both", expand = 1)
    global scenario_2_feedback_1
    global scenario_2_feedback_2
    global scenario_2_feedback_3
    global scenario_2_feedback_4
    global scenario_2_feedback_5
    global scenario_2_feedback_6
    global scenario_2_result_label
    scenario_2_feedback_1.place_forget()
    scenario_2_feedback_2.place_forget()
    scenario_2_feedback_3.place_forget()
    scenario_2_feedback_4.place_forget()
    scenario_2_feedback_5.place_forget()
    scenario_2_feedback_6.place_forget()
    scenario_2_result_label.place_forget()

def scenario_3_to_scenariopage():
    scenariopage_3.pack_forget()
    scenariopage.pack(fill="both", expand = 1)
    global scenario_3_feedback_1
    global scenario_3_feedback_2
    global scenario_3_feedback_3
    global scenario_3_feedback_4
    global scenario_3_feedback_5
    global scenario_3_feedback_6
    global scenario_3_result_label
    scenario_3_feedback_1.place_forget()
    scenario_3_feedback_2.place_forget()
    scenario_3_feedback_3.place_forget()
    scenario_3_feedback_4.place_forget()
    scenario_3_feedback_5.place_forget()
    scenario_3_feedback_6.place_forget()
    scenario_3_result_label.place_forget()

# backgrounds

# dark backgrounds

bg_dark = Image.open("Dark Background.png").resize((1100, 1100))
bg_dark_tk = ImageTk.PhotoImage(bg_dark)

bg_dark_label_homepage = CTkLabel(homepage, text = "", image = bg_dark_tk)

bg_dark_label_lessonpage = CTkLabel(lessonpage, text = "", image = bg_dark_tk)

bg_dark_label_lessonpage_1 = CTkLabel(lessonpage_1, text = "", image = bg_dark_tk)

bg_dark_label_lessonpage_2 = CTkLabel(lessonpage_2, text = "", image = bg_dark_tk)

bg_dark_label_lessonpage_3 = CTkLabel(lessonpage_3, text = "", image = bg_dark_tk)

bg_dark_label_quizpage = CTkLabel(quizpage, text = "", image = bg_dark_tk)

bg_dark_label_quizpage_1 = CTkLabel(quizpage_1, text = "", image = bg_dark_tk)

bg_dark_label_quizpage_2 = CTkLabel(quizpage_2, text = "", image = bg_dark_tk)

bg_dark_label_quizpage_3 = CTkLabel(quizpage_3, text = "", image = bg_dark_tk)

bg_dark_label_scenariopage = CTkLabel(scenariopage, text = "", image = bg_dark_tk)

bg_dark_label_scenariopage_1 = CTkLabel(scenariopage_1, text = "", image = bg_dark_tk)

bg_dark_label_scenariopage_2 = CTkLabel(scenariopage_2, text = "", image = bg_dark_tk)

bg_dark_label_scenariopage_3 = CTkLabel(scenariopage_3, text = "", image = bg_dark_tk)


# light backgrounds

bg_light = Image.open("Light Background.jpg").resize((1100, 1100))
bg_light_tk = ImageTk.PhotoImage(bg_light)

bg_light_label_homepage = CTkLabel(homepage, text = "", image = bg_light_tk)

bg_light_label_lessonpage = CTkLabel(lessonpage, text = "", image = bg_light_tk)

bg_light_label_lessonpage_1 = CTkLabel(lessonpage_1, text = "", image = bg_light_tk)

bg_light_label_lessonpage_2 = CTkLabel(lessonpage_2, text = "", image = bg_light_tk)

bg_light_label_lessonpage_3 = CTkLabel(lessonpage_3, text = "", image = bg_light_tk)

bg_light_label_quizpage = CTkLabel(quizpage, text = "", image = bg_light_tk)

bg_light_label_quizpage_1 = CTkLabel(quizpage_1, text = "", image = bg_light_tk)

bg_light_label_quizpage_2 = CTkLabel(quizpage_2, text = "", image = bg_light_tk)

bg_light_label_quizpage_3 = CTkLabel(quizpage_3, text = "", image = bg_light_tk)

bg_light_label_scenariopage = CTkLabel(scenariopage, text = "", image = bg_light_tk)

bg_light_label_scenariopage_1 = CTkLabel(scenariopage_1, text = "", image = bg_light_tk)

bg_light_label_scenariopage_2 = CTkLabel(scenariopage_2, text = "", image = bg_light_tk)

bg_light_label_scenariopage_3 = CTkLabel(scenariopage_3, text = "", image = bg_light_tk)



# dark theme is default
dark_theme()

# speech icon image for text to speech
tts_icon = Image.open("speech_icon.png").resize((20, 20))
image_tk_4 = ImageTk.PhotoImage(tts_icon)

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

homepage_tts_button = CTkButton(homepage, text = "", image = image_tk_4, command = homepage_tts, width=50, height=50)
homepage_tts_button.place(x=600, y=200)

# Widgets for Lesson Page (lesson list)
lessonpage_title = CTkLabel(lessonpage, text="Lesson List", font=("Arial bold", 25),)
lessonpage_title.place(x=340, y=25)

lesson_1 = CTkButton(lessonpage, width=200, height=100, text="Inquiry Question 1", font=("Arial bold", 15), command=begin_lesson_1)
lesson_1.place(x=305, y=150)
lesson_2 = CTkButton(lessonpage, width=200, height=100, text="Inquiry Question 2", font=("Arial bold", 15), command=begin_lesson_2)
lesson_2.place(x=305, y=300)
lesson_3 = CTkButton(lessonpage, width=200, height=100, text="Inquiry Question 3", font=("Arial bold", 15), command=begin_lesson_3)
lesson_3.place(x=305, y=450) 

lessonpage_tts_button = CTkButton(lessonpage, text = "", image = image_tk_4, command = lessonpage_tts)
lessonpage_tts_button.place(x=550, y = 25)

lessonpage_back_button = CTkButton(lessonpage, text = "Back", command = lessonpage_to_homepage)
lessonpage_back_button.place(x = 50, y = 600)

# Widgets for Quiz Page (quiz list)
quizpage_title = CTkLabel(quizpage, text="Quiz List", font=("Arial bold", 25),)
quizpage_title.place(x=350, y=25)

quiz_1 = CTkButton(quizpage, width=200, height=100, text="Inquiry Question 1 Quiz", font=("Arial bold", 15), command= begin_quiz_1)
quiz_1.place(x=305, y=150)
quiz_2 = CTkButton(quizpage, width=200, height=100, text="Inquiry Question 2 Quiz", font=("Arial bold", 15), command= begin_quiz_2)
quiz_2.place(x=305, y=300)
quiz_3 = CTkButton(quizpage, width=200, height=100, text="Inquiry Question 3 Quiz", font=("Arial bold", 15), command= begin_quiz_3)
quiz_3.place(x=305, y=450) 

quizpage_tts_button = CTkButton(quizpage, text = "", image = image_tk_4, command = quizpage_tts)
quizpage_tts_button.place(x=550, y = 25)

quizpage_back_button = CTkButton(quizpage, text = "Back", command = quizpage_to_homepage)
quizpage_back_button.place(x=50, y=600)

# Widgets for Scenario Page (scenario list)

scenariopage_title = CTkLabel(scenariopage, text="Scenario List", font=("Arial bold", 25),)
scenariopage_title.place(x=330, y=25)

scenario_1 = CTkButton(scenariopage, width=200, height=100, text="Scenario 1", font=("Arial bold", 15), command= begin_scenario_1)
scenario_1.place(x=305, y=150)
scenario_2 = CTkButton(scenariopage, width=200, height=100, text="Scenario 2", font=("Arial bold", 15), command= begin_scenario_2)
scenario_2.place(x=305, y=300)
scenario_3 = CTkButton(scenariopage, width=200, height=100, text="Scenario 3", font=("Arial bold", 15), command= begin_scenario_3)
scenario_3.place(x=305, y=450) 

scenariopage_tts_button = CTkButton(scenariopage, image = image_tk_4, text = "", command = scenariopage_tts)
scenariopage_tts_button.place(x = 550, y =25)

scenariopage_back_button = CTkButton(scenariopage, text = "Back", command = scenariopage_to_homepage)
scenariopage_back_button.place(x=50, y=600)

# Lesson 1 text

# Function to display the current lesson title and content
def lesson_1_show_lesson():
    global lesson_1_temp 
    lesson_1_temp = lesson_data_1[lesson_1_current_lesson]
    lesson_1_title.configure(text = lesson_1_temp["title"])
    lesson_1_content.configure(text = lesson_1_temp["content"])
    lesson_1_tts_button.place(x = 650, y = 50)

# Function to move to the next question
def next_lesson_1():
    global lesson_1_current_lesson
    lesson_1_current_lesson += 1
    if lesson_1_current_lesson < len(lesson_data_1):
        # If there are more lessons, show the next lesson
        lesson_1_show_lesson()
    else:
        # If there are no more lessons, exit back to lesson list
        lessonpage_1.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_1_current_lesson = 0
        lesson_1_show_lesson()

# Function to move to the previous question
def previous_lesson_1():
    global lesson_1_current_lesson
    lesson_1_current_lesson -= 1
    if lesson_1_current_lesson >= 0:
        # If there are preivous lessons, show the previous lesson
        lesson_1_show_lesson()
    else:
        # If there are no previous lessons (at first lesson), exit back to the lesson list
        lessonpage_1.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_1_current_lesson = 0
        lesson_1_show_lesson()

# Reads the current lesson title and content
def lesson_1_tts():
    engine = pyttsx3.init()
    # remove \n newline operators from content so it isn't read out
    lesson_1_processed_text = lesson_1_temp["content"].replace("\n", ".")
    # all content to be spoke is put into an array
    lesson_1_tts_content = [lesson_1_temp["title"], lesson_1_processed_text] 
    for i in lesson_1_tts_content:
        engine.say(i) 
        engine.runAndWait()

# Create Lesson Title
lesson_1_title = CTkLabel(lessonpage_1, text = "", font = ("arial bold", 25))
lesson_1_title.place(x = 50, y = 50 )

# Create Lesson Content
lesson_1_content = CTkLabel(lessonpage_1, text = "", font=("arial", 18), justify = LEFT)
lesson_1_content.place(x = 10, y = 200)

# Create Next Button, text to speech button and back button
lesson_1_next_button = CTkButton(lessonpage_1, text = "Next", command = next_lesson_1)
lesson_1_next_button.place(x = 650, y = 600)

lesson_1_tts_button = CTkButton(lessonpage_1, text = "", image = image_tk_4, command = lesson_1_tts)
lesson_1_tts_button.pack()

lesson_1_back_button = CTkButton(lessonpage_1, text = "Back", command = previous_lesson_1)
lesson_1_back_button.place(x = 10, y = 600)

# initialise current lesson
lesson_1_current_lesson = 0

# Show first Lesson
lesson_1_show_lesson()

# Lesson 2 text

# Function to display the current lesson title and content
def lesson_2_show_lesson():
    global lesson_2_temp
    lesson_2_temp = lesson_data_2[lesson_2_current_lesson]
    lesson_2_title.configure(text = lesson_2_temp["title"])
    lesson_2_content.configure(text = lesson_2_temp["content"])
    lesson_2_tts_button.place(x = 650, y = 50)

# Function to move to the next question
def next_lesson_2():
    global lesson_2_current_lesson
    lesson_2_current_lesson += 1
    if lesson_2_current_lesson < len(lesson_data_2):
        # If there are more lessons, show the next lesson
        lesson_2_show_lesson()
    else:
        # If there are no more lessons, exit back to lesson list
        lessonpage_2.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_2_current_lesson = 0
        lesson_2_show_lesson()

# Function to move to the previous question
def previous_lesson_2():
    global lesson_2_current_lesson
    lesson_2_current_lesson -= 1
    if lesson_2_current_lesson >= 0:
        # If there are preivous lessons, show the previous lesson
        lesson_2_show_lesson()
    else:
        # If there are no previous lessons (at first lesson), exit back to the lesson list
        lessonpage_2.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_2_current_lesson = 0
        lesson_2_show_lesson()

# Reads the current lesson title and content
def lesson_2_tts():
    engine = pyttsx3.init()
    # remove \n newline operators from content so it isn't read out
    lesson_2_processed_text = lesson_2_temp["content"].replace("\n", ".")
    # all content to be spoke is put into an array
    lesson_2_tts_content = [lesson_1_temp["title"], lesson_2_processed_text] 
    for i in lesson_2_tts_content:
        engine.say(i) 
        engine.runAndWait()

# Create Lesson Title
lesson_2_title = CTkLabel(lessonpage_2, text = "", font = ("arial bold", 25))
lesson_2_title.place(x = 50, y = 50 )

# Create Lesson Content
lesson_2_content = CTkLabel(lessonpage_2, text = "", font=("arial", 18), justify = LEFT)
lesson_2_content.place(x = 20, y = 200)

# Create Next Button, text to speech button and back button
lesson_2_next_button = CTkButton(lessonpage_2, text = "Next", command = next_lesson_2)
lesson_2_next_button.place(x = 650, y = 600)

lesson_2_tts_button = CTkButton(lessonpage_2, text = "", image = image_tk_4, command = lesson_2_tts)
lesson_2_tts_button.pack()

lesson_2_back_button = CTkButton(lessonpage_2, text = "Back", command = previous_lesson_2)
lesson_2_back_button.place(x = 20, y = 600)

# initialise current lesson
lesson_2_current_lesson = 0

# Show first Lesson
lesson_2_show_lesson()

# Lesson 3 text

# Function to display the current lesson title and content
def lesson_3_show_lesson():
    global lesson_3_temp
    lesson_3_temp = lesson_data_3[lesson_3_current_lesson]
    lesson_3_title.configure(text = lesson_3_temp["title"])
    lesson_3_content.configure(text = lesson_3_temp["content"])
    lesson_3_tts_button.place(x = 650, y = 50)

# Function to move to the next question
def next_lesson_3():
    global lesson_3_current_lesson
    lesson_3_current_lesson += 1
    if lesson_3_current_lesson < len(lesson_data_3):
        # If there are more lessons, show the next lesson
        lesson_3_show_lesson()
    else:
        # If there are no more lessons, exit back to lesson list
        lessonpage_3.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_3_current_lesson = 0
        lesson_3_show_lesson()

# Function to move to the previous question
def previous_lesson_3():
    global lesson_3_current_lesson
    lesson_3_current_lesson -= 1
    if lesson_3_current_lesson >= 0:
        # If there are preivous lessons, show the previous lesson
        lesson_3_show_lesson()
    else:
        # If there are no previous lessons (at first lesson), exit back to the lesson list
        lessonpage_3.pack_forget()
        lessonpage.pack(fill = BOTH, expand = 1)
        lesson_3_current_lesson = 0
        lesson_3_show_lesson()

# Reads the current lesson title and content
def lesson_3_tts():
    engine = pyttsx3.init()
    # remove \n newline operators from content so it isn't read out
    lesson_3_processed_text = lesson_3_temp["content"].replace("\n", ".")
    # all content to be spoke is put into an array
    lesson_3_tts_content = [lesson_3_temp["title"], lesson_3_processed_text] 
    for i in lesson_3_tts_content:
        engine.say(i) 
        engine.runAndWait()

# Create Lesson Title
lesson_3_title = CTkLabel(lessonpage_3, text = "", font = ("arial bold", 25))
lesson_3_title.place(x = 50, y = 50 )

# Create Lesson Content
lesson_3_content = CTkLabel(lessonpage_3, text = "", font=("arial", 18), justify = LEFT)
lesson_3_content.place(x = 20, y = 125)

# Create Next Button, text to speech button and back button
lesson_3_next_button = CTkButton(lessonpage_3, text = "Next", command = next_lesson_3)
lesson_3_next_button.place(x = 650, y = 600)

lesson_3_tts_button = CTkButton(lessonpage_3, text = "", image = image_tk_4, command = lesson_3_tts)
lesson_3_tts_button.pack()

lesson_3_back_button = CTkButton(lessonpage_3, text = "Back", command = previous_lesson_3)
lesson_3_back_button.place(x = 30, y = 600)

# initialise current lesson
lesson_3_current_lesson = 0

# Show first Lesson
lesson_3_show_lesson()

# Quiz 1 System (including marking)

# Function to display the current question and choices
def quiz_1_show_question():
    global quiz_1_temp
    quiz_1_temp = quiz_data_1[quiz_1_current_question]
    quiz_1_question_label.configure(text=quiz_1_temp["question"])
   
    choices = quiz_1_temp["choices"]
    for i in range(4):
        quiz_1_choice_buttons[i].configure(text=choices[i], state="normal")

    quiz_1_feedback_label.configure(text="")
    quiz_1_next_button.configure(state="disabled")

    text_to_speech_1.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_1_tts():
    engine = pyttsx3.init()
    quiz_1_tts_content = [quiz_1_temp["question"], quiz_1_temp["choices"]]
    for i in quiz_1_tts_content:
        engine.say(i)
        engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_1_check_answer(choice):
    quiz_1_temp = quiz_data_1[quiz_1_current_question]
    selected_choice = quiz_1_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == quiz_1_temp["answer"]:
        global quiz_1_score
        quiz_1_score += 1
        quiz_1_score_label.configure(text="Score: {}/{}".format(quiz_1_score, len(quiz_data_1)))
        quiz_1_feedback_label.configure(text="Correct!", fg_color = "Green")
    else:
        quiz_1_feedback_label.configure(text="Incorrect! "+ quiz_1_temp["answer"], fg_color = "Red")
   
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
                            "Congratulations! Final score: {}/{}".format(quiz_1_score, len(quiz_data_1)))

# Quiz 1 Widgets

# Create the question label
quiz_1_question_label = CTkLabel(quizpage_1, anchor="center", font=('arial bold', 18))
quiz_1_question_label.pack(pady=10)

# Create the choice buttons
quiz_1_choice_buttons = []
for i in range(4):
    button_1 = CTkButton(quizpage_1, height = 100, width = 200, command=lambda i=i: quiz_1_check_answer(i))
    button_1.pack(pady=5)
    quiz_1_choice_buttons.append(button_1)

# text to speech button for questions
text_to_speech_1 = CTkButton(quizpage_1, text="", image = image_tk_4, command = quiz_1_tts)
text_to_speech_1.pack()

# Create the feedback label, score label and next buttom
quiz_1_feedback_label = CTkLabel(quizpage_1,anchor="center")
quiz_1_feedback_label.pack(pady=10)

quiz_1_score_label = CTkLabel(quizpage_1, text="Score: 0/{}".format(len(quiz_data_1)),anchor="center")
quiz_1_score_label.pack(pady=10)

quiz_1_next_button = CTkButton(quizpage_1, text="Next", command=next_question_1, state="disabled")
quiz_1_next_button.pack(pady=10)

# quiz 1 back button
quiz_1_back_button = CTkButton(quizpage_1, text = "Back", command = quiz_1_to_quizpage)
quiz_1_back_button.place(x = 10, y = 600)

# Initialise score and current question
quiz_1_score = 0
quiz_1_current_question = 0

# Show First Question
quiz_1_show_question()

# Quiz 2 System (including marking)

# Function to display the current question and choices
def quiz_2_show_question():
    global quiz_2_temp
    quiz_2_temp = quiz_data_2[quiz_2_current_question]
    quiz_2_question_label.configure(text=quiz_2_temp["question"])
   
    choices = quiz_2_temp["choices"]
    for i in range(4):
        quiz_2_choice_buttons[i].configure(text=choices[i], state="normal")

    quiz_2_feedback_label.configure(text="")
    quiz_2_next_button.configure(state="disabled")

    text_to_speech_2.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_2_tts():
    engine = pyttsx3.init()
    quiz_2_tts_content = [quiz_2_temp["question"], quiz_2_temp["choices"]]
    for i in quiz_2_tts_content:
        engine.say(i)
        engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_2_check_answer(choice):
    quiz_2_temp = quiz_data_2[quiz_2_current_question]
    selected_choice = quiz_2_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == quiz_2_temp["answer"]:
        global quiz_2_score
        quiz_2_score += 1
        quiz_2_score_label.configure(text="Score: {}/{}".format(quiz_2_score, len(quiz_data_2)))
        quiz_2_feedback_label.configure(text="Correct!", fg_color = "Green")
    else:
        quiz_2_feedback_label.configure(text="Incorrect! "+ quiz_2_temp["answer"], fg_color = "Red")
   
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
                            "Congratulations! Final score: {}/{}".format(quiz_2_score, len(quiz_data_2)))

# Quiz 2 Widgets

# Create the question label
quiz_2_question_label = CTkLabel(quizpage_2, anchor="center", font=('arial bold', 18))
quiz_2_question_label.pack(pady=10)

# Create the choice buttons
quiz_2_choice_buttons = []
for i in range(4):
    button_2 = CTkButton(quizpage_2, height = 100, width = 200, command=lambda i=i: quiz_2_check_answer(i))
    button_2.pack(pady=5)
    quiz_2_choice_buttons.append(button_2)

# text to speech button for questions
text_to_speech_2 = CTkButton(quizpage_2, text="", image = image_tk_4, command = quiz_2_tts)
text_to_speech_2.pack()

# Create the feedback label, score label and next button
quiz_2_feedback_label = CTkLabel(quizpage_2,anchor="center")
quiz_2_feedback_label.pack(pady=10)

quiz_2_score_label = CTkLabel(quizpage_2, text="Score: 0/{}".format(len(quiz_data_2)),anchor="center")
quiz_2_score_label.pack(pady=10)

quiz_2_next_button = CTkButton(quizpage_2, text="Next", command=next_question_2, state="disabled")
quiz_2_next_button.pack(pady=10)

# quiz 2 back button 

quiz_2_back_button = CTkButton(quizpage_2, text = "Back", command = quiz_2_to_quizpage)
quiz_2_back_button.place(x = 10, y = 600)


# Initialise score and current question
quiz_2_score = 0
quiz_2_current_question = 0

# Show First Question
quiz_2_show_question()

# Quiz 3 System (including marking)

# Shows the current question and choice buttons
def quiz_3_show_question():
    global quiz_3_temp
    quiz_3_temp = quiz_data_3[quiz_3_current_question]
    quiz_3_question_label.configure(text=quiz_3_temp["question"])
   
    choices = quiz_3_temp["choices"]
    for i in range(4):
        quiz_3_choice_buttons[i].configure(text=choices[i], state="normal")

    quiz_3_feedback_label.configure(text="")
    quiz_3_next_button.configure(state="disabled")

    text_to_speech_3.place(x = 600, y = 100)

# Reads the Current Question and Choices
def quiz_3_tts():
    engine = pyttsx3.init()
    quiz_3_tts_content = [quiz_3_temp["question"], quiz_3_temp["choices"]]
    for i in quiz_3_tts_content:
        engine.say(i)
        engine.runAndWait()

# Function to check the selected answer and provide feedback
def quiz_3_check_answer(choice):
    quiz_3_temp = quiz_data_3[quiz_3_current_question]
    selected_choice = quiz_3_choice_buttons[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == quiz_3_temp["answer"]:
        global quiz_3_score
        quiz_3_score += 1
        quiz_3_score_label.configure(text="Score: {}/{}".format(quiz_3_score, len(quiz_data_3)))
        quiz_3_feedback_label.configure(text="Correct!", fg_color = "Green")
    else:
        quiz_3_feedback_label.configure(text="Incorrect! "+ quiz_3_temp["answer"], fg_color = "Red")
   
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
                            "Congratulations! Final score: {}/{}".format(quiz_3_score, len(quiz_data_3)))

# Quiz 3 Widgets

# Create the question label
quiz_3_question_label = CTkLabel(quizpage_3, anchor="center", font=('arial bold', 18))
quiz_3_question_label.pack(pady=10)

# Create the choice buttons
quiz_3_choice_buttons = []
for i in range(4):
    button_3 = CTkButton(quizpage_3, height = 100, width = 300, command=lambda i=i: quiz_3_check_answer(i))
    button_3.pack(pady=5)
    quiz_3_choice_buttons.append(button_3)

# text to speech button for questions
text_to_speech_3 = CTkButton(quizpage_3, text="", image = image_tk_4, command = quiz_3_tts)
text_to_speech_3.pack()

# Create the feedback label, score label and next button
quiz_3_feedback_label = CTkLabel(quizpage_3,anchor="center")
quiz_3_feedback_label.pack(pady=10)

quiz_3_score_label = CTkLabel(quizpage_3, text="Score: 0/{}".format(len(quiz_data_3)),anchor="center")
quiz_3_score_label.pack(pady=10)

quiz_3_next_button = CTkButton(quizpage_3, text="Next", command=next_question_3, state="disabled")
quiz_3_next_button.pack(pady=10)

# quiz 3 back button

quiz_3_back_button = CTkButton(quizpage_3, text = "Back", command = quiz_3_to_quizpage)
quiz_3_back_button.place(x = 10, y = 600)

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

scenario_1_description_button = CTkButton(scenariopage_1, text = "Scenario Description", image = image_tk_4, compound = LEFT, command = scenario_1_description_tts)
scenario_1_description_button.place(x = 550, y = 50 )

scenario_1_questions_tts_button = CTkButton(scenariopage_1, text = "Questions", image = image_tk_4, compound = LEFT, command = scenario_1_questions_tts)
scenario_1_questions_tts_button.place(x = 550, y = 100)

# scenario 1 question 1 widgets

scenario_1_question_1_title = CTkLabel(scenariopage_1, text = "1) What Primary Injury\n has Johhny Suffered?", font=("arial bold", 12))
scenario_1_question_1_title.place(x = 20, y = 125)

scenario_1_question_1_choices = CTkLabel(scenariopage_1, text = "a) Heart Attack\n b) Hyperthermia\n c) General Burns\n d) Shock ")
scenario_1_question_1_choices.place(x = 30, y = 170)
                                
scenario_1_question_1_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_1_entry.place(x = 30, y = 230 )

# scenario 1 question 2 widgets

scenario_1_question_2_title = CTkLabel(scenariopage_1, text = "2) How should the \nPrimary injury be treated?", font=("arial bold", 12))
scenario_1_question_2_title.place(x = 300, y = 125)

scenario_1_question_2_title = CTkLabel(scenariopage_1, text = "a) Epipen\n b) Running hands under Cool Water\n c) Immediate Bandaging\n d) Lotions and Oils" )
scenario_1_question_2_title.place(x = 260, y = 170)
                                
scenario_1_question_2_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_2_entry.place(x = 315, y = 230)

# scenario 1 question 3 widgets

scenario_1_question_3_title = CTkLabel(scenariopage_1, text = "3) As Johnny has passed out,\n what is the first priority?",font=("arial bold", 12))
scenario_1_question_3_title.place(x = 10, y = 295)

scenario_1_question_3_choices = CTkLabel(scenariopage_1, text = "a) Tend to Primary Injury\n b) Roll into Recovery Position\nc) Check for Breathing\n d) Turn off Stove")
scenario_1_question_3_choices.place(x = 10, y = 335)
                                
scenario_1_question_3_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_3_entry.place(x = 30, y = 405)

# scenario 1 question 4 widgets

scenario_1_question_4_title = CTkLabel(scenariopage_1, text = "4) Gas and smoke begin to fill the room,\nHow should Johnny be carried out?", font=("arial bold", 12))
scenario_1_question_4_title.place(x = 260, y = 300)

scenario_1_question_4_choices = CTkLabel(scenariopage_1, text = "a) Chair Lift Method\nb) Four-Handed Seat\nd) Any method is applicable\nd) Drag Method")
scenario_1_question_4_choices.place(x = 280, y = 335)
                                                            
scenario_1_question_4_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_4_entry.place(x = 305, y = 405)

# scenario 1 question 5 widgets

scenario_1_question_5_title = CTkLabel(scenariopage_1, text = "5) Is Medical Referal Necessary?", font=("arial bold", 12))
scenario_1_question_5_title.place(x = 10, y = 485)

scenario_1_question_5_choices = CTkLabel(scenariopage_1, text = "a) Yes, in all cases\nb) No, there is no reason to\nc) Decided by Patient\nd) Unsure")
scenario_1_question_5_choices.place(x = 10, y = 510)
                                
scenario_1_question_5_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_5_entry.place(x = 30, y = 580)


# scenario 1 question 6 widgets

scenario_1_question_6_title = CTkLabel(scenariopage_1, text = "6) You were the only person around when Johhny got\n injured, Are you legally obliged to assist?", font=("arial bold", 12))
scenario_1_question_6_title.place(x = 240, y = 475)

scenario_1_question_6_choices = CTkLabel(scenariopage_1, text = "a) Yes\nb) No\nc) If it were a situation of life or death\nd) Unsure")
scenario_1_question_6_choices.place(x = 250, y = 510)
                                
scenario_1_question_6_entry = CTkEntry(scenariopage_1, width = 100)
scenario_1_question_6_entry.place(x = 305, y = 580)

#scenario 1 image
Scenario_1_Image = Image.open("Scenario_1_Image.jpg").resize((300, 300))
image_tk_1 = ImageTk.PhotoImage(Scenario_1_Image)
image_label_1 = tk.Label(scenariopage_1, text="", image = image_tk_1)
image_label_1.image = image_tk_1
image_label_1.place(x=650, y=200)

# scenario 1 marking

def scenario_1_marking():
    global scenario_1_score
    global scenario_1_feedback_1
    global scenario_1_feedback_2
    global scenario_1_feedback_3
    global scenario_1_feedback_4
    global scenario_1_feedback_5
    global scenario_1_feedback_6
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
        scenario_1_feedback_1.place(x=60, y=260)
    else:
        scenario_1_feedback_1 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_1.place(x=15, y=260)

    if scenario_1_question_2_entry.get() == "b" :
        scenario_1_score += 1
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_2.place(x=350, y=260)
    else:
        scenario_1_feedback_2 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_1_feedback_2.place(x=300, y=260)

    if scenario_1_question_3_entry.get() == "c" :
        scenario_1_score += 1
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_3.place(x=60, y=440)
    else:
        scenario_1_feedback_3 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_1_feedback_3.place(x=15, y=440)

    if scenario_1_question_4_entry.get() == "d" :
        scenario_1_score += 1
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_4.place(x=350, y=440)
    else:
        scenario_1_feedback_4 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_1_feedback_4.place(x=305, y=440)

    if scenario_1_question_5_entry.get() == "a" :
        scenario_1_score += 1
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_5.place(x=60, y=620)
    else:
        scenario_1_feedback_5 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_1_feedback_5.place(x=15, y=620)

    if scenario_1_question_6_entry.get() == "b" :
        scenario_1_score += 1
        scenario_1_feedback_6 = CTkLabel(scenariopage_1, text="Correct", bg_color="green")
        scenario_1_feedback_6.place(x=350, y=620)
    else:
        scenario_1_feedback_6 = CTkLabel(scenariopage_1, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_1_feedback_6.place(x=305, y=620)
    
    global scenario_1_result_label
    scenario_1_result_label = CTkLabel(scenariopage_1, text=f"Your Score is : {scenario_1_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_1_result_label.place(x = 600, y = 550)
    
# scenario 1 submit button

scenario_1_submit = CTkButton(scenariopage_1, text = "Submit", command = scenario_1_marking)
scenario_1_submit.place(x = 600, y = 660)

# scenario 1 back button 

scenario_1_back_button = CTkButton(scenariopage_1, text = "Back", command = scenario_1_to_scenariopage)
scenario_1_back_button.place(x = 10, y = 660)

# widgets for scenario 2

scenario_2_description_title = CTkLabel(scenariopage_2, text = "Scenario 2 Description:", font = ("arial bold", 20))
scenario_2_description_title.place(x = 15, y = 10)

scenario_2_description = CTkLabel(scenariopage_2, text = "You are on a walking track at a park when you notice a young girl yelling for help.\nUpon inspection, you notice that she has two identical punctures next\n to eachother on her leg.The area surrounding it has gone red and puffy.\nShe says she cannot walk, and says the pain is immense.\n There are visible stingers protruding from the punctures." )
scenario_2_description.place( x = 10, y = 50)

# scenario 2 text to speech buttons

scenario_2_description_button = CTkButton(scenariopage_2, text = "Scenario Description", image = image_tk_4, compound = LEFT, command = scenario_2_description_tts)
scenario_2_description_button.place(x = 550, y = 50 )

scenario_2_questions_tts_button = CTkButton(scenariopage_2, text = "Questions", image = image_tk_4, compound = LEFT, command = scenario_2_questions_tts)
scenario_2_questions_tts_button.place(x = 550, y = 100)


# scenario 2 question 1 widgets

scenario_2_question_1_title = CTkLabel(scenariopage_2, text = "1) What is the girl's injury?", font = ("arial bold", 12))
scenario_2_question_1_title.place(x = 10, y = 135)

scenario_2_question_1_choices = CTkLabel(scenariopage_2, text = "a) Snake Bite\nb) Insect Sting\nc) Bleeding (stabbed) \nd) Leg Fracture")
scenario_2_question_1_choices.place(x = 10, y = 160)
                               
scenario_2_question_1_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_1_entry.place(x = 20, y = 230 )


# scenario 2 question 2 widgets

scenario_2_question_2_title = CTkLabel(scenariopage_2, text = "2) Due to the puffiness and rashes around the wound\n what else may have occured?", font = ("arial bold", 12))
scenario_2_question_2_title.place(x = 225, y = 135)
                               
scenario_2_question_2_choices = CTkLabel(scenariopage_2, text = "a) Anaphylactic Reaction\nb) Burns\nc) Bruising\nd) Nervous Response")
scenario_2_question_2_choices.place(x = 295, y = 170)

scenario_2_question_2_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_2_entry.place(x = 305, y = 230)


# scenario 2 question 3 widgets

scenario_2_question_3_title = CTkLabel(scenariopage_2, text = "3) How would you first\n treat the primary injury?", font=("arial bold", 12))
scenario_2_question_3_title.place(x = 10, y = 300)
                               
scenario_2_question_3_title = CTkLabel(scenariopage_2, text = "a) Wetten Wound\nb) Bandage Wound \nc) Remove the Stingers\nd) Apply Blister Cream")
scenario_2_question_3_title.place(x = 10, y = 335)

scenario_2_question_3_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_3_entry.place(x = 20, y = 405)


# scenario 2 question 4 widgets

scenario_2_question_4_title = CTkLabel(scenariopage_2, text = "4) What medical instrument may\n be used in this treatment?", font=("arial bold", 12))
scenario_2_question_4_title.place(x = 260, y = 300)

scenario_2_question_4_choices = CTkLabel(scenariopage_2, text = "a) Green Whistle\nb) Surgical Knife\nc) Medical Brush\nd) Epipen")
scenario_2_question_4_choices.place(x = 300, y = 335)
                               
scenario_2_question_4_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_4_entry.place(x = 305, y = 405)


# scenario 2 question 5 widgets

scenario_2_question_5_title = CTkLabel(scenariopage_2, text = "5) Assume the girl passes out,\n what should you do?", font=("arial bold", 12))
scenario_2_question_5_title.place(x = 10, y = 475)

scenario_2_question_5_choices = CTkLabel(scenariopage_2, text = "a) Check for Breathing\n b) Check Pulse\n c) Shake Girl Awake\n Call Out for Help")
scenario_2_question_5_choices.place(x = 10, y = 515)
                               
scenario_2_question_5_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_5_entry.place(x = 20, y = 580)

# scenario 2 question 6 widgets

scenario_2_question_6_title = CTkLabel(scenariopage_2, text = "6) She regains consciousness and you call\n 000 for help, what part of DRSABCD is this?", font=("arial bold", 12))
scenario_2_question_6_title.place(x = 260, y = 475)

scenario_2_question_6_title = CTkLabel(scenariopage_2, text = "a) Danger\nb) Response\nc) Send for Help\nd) Airways")
scenario_2_question_6_title.place(x = 300, y = 515)     

scenario_2_question_6_entry = CTkEntry(scenariopage_2, width = 100)
scenario_2_question_6_entry.place(x = 305, y = 580)

# scenario 2 image
Scenario_2_Image = Image.open("Scenario_2_Image.jpg").resize((300, 300))
image_tk_2 = ImageTk.PhotoImage(Scenario_2_Image)
image_label_2 = tk.Label(scenariopage_2, text="", image = image_tk_2)
image_label_2.image = image_tk_2
image_label_2.place(x=650, y=240)

# scenario 2 marking

def scenario_2_marking():
    global scenario_2_score
    global scenario_2_feedback_1
    global scenario_2_feedback_2
    global scenario_2_feedback_3
    global scenario_2_feedback_4
    global scenario_2_feedback_5
    global scenario_2_feedback_6
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
        scenario_2_feedback_1.place(x=60, y=260)
    else:
        scenario_2_feedback_1 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_2_feedback_1.place(x=15, y=260)
    if scenario_2_question_2_entry.get() == "a" :
        scenario_2_score += 1
        scenario_2_feedback_2 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_2.place(x=350, y=260)
    else:
        scenario_2_feedback_2 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_2_feedback_2.place(x=300, y=260)
    if scenario_2_question_3_entry.get() == "c" :
        scenario_2_score += 1
        scenario_2_feedback_3 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_3.place(x=60, y=440)
    else:
        scenario_2_feedback_3 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_2_feedback_3.place(x=15, y=440)
    if scenario_2_question_4_entry.get() == "d" :
        scenario_2_score += 1
        scenario_2_feedback_4 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_4.place(x=350, y=440)
    else:
        scenario_2_feedback_4 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_2_feedback_4.place(x=305, y=440)
    if scenario_2_question_5_entry.get() == "a" :
        scenario_2_score += 1
        scenario_2_feedback_5 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_5.place(x=60, y=620)
    else:
        scenario_2_feedback_5 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_2_feedback_5.place(x=15, y=620)
    if scenario_2_question_6_entry.get() == "c" :
        scenario_2_score += 1
        scenario_2_feedback_6 = CTkLabel(scenariopage_2, text="Correct", bg_color="green")
        scenario_2_feedback_6.place(x=350, y=620)
    else:
        scenario_2_feedback_6 = CTkLabel(scenariopage_2, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_2_feedback_6.place(x=305, y=620)
    global scenario_2_result_label
    scenario_2_result_label = CTkLabel(scenariopage_2, text=f"Your Score is : {scenario_2_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_2_result_label.place(x = 600, y = 550)


# scenario 2 submit button

scenario_2_submit = CTkButton(scenariopage_2, text = "Submit", command = scenario_2_marking)
scenario_2_submit.place(x = 600, y = 660)

scenario_2_back_button = CTkButton(scenariopage_2, text = "Back", command = scenario_2_to_scenariopage)
scenario_2_back_button.place(x = 10, y = 660)

# widgets for scenario 3

scenario_3_description_title = CTkLabel(scenariopage_3, text = "Scenario 3 Description:", font = ("arial bold", 20))
scenario_3_description_title.place(x = 15, y = 10)

scenario_3_description = CTkLabel(scenariopage_3, text = " You are out near a lake during winter, when you notice a man has fallen\nin. He manages to get out but is shivering and battling consciousness\n At this point in time it is also raining. You are the only person around at the time." )
scenario_3_description.place( x = 10, y = 50)

# scenario 1 text to speech buttons

scenario_3_description_button = CTkButton(scenariopage_3, text = "Scenario Description", image = image_tk_4, compound = LEFT, command = scenario_3_description_tts)
scenario_3_description_button.place(x = 550, y = 50 )

scenario_3_questions_tts_button = CTkButton(scenariopage_3, text = "Questions", image = image_tk_4, compound = LEFT, command = scenario_3_questions_tts)
scenario_3_questions_tts_button.place(x = 550, y = 100)

# scenario 3 question 1 widgets

scenario_3_question_1_title = CTkLabel(scenariopage_3, text = "1) What condition can be\n associated with this man?", font=("arial bold", 12))
scenario_3_question_1_title.place(x = 10, y = 125)

scenario_3_question_1_choices = CTkLabel(scenariopage_3, text = "a) Hyperthermia\nb) Hypothermia\nc) Coldstroke\nd) Shock")
scenario_3_question_1_choices.place(x = 30, y = 160)
                               
scenario_3_question_1_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_1_entry.place(x = 20, y = 230 )


# scenario 3 question 2 widgets

scenario_3_question_2_title = CTkLabel(scenariopage_3, text = "2) What is the First Step of Treatment?", font=("arial bold", 12))
scenario_3_question_2_title.place(x = 260, y = 135)

scenario_3_question_2_choices = CTkLabel(scenariopage_3, text = "a) Cover Man in Warm Garments\n b) Check his Breathing\n c) Seek Shelter from Rain\n d) Ask him How This Happened")
scenario_3_question_2_choices.place(x = 260, y = 160)

scenario_3_question_2_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_2_entry.place(x = 305, y = 230)


# scenario 3 question 3 widgets

scenario_3_question_3_title = CTkLabel(scenariopage_3, text = "3) From Question 2, What Part of\n DRSABCD is this?", font=("arial bold", 12))
scenario_3_question_3_title.place(x = 5 , y = 300)

scenario_3_question_3_choices = CTkLabel(scenariopage_3, text = "a) Danger\nb) Response\nc) Breathing\nd) CPR")
scenario_3_question_3_choices.place(x = 30, y = 335)
                                         
scenario_3_question_3_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_3_entry.place(x = 20, y = 405)


# scenario 3 question 4 widgets

scenario_3_question_4_title = CTkLabel(scenariopage_3, text = "4) What Treatment is Most Appropriate?", font=("arial bold", 12))
scenario_3_question_4_title.place(x = 260, y = 310)

scenario_3_question_4_choices = CTkLabel(scenariopage_3, text = "a) Provide Blankets and Garments\nb) Provide a Lighter \nc) Provide Cool Water\nd) Provide Electric Heating")
scenario_3_question_4_choices.place(x = 260, y = 335)

scenario_3_question_4_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_4_entry.place(x = 305, y = 405)

# scenario 3 question 5 widgets

scenario_3_question_5_title = CTkLabel(scenariopage_3, text = "5) The patient seems to still\n be struggling, but breathing is\n regular, is CPR necessary?",font=("arial bold", 12) )
scenario_3_question_5_title.place(x = 10, y = 465)

scenario_3_question_5_choices = CTkLabel(scenariopage_3, text = "a) Yes\nb) No\nc) Ask the Patient\nd) Unsure")
scenario_3_question_5_choices.place(x = 10, y = 510)                
                               
scenario_3_question_5_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_5_entry.place(x = 20, y = 580)


# scenario 3 question 6 widgets

scenario_3_question_6_title = CTkLabel(scenariopage_3, text = "6) What else can be done for the patient?", font=("arial bold", 12) )
scenario_3_question_6_title.place(x = 260, y = 485)

scenario_3_question_6_choices = CTkLabel(scenariopage_3, text = "a) Encourage Passive Movement\nb) Directly Applying Heat\nc) Remove Wet Clothing\nd) Wrap Yourself Around Patient")
scenario_3_question_6_choices.place(x = 260, y = 510)
                               
scenario_3_question_6_entry = CTkEntry(scenariopage_3, width = 100)
scenario_3_question_6_entry.place(x = 305, y = 580)

# scenario 3 image
Scenario_3_Image = Image.open("Scenario_3_Image.jpg").resize((300, 300))
image_tk_3 = ImageTk.PhotoImage(Scenario_3_Image)
image_label_3 = tk.Label(scenariopage_3, text="", image = image_tk_3)
image_label_3.image = image_tk_3
image_label_3.place(x=650, y=240)

# scenario 3 marking

def scenario_3_marking():
    global scenario_3_score
    global scenario_3_feedback_1
    global scenario_3_feedback_2
    global scenario_3_feedback_3
    global scenario_3_feedback_4
    global scenario_3_feedback_5
    global scenario_3_feedback_6
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
        scenario_3_feedback_1.place(x=60, y=260)
    else:
        scenario_3_feedback_1 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_3_feedback_1.place(x=15, y=260)
    if scenario_3_question_2_entry.get() == "c" :
        scenario_3_score += 1
        scenario_3_feedback_2 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_2.place(x=350, y=260)
    else:
        scenario_3_feedback_2 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_3_feedback_2.place(x=300, y=260)
    if scenario_3_question_3_entry.get() == "d" :
        scenario_3_score += 1
        scenario_3_feedback_3 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_3.place(x=60, y=435)
    else:
        scenario_3_feedback_3 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is D", bg_color="red")
        scenario_3_feedback_3.place(x=15, y=435)
    if scenario_3_question_4_entry.get() == "a" :
        scenario_3_score += 1
        scenario_3_feedback_4 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_4.place(x=350, y=450)
    else:
        scenario_3_feedback_4 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is A", bg_color="red")
        scenario_3_feedback_4.place(x=305, y=450)
    if scenario_3_question_5_entry.get() == "b" :
        scenario_3_score += 1
        scenario_3_feedback_5 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_5.place(x=60, y=620)
    else:
        scenario_3_feedback_5 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is B", bg_color="red")
        scenario_3_feedback_5.place(x=15, y=620)
    if scenario_3_question_6_entry.get() == "c" :
        scenario_3_score += 1
        scenario_3_feedback_6 = CTkLabel(scenariopage_3, text="Correct", bg_color="green")
        scenario_3_feedback_6.place(x=350, y=620)
    else:
        scenario_3_feedback_6 = CTkLabel(scenariopage_3, text="Incorrect, Correct Answer is C", bg_color="red")
        scenario_3_feedback_6.place(x=305, y=620)
    
    global scenario_3_result_label
    scenario_3_result_label = CTkLabel(scenariopage_3, text=f"Your Score is : {scenario_3_score}/7", font=("arial bold", 15), bg_color="blue")
    scenario_3_result_label.place(x = 600, y = 550)


# scenario 3 submit button

scenario_3_submit = CTkButton(scenariopage_3, text = "Submit", command = scenario_3_marking)
scenario_3_submit.place(x = 600, y = 660)

scenario_3_back_button = CTkButton(scenariopage_3, text = "Back", command = scenario_3_to_scenariopage)
scenario_3_back_button.place(x = 10, y = 660)

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

menutheme.add_command(label = "Dark", command= dark_theme)
menutheme.add_command(label = "Light", command= light_theme)

root.resizable(height=False, width=False)
    
root.mainloop()

