"# Educational-Program---PDHPE-Revision-System" 

Documentation of Changes between Commits

Commit 1:

Built the initial layout for the GUI (homepage). This included a lesson button, quiz button and scenario button, to access the different revision types. Home page also included a menubar with customisable features for inclusivity. This included sizing (small, medium, large), theme (dark, light) and translate (not ready yet). Tkinter Frames were used to represent different pages, this allowed for seamless transitions from home page to the different revision types. A lesson page was built, displaying three lessons (represented as buttons) which are yet to be filled with information. A home function was also installed into the menubar which would return the user to the home page upon clicking. Custom Tkinter was used for the GUI as it provided functions that would reduce the amount of lines of code.

Test:

A test commit to see whether or not the GitHub repository would record new changes. For this test, a test button was placed onto the homepage. 

Commit 2: 

Quiz page was built (for choice of quiz), with accompanying functions to enter and return from the page. Three quizzes were displayed on this page (represented as buttons). An initial layout of questions and marking system was built onto quiz 1 on the quiz page. Entry Boxes will be used for user answers to questions, while labels will be used to display questions and answer choices (multiple choice). Placeholder questions and answers were used to test if the marking system functioned correctly. The window size for the "large" size option was also increased to allow all widgets to be seen on the quiz page. The test button from the prior "test commit" was also removed.

Commit 3:

Question layout for quizzes was finalised, with a submit button implemented in the bottom corner. Upon pressing the submit button, a label will appear displaying the user score. This label's background was changed to green for users to easily notice that it had appeared. Buttons and titles on the homepage were also altered so that their text will be in "bold" and "italic", allows the user to read some of its text more easily. Note: at this point, all questions and answers were identical and placeholders to test if the whole program would run as intended. Quiz pages for quiz 2 and quiz 3 were also built, layout for both were identical to quiz 1.

Commit 4:

Scenario part of revision system was completed, with placeholder questions, answers, and descriptions. Includes the creation of functions to switch between scenario pages, functions to mark scenario questions and functions to output result. The scenarios segment of the system only has 7 questions per scenario, to improve the layout of the page, and allow for description and instruction labels. A gap has also been left on each scenario page for the future implementation of images to supplement scenarios. Also edited the code so that results would appear on different page and not on the pages with questions. Also added "/total amount of questions" on result outputs.

Commit 5:

The default window size was increased as upon trying to enter questions and answers onto quiz pages, most did not fit. This in turn led to adjusting widgets to account for the change in default window size as well as adjusting the size functions. The buttons that take the user to lessons were also renamed to inquiry questions 1-3 rather than placeholder labels.

Commit 6:

Replaced placeholder questions in quizzes 1-3 with real questions relating to first aid (PDHPE senior syllabus). Included splitting the question label and the choices (a-d) labels so that moving them around to fit in the page would be easier. Also allowed for question labels to be in bold, so that the user is able to differentiate the question from the choices. Also edited marking system to account for these changes as prior to the change, the answers to all questions was "a" (placeholder).

Commit 7:

Changed quiz format so that each question would have the entire page to itself. Upon pressing a button the current question would configure into next. This allowed for real-time feedback (correct/incorrect after every answer). This was done using external python files full of quiz data and importing them into the main program. First images were also added to the program (for scenario revision option) (note: image title Frog.PNG was a test image, will be deleted in next commit). Scenario question pages were kept the same as before, except now when submit is pressed, there is no new page that appears, rather labels are added underneath the questions saying if they were answered correctly or incorrectly. The final score was also added onto this page. The Translate feature will now be replaced by text-to-speech as the final inclusive feature as configuring google-translate proved too difficult. Preliminary applications of text-to-speech are in the code (including for quizzes) although the text-to-speech reads out not only the question and its choices but also the answer.

Commit 8:

Lessons (1-3) were built and completed. As all information would not fit on one page, scrollbars were implemented on each lesson page. Scenarios were completed, with each having their own image and a function that gives an error message when an invalid answer is given. Scenario marking was fixed, before the score wasn't getting incremented properly as += operator was written as =+. Some variable names in the quiz marking systems were changed so that they were more meaningful (intrinsic documentation). Quiz data files were also fixed (some questions were faulty as answers in database were misspelled). Large size function was altered so that the page would fit onto window and widgets would not overlap. The test image (Frog.PNG) was also removed.

Commit 9:

Code was changed so that every page had a button that would read the entirety of the page. As the speech function in python can only read 2-3 arguments, longer texts were put into arrays and the speak function was looped. The lesson titles on the lesson list were also edited so that each one displayed what inquiry question it was providing information for. General cleanup for code, including adding more comments to make future edits and maintenance easier.

Commit 10:

Errors were found in the scenario section of code, where when different sizes were applied the images did not change size and overlapped with text, this was fixed using a function that would be called when activating each size function. The reworking of lesson pages had also begun, giving each piece of information in each lesson its own page so that it was easier to read and looked more aesthetically pleasing. Back buttons were also added to each page. Before this the user would have to use the home function which would send them to the homepage, whereas the back button only sent the user to the previous page, increasing user accessibility. Also edited the appearance of lesson, quiz, scenario lists to match the home page (achieved through changing button sizes), to improve consistency of the GUI. Also began to change text to speech buttons to buttons with the microphone icon, for user accessibility and aesthetics.

Commit 11:

Edited code so that dark and light themes would also switch between dark and light wallpapers that were images. For these backgrounds, potential images were chosen but nothing is confirmed as of yet as the current options do not go well with the buttons. Functions were also created that would be called when changing sizes that altered the position and size of the scenario images as before they would overlap with text. Code was also edited so that when the user would exit or finish a quiz, when they reentered the same quiz, the score and questions would be reset, this will also have to be done for scenario pages. Lesson pages were also finalised using a similar format to the quiz pages, using an external file that contained lesson that would be imported in the mainprogram and be looped across one page.

Commit 12: 

Finalised background images, dark and light gridlines that mimic a notebook. Makes the code more aesthetic and ergonomic to the user. These backgrounds were now applied to all pages, not just main pages. Removed uneccessary result pages as they were no longer part of the code. Edited code so that after the user finishes and exits a scenario, after they re enter the same scenario, the feedback is reset. Renamed some function names for lessson pages, made more meaningful. Edited code so that when lesson content is read, the \n operator isn't read aloud as well. Made question labels bold, to improve aesthetics and readability.
