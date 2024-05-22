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

Commit 4:

The default window size was increased as upon trying to enter questions and answers onto quiz pages, most did not fit. This in turn led to adjusting widgets to account for the change in default window size as well as adjusting the size functions. The buttons that take the user to lessons were also renamed to inquiry questions 1-3 rather than placeholder labels.
