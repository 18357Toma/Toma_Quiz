#Imports.
from tkinter import * #Importing tkinter so I can use the widgets.
import random
from tkinter import messagebox
from PIL import ImageTk, Image


#Defining Variables.
background_color = "mint cream"
background_color2 = "black"
username_list = []
asked = []



question_answer = {
  1: ["It doesn’t matter how much sleep you get, you can always function your best.", "True", "False. 8 - 10 hours is recommended.", "It depends on the day.", "Any amount of sleep is okay as long as you have naps in the day.", "Varied age groups have different times recommended but from 13 - 18 years old, 8 - 10 hours sleep is suggested." , 2],

  2: [" What is the difference between mental health and mental illness?" , "There isn’t a difference." , "Mental illnesses are untreatable whereas mental health can be cared for." , "Illness is branched from mental health  and can affect a person’s performance, mental health is the state of your emotional well being." , "Mental health is physical wellbeing whereas mental illnesses affect the brain’s ability to function." , "Mental health is like a tree and mental illness branches off of it." , 3],

  3: ["What type of people are affected by mental health issues?" , "Usually teenagers." , "People who get bullied at school." , "Depressed kids." , "All of the above.", "Everyone endures life challenges and therefore anybody can be affected by issues of mental health." , 4],

  4: ["How should you approach someone that looks upset?" , "Be sincere and ask if there’s anything you can do for them, show your sympathy and let them have space." , "Punch them, pull their hair and push them to the ground saying “Stop being a cry baby!”." , "Insist on helping them with anything you think you can, even if they say no." , "Avoid approaching them, give them their space and let them deal with it on their own.", "Along with respecting boundaries, we should reach out to the person." , 1],

  5: ["How many people have been affected by mental health in New Zealand?" , "10." , "50%" , "1 in 4 people" , "Everyone" , "Everyone has had a point in time where they were very low or very happy." , 4],

  6: ["What is a good way to cope with poor mental health?" , "Eat, eat, eat and eat the feelings away." , "Take time to enjoy things such as hobbies, things you are good at and talk to someone if you feel it would help release the stress." , "Try to stay occupied by school work and join lots of social clubs." , "Involve yourself more in class or sports and push yourself to the limits to distract you from the problem." , "Take a break from everything, even with a friend by your side." , 2],

  7: ["Which Mental health issue affects people the most?" , "Paranoia (distrust of others or feeling like someone is after you)." , "Depression (persistent upset emotions or lack of interest in things, significantly affecting life activities)." , "Eating disorder (abnormal/unusual and unhealthy eating habits)." , "OCD (Obsessive compulsive disorder, repeating behavioural habits due to immoderate thoughts)." , "Depression is the most common issue which is suffered by people, majority being teenagers." , 2],

  8: ["What is the best thing to do when you see someone enjoying their day?" , "Nothing, or vibe with them." , "Ruin their day." , "Punch them." , "Make jokes and laugh at them with friends.", "You don't necessarily have to do anything, just let them be happy or join in!." , 1],

  9: ["Do people who suffer from serious mental issues deserve special treatment?" , "No, I think we should punch them.", "Yes, it’s nearly impossible to live through life with such difficult problems." , "Acknowledge that they have struggles and don’t persist in bringing them up. Sometimes it’s best to treat them like you should treat anyone, with respect and not like a child.", "Treat them with anything you can such as helping them grab their food at lunch or helping out with school work. Never let them be on their own to do things because they need help." , "It’s good to be nice, but not controlling over peoples’ lives." , 3],

  10: ["What shouldn’t you do to someone who is having a rough time with their mental wellbeing?" , "Give them coffee." , "Suggest different ways of distractions such as  colouring a book." , "Offer them to go out into a better space or even go for a run with them." , "Punch them." , "Just don’t punch them." , 4],
}

#Functions.
#Randomiser function.
def shuffle():
  global qnum 
  qnum = random.randint (1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    shuffle()



#Classes.

class MenuPage:
  def __init__(self, parent):
    #Set up frame for window.
    self.menu_frame = Frame(parent)
    self.menu_frame.grid() #Grid/table structure window.
    base.geometry("980x600")

    self.bg_image = Image.open("lightbackground.png") 
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
    base.configure(bg = background_color) 
    self.image_label= Label(self.menu_frame, image=self.bg_image)
    self.image_label.place(x=0, y=0) # make label fit the parent window always


    self.title_image = Image.open("quiztitle.png")
    #need to use Image if need to resize
    self.title_image = self.title_image.resize((500, 100), Image.ANTIALIAS)
    self.title_image = ImageTk.PhotoImage(self.title_image)
    #Label widget for heading.
    self.heading_label = Label(self.menu_frame, image=self.title_image, borderwidth = 0) #The label is text.
    self.heading_label.grid(row = 1, column = 1, padx = 10)

    #Subtitle text.
    self.user_label = Label(self.menu_frame, text="Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), bg = background_color)
    self.user_label.grid(row = 2, column = 1, padx = 20, pady = 20)

    #Enter name box.
    self.entry_box = Entry(self.menu_frame)
    self.entry_box.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 80, ipady = 10)


    #Dark theme button.
    self.theme1_button = Button(self.menu_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'black', activebackground = 'light gray', padx=10, pady=10, relief = RAISED, command = self.dark_theme)
    self.theme1_button.grid(row = 0, column = 0, pady = 20, padx = 20)

    #Light theme button.
    self.theme2_button = Button(self.menu_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'black',  activebackground = 'light gray', padx=10, pady=10, relief = RAISED)
    self.theme2_button.grid(row = 0, column = 2, pady = 20, padx = 20)

    #Start button.
    self.start_button = Button(self.menu_frame, text = "START", font = ("Helvetica", "18", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.name_collection)
    self.start_button.grid(row = 4, column = 1, padx = 20, pady = 40, ipadx = 30, ipady = 10)
  

  def dark_theme(self):
      self.menu_frame.destroy()
      DarkMenuPage(base)

  #Name Colection.
  def name_collection(self):
      name=self.entry_box.get()
      if str.isalpha(name) == True and len(name) >0 and len(name) <=10:
        username_list.append(name)
        self.menu_frame.destroy() #destroy the starter
        QuizPage(base)
      elif str.isalpha(name) == False and len(name) >0:
        messagebox.showerror("Name error:", "Please check that you are only using letters and no other characters or numerals.")
      elif len(name) <1:
        messagebox.showerror("Name error:", "Please check that you have entered a name.")
      elif len(name) >10:
        messagebox.showerror("Name error:", "Please check that you have entered a name up to 10 characters.")


class DarkMenuPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.menu_frame = Frame(parent)
      self.menu_frame.grid() #Grid/table structure window.
      base.geometry("980x600") #Geometry used to create a fixed window size/window dimensions.

      self.bg_image = Image.open("darkbackground.png")
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      base.configure(bg = background_color2)
      self.image_label= Label(self.menu_frame, image = self.bg_image)
      self.image_label.place(x=0, y=0) # make label l to fit the parent window always

      #Label widget for heading.
      self.title_image = Image.open("darkquiztitle.png") #need to use Image if need to resize
      self.title_image = self.title_image.resize((500, 100), Image.ANTIALIAS)
      self.title_image = ImageTk.PhotoImage(self.title_image)
      #Label widget for heading.
      self.heading_label = Label(self.menu_frame, image=self.title_image, borderwidth = 0) #The label is text.
      self.heading_label.grid(row = 1, column = 1, padx = 10)

      #Subtitle text.
      self.user_label = Label(self.menu_frame, text = "Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), foreground = 'white', bg = background_color2)
      self.user_label.grid(row = 2, column = 1, padx = 20, pady = 20)

      #Enter name box.
      self.entry_box = Entry(self.menu_frame)
      self.entry_box.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 80, ipady = 10)
      self.value = IntVar() #Holds the value of radio buttons.

      #Dark theme button.
      self.theme1_button = Button(self.menu_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'white', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'white', activebackground = 'light gray',  padx=10, pady=10, relief = RAISED)
      self.theme1_button.grid(row = 0, column = 0, pady = 20, padx = 20)

      #Light theme button.
      self.theme2_button = Button(self.menu_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'white',  activebackground = 'light gray',  padx=10, pady=10, relief = RAISED, command = self.light_theme)
      self.theme2_button.grid(row = 0, column = 2, pady = 20, padx = 20)
    
      #Start button.
      self.start_button = Button(self.menu_frame, text = "START", font = ("Helvetica", "16", 'bold'), foreground = 'white', bg = '#775144', highlightthickness = 2, highlightbackground = 'white',  activebackground = '#60100B', activeforeground = 'white', relief = RAISED, command = self.name_collection)
      self.start_button.grid(row = 4, column = 1, padx = 20, pady = 40, ipadx = 30, ipady = 10)


  def light_theme(self):
      self.menu_frame.destroy()
      MenuPage(base)

  #Name Colection.
  def name_collection(self):
      name = self.entry_box.get()
      if str.isalpha(name) == True and len(name) >0 and len(name) <=10:
        username_list.append(name)
        self.menu_frame.destroy() #destroy the starter
        DarkQuizPage(base)
      elif str.isalpha(name) == False and len(name) >0:
        messagebox.showerror("Name error:", "Please check that you are only using letters and no other characters or numerals.")
      elif len(name) <1:
        messagebox.showerror("Name error:", "Please check that you have entered a name.")
      elif len(name) >10 and str.isalpha(name) == True:
        messagebox.showerror("Name error:", "Please check that you have entered a name up to 10 characters.")


class QuizPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.
      self.quiz_frame.pack(fill="both", expand=True)

      shuffle()

      self.value=IntVar() #Holds the value of radio buttons.


      self.bg_image = Image.open("lightbackground.png") 
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      base.configure(bg = background_color) 
      self.bg_label= Label(self.quiz_frame, image=self.bg_image)
      self.bg_label.place(x=0, y=0) # make label fit the parent window always


      #Label widget for title logo.
      self.logo_image = Image.open("titlelogo.png") #need to use Image if need to resize
      self.logo_image = self.logo_image.resize((140, 120), Image.ANTIALIAS)
      self.logo_image = ImageTk.PhotoImage(self.logo_image)
      self.logo_label= Label(self.quiz_frame, image=self.logo_image, borderwidth = 0)
      self.logo_label.place(x = 20, y = 40)

      #question
      self.question_label = Label(self.quiz_frame, text = "Q: " + question_answer[qnum][0], font =("Helvitica","16", "bold"), foreground = 'black', bg = '#d8e9da', highlightbackground = 'black', pady = 5, width = 52, highlightthickness = 2, wraplength = 700)
      self.question_label.place(x = 200, y = 40)

      #radio button 1.
      self.option1= Radiobutton(self.quiz_frame, text=question_answer[qnum][1], font=("Helvetica","12"), foreground = 'black', value=1, padx=5, pady=5, variable = self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option1.place(x = 200, y = 160)

      #radio button 2
      self.option2 = Radiobutton(self.quiz_frame, text=question_answer[qnum][2], font=("Helvetica","12"), foreground = 'black', value=2, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da',  highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option2.place(x = 600, y = 160)

      #radio button 3
      self.option3=Radiobutton(self.quiz_frame, text=question_answer[qnum][3], font=("Helvetica","12"), foreground = 'black', value=3, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option3.place(x = 200, y = 340)

      #radio button 4
      self.option4=Radiobutton(self.quiz_frame, text=question_answer[qnum][4], font=("Helvetica","12"), foreground = 'black', value=4, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#d8e9da', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option4.place(x = 600, y = 340)

      #Question counter label.
      self.questioncounter_label=Label(self.quiz_frame, text="Q Num: ", font=("Helvetica", "14", "bold"), bg = background_color, highlightbackground = 'black', highlightthickness = 2, pady = 5, padx=5)
      self.questioncounter_label.place(x = 20, y = 180)

      #QNumber calculated label.
      self.qnumber_label=Label(self.quiz_frame, text=1, font=("Helvetica", "14", "bold"), bg = background_color, highlightbackground = 'black', highlightthickness = 2, pady = 5, padx=5)
      self.qnumber_label.place(x = 120, y = 180)

      #Score label.
      self.score_label=Label(self.quiz_frame, text="TOTAL SCORE", font=("Helvetica", "14", "bold"), bg = background_color, pady = 5)
      self.score_label.place(x = 20, y = 280)

      #Calculated Score label.
      self.numberscore_label=Label(self.quiz_frame, text=0, font=("Helvetica", "16", "bold"), bg = background_color, pady = 5)
      self.numberscore_label.place(x = 85, y = 310)

      #Answertext label
      self.answertext_label=Label(self.quiz_frame, text="....", font=("Helvetica", "14", "bold"), bg = background_color, foreground = background_color, pady = 5, justify='center', wraplength = 480)
      self.answertext_label.place(x = 360, y = 480)

      #Exit to menu button.
      self.exit_button = Button(self.quiz_frame, text = "EXIT TO MENU", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#F07470', pady=10, width = 15, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit)
      self.exit_button.place(x = 20, y = 530)


      #Next button.
      self.next_button = Button(self.quiz_frame, text = "NEXT", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#D9EAD3', pady= 10, width = 10, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.score_calculations)
      self.next_button.place(x = 870, y = 530)

      self.score = 0
      self.question_number = 1


  def exit(self):
    self.score = 0
    self.question_number = 0
    self.quiz_frame.destroy()
    MenuPage(base)

  #Question setup.
  def question_change(self):
    shuffle()
    self.value.set(0)
    self.question_label.config(text= "Q: " + question_answer[qnum][0])
    self.option1.config(text = question_answer[qnum][1])
    self.option2.config(text = question_answer[qnum][2])
    self.option3.config(text = question_answer[qnum][3])
    self.option4.config(text = question_answer[qnum][4])

  #Score calculations.
  def score_calculations(self):
    total_score = self.numberscore_label
    option_choice = self.value.get()
    answer_text = self.answertext_label
    question_counter = self.qnumber_label
    if len(asked)>9:
      if option_choice == question_answer[qnum][6]: #If last question is right answer.
        self.score +=1
        self.question_number +=1
        total_score.configure(text= self.score)
        question_counter.configure(text= self.question_number, foreground = 'black')
        answer_text.configure(text="Correct!", foreground = 'green')
        self.endResults()
      else: #If last question was wrong answer.
        self.score +=0
        self.question_number +=1
        total_score.configure(text= self.score)
        question_counter.configure(text= self.question_number, foreground = 'black')
        answer_text.configure(text= "Incorrect: \n" + question_answer[qnum][5], foreground = 'red')
        self.endResults()
    else:
      if option_choice == 0: #Check if user made a choice.
        answer_text.config(text="Sorry you didn't select anything, please retry", foreground = 'red')
      else: #If they made choice that isn't last question.
        if option_choice == question_answer[qnum][6]: #If user is right.
          self.score+=1
          self.question_number +=1
          total_score.configure(text = self.score)
          question_counter.configure(text= self.question_number, foreground = 'black')
          answer_text.configure(text="Correct!", foreground = 'green')
          self.question_change() #Run method for next question to come up.
        else: #If the user chooses wrong answer.
          self.score +=0
          self.question_number +=1
          total_score.configure(text= self.score)
          question_counter.configure(text= self.question_number, foreground = 'black')
          answer_text.configure(text="Incorrect: \n" + question_answer[qnum][5], foreground = 'red')
          self.question_change()

  #Results function.
  def endResults(self):
    self.quiz_frame.destroy()
    name = username_list[0]
    file = open("scoreBoard.txt", "a") #Opens the file that has high scores from appending.
    if name == "reset": #Clear the file list of scores when the name 'reset' is entered.
        file=open("scoreBoard.txt","w")
    else:
        file.write(str(self.score)) #The score intergers are turned into string.
        file.write("    ----    ") #Text is shown in file.
        file.write(name+"\n") #Displays name in the file and adds a line.
        file.close() #Close file.

    inputFile = open("scoreBoard.txt", "r") #Opens the score file which we can read.
    lineList = inputFile.readlines() #Line list is equal to  each line of the list.
    lineList.sort() #Lines are sorted in alphabetical order.
    top = [] #Top scores are displayed.
    top5 = (lineList[-5:]) #For top 10 these are the last 10 figures.
    for line in top5: #For each of the lines.
      point = line.split("    ----    ")
      top.append((int(point[0]), point[1]))
    file.close() #Close file.
    top.sort()
    top.reverse()
    return_string = ""
    for i in range(len(top)):
      return_string +="{}    ----    {}\n".format(top[i][0], top[i][1])
    print(return_string) #Tests are shown on the console.
    results_page = ResultsPage(base) #object
    results_page.scoreboard_label.config(text = return_string) #Configures scoreboard label to display top 5 names in results class.



class DarkQuizPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      self.quiz_frame.pack(fill="both", expand=True)
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      shuffle()

      self.value=IntVar() #Holds the value of radio buttons.

      self.bg_image = Image.open("darkbackground.png") 
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      base.configure(bg = background_color2) 
      self.bg_label= Label(self.quiz_frame, image=self.bg_image)
      self.bg_label.place(x=0, y=0) # make label fit the parent window always

      #Label widget for title logo.
      self.logo_image = Image.open("darktitlelogo.png")
      self.logo_image = ImageTk.PhotoImage(self.logo_image)
      self.logo_label= Label(self.quiz_frame, image=self.logo_image, borderwidth = 0)
      self.logo_label.place(x = 20, y = 40)

      self.question_label = Label(self.quiz_frame, text = "Q: " + question_answer[qnum][0], font =("Helvitica","16", "bold"), foreground = 'white', bg = '#c09891', highlightbackground = 'white', pady=5, width = 52, highlightthickness = 2, wraplength = 700)
      self.question_label.place(x = 200, y = 40)

      #radio button 1.
      self.option1= Radiobutton(self.quiz_frame, text=question_answer[qnum][1], font=("Helvetica","12"), foreground = 'black', value=1, padx=5, pady=5, variable = self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#c09891', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option1.place(x = 200, y = 160)

      #radio button 2
      self.option2 = Radiobutton(self.quiz_frame, text=question_answer[qnum][2], font=("Helvetica","12"), foreground = 'black', value=2, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#c09891',  highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option2.place(x = 600, y = 160)

      #radio button 3
      self.option3=Radiobutton(self.quiz_frame, text=question_answer[qnum][3], font=("Helvetica","12"), foreground = 'black', value=3, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#c09891', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option3.place(x = 200, y = 340)

      #radio button 4
      self.option4=Radiobutton(self.quiz_frame, text=question_answer[qnum][4], font=("Helvetica","12"), foreground = 'black', value=4, padx=5, pady=5, variable=self.value, background = "white", activebackground='light gray',  indicatoron = 0, selectcolor = 'light gray', highlightbackground = '#c09891', highlightthickness = 2, relief = RAISED, justify="left", width = 35, height = 6, wraplength = 300)
      self.option4.place(x = 600, y = 340)
  
      #Question counter label.
      self.questioncounter_label=Label(self.quiz_frame, text="Q Num: ", font=("Helvetica", "14", "bold"), foreground = 'white', bg = background_color2, highlightbackground = 'white', highlightthickness = 2, pady = 5)
      self.questioncounter_label.place(x = 20, y = 180)

      #QNumber calculated label.
      self.qnumber_label=Label(self.quiz_frame, text=1, font=("Helvetica", "14", "bold"), bg = background_color2, foreground = 'white', highlightbackground = 'white', highlightthickness = 2, pady = 5)
      self.qnumber_label.place(x = 120, y = 180)

      #Score label.
      self.score_label=Label(self.quiz_frame, text="TOTAL SCORE", font=("Helvetica", "14", "bold"), bg = background_color2, pady = 5, foreground = 'white')
      self.score_label.place(x = 20, y = 280)

      #Calculated Score label.
      self.numberscore_label=Label(self.quiz_frame, text=0, font=("Helvetica", "16", "bold"), bg = background_color2, pady = 5, foreground = 'white')
      self.numberscore_label.place(x = 85, y = 310)

      #Answertext label
      self.answertext_label=Label(self.quiz_frame, text="....", font=("Helvetica", "14", "bold"), bg = background_color2, pady = 5, justify='center', wraplength = 480)
      self.answertext_label.place(x = 360, y = 480)
  

      #Exit to menu button.
      self.exit_button = Button(self.quiz_frame, text = "EXIT TO MENU", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#F07470', pady=10, width = 15, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit)
      self.exit_button.place(x = 20, y = 530)


      #Next button.
      self.next_button = Button(self.quiz_frame, text = "NEXT", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#D9EAD3', pady= 10, width = 10, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.score_calculations)
      self.next_button.place(x = 870, y = 530)
      
      self.score=0
      self.question_number=0
    
    
  def exit(self):
    self.score=0
    self.question_number=0
    self.quiz_frame.destroy()
    DarkMenuPage(base)


#Question setup.
  def question_change(self):
    shuffle()
    self.value.set(0)
    self.question_label.config(text= "Q: " + question_answer[qnum][0])
    self.option1.config(text = question_answer[qnum][1])
    self.option2.config(text = question_answer[qnum][2])
    self.option3.config(text = question_answer[qnum][3])
    self.option4.config(text = question_answer[qnum][4])

  #Score calculations.
  def score_calculations(self):
    total_score = self.numberscore_label
    option_choice = self.value.get()
    answer_text = self.answertext_label
    question_counter = self.qnumber_label
    if len(asked)>9:
      if option_choice == question_answer[qnum][6]: #If last question is right answer.
        self.score +=1
        self.question_number +=1
        total_score.configure(text= self.score)
        question_counter.configure(text= self.question_number, foreground = 'white')
        answer_text.configure(text="Correct!", foreground = 'green')
        self.darkEndResults()
      else: #If last question was wrong answer.
        self.score +=0
        self.question_number +=1
        total_score.configure(text= self.score)
        question_counter.configure(text= self.question_number, foreground = 'white')
        answer_text.configure(text= "Incorrect: \n" + question_answer[qnum][5], foreground = 'red')
        self.darkEndResults()
    else:
      if option_choice == 0: #Check if user made a choice.
        answer_text.config(text="Sorry you didn't select anything, please retry", foreground = 'red')
      else: #If they made choice that isn't last question.
        if option_choice == question_answer[qnum][6]: #If user is right.
          self.score+=1
          self.question_number +=1
          total_score.configure(text = self.score)
          question_counter.configure(text= self.question_number, foreground = 'white')
          answer_text.configure(text="Correct!", foreground = 'green')
          self.question_change() #Run method for next question to come up.
        else: #If the user chooses wrong answer.
          self.question_number +=1
          total_score.configure(text= self.score)
          question_counter.configure(text= self.question_number, foreground = 'white')
          answer_text.configure(text="Incorrect: \n" + question_answer[qnum][5], foreground = 'red')
          self.question_change()

  def darkEndResults(self):
    self.quiz_frame.destroy()
    name = username_list[0]
    file = open("scoreBoard.txt", "a") #Opens the file that has high scores from appending.

    if name == "reset": #Clear the file list of scores when the name 'reset' is entered.
        file=open("scoreBoard.txt","w")
    else:
        file.write(str(self.score)) #The score intergers are turned into string.
        file.write("    ----    ") #Text is shown in file.
        file.write(name+"\n") #Displays name in the file and adds a line.
        file.close() #Close file.

    inputFile = open("scoreBoard.txt", "r") #Opens the score file which we can read.
    lineList = inputFile.readlines() #Line list is equal to  each line of the list.
    lineList.sort() #Lines are sorted in alphabetical order.
    top = [] #Top scores are displayed.
    top5 = (lineList[-5:]) #For top 10 these are the last 10 figures.
    for line in top5: #For each of the lines.
      point = line.split("    ----    ")
      top.append((int(point[0]), point[1]))
    file.close() #Close file.
    top.sort()
    top.reverse()
    return_string = ""
    for i in range(len(top)):
      return_string +="{}    ----    {}\n".format(top[i][0], top[i][1])
    print(return_string) #Tests are shown on the console.
    darkresults_page = DarkResultsPage(base) #object
    darkresults_page.scoreboard_label.config(text = return_string) #Configures scoreboard label to display top 5 names in results class.


#Scoreboard class.
class ResultsPage:
    def __init__(self, parent):
      #Setting up the frame.
      self.results_frame = Frame(parent)
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.
      self.results_frame.pack(fill="both", expand=True)


      self.bg_image = Image.open("lightbackground.png") 
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      base.configure(bg = background_color) 
      self.bg_label= Label(self.results_frame, image=self.bg_image)
      self.bg_label.place(x=0, y=0) # make label fit the parent window always


      #Label widget for title logo.
      self.logo_image = Image.open("titlelogo.png") #need to use Image if need to resize
      self.logo_image = self.logo_image.resize((140, 120), Image.ANTIALIAS)
      self.logo_image = ImageTk.PhotoImage(self.logo_image)
      self.logo_label= Label(self.results_frame, image=self.logo_image, borderwidth = 0)
      self.logo_label.place(x = 20, y = 40)

      #Title label.
      self.title_label = Label(self.results_frame, text = "RESULTS", font =("Helvitica","20", "bold"), bg = '#d8e9da', highlightbackground = 'black', width = 20, highlightthickness = 2)
      self.title_label.place(x = 300, y = 40)

      #Description label.
      self.description_label = Label(self.results_frame, text = "SCORE           NAME", font =("Helvitica","16", "bold"), bg = '#d8e9da', highlightbackground = 'black', width = 18, highlightthickness = 2)
      self.description_label.place(x = 370, y = 130)

      #Scoreboard label.
      self.scoreboard_label = Label(self.results_frame, text = "scores", font =("Helvitica","14", "bold"), highlightbackground = 'black', pady = 10, bg = '#d8e9da', width = 18, highlightthickness = 8)
      self.scoreboard_label.place(x = 380, y = 180)

      #Exit to menu button.
      self.exitquiz_button = Button(self.results_frame, text = "EXIT QUIZ", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#F07470', pady=10, width = 15, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit)
      self.exitquiz_button.place(x = 20, y = 530)

    def exit(self):
      base.destroy()



#Dark version Scoreboard class.
class DarkResultsPage:
    def __init__(self, parent):
      #Setting up the frame.
      self.results_frame = Frame(parent)
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.
      self.results_frame.pack(fill="both", expand=True)


      self.bg_image = Image.open("darkbackground.png") 
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      base.configure(bg = background_color2) 
      self.bg_label= Label(self.results_frame, image=self.bg_image)
      self.bg_label.place(x=0, y=0) # make label fit the parent window always

      #Label widget for title logo.
      self.logo_image = Image.open("darktitlelogo.png")
      self.logo_image = ImageTk.PhotoImage(self.logo_image)
      self.logo_label= Label(self.results_frame, image=self.logo_image, borderwidth = 0)
      self.logo_label.place(x = 20, y = 40)

      #Title label.
      self.title_label = Label(self.results_frame, text = "RESULTS", font =("Helvitica","20", "bold"), foreground = 'white', bg = '#c09891', highlightbackground = 'black', width = 20, highlightthickness = 2)
      self.title_label.place(x = 300, y = 40)

      #Description label.
      self.description_label = Label(self.results_frame, text = "SCORE           NAME", font =("Helvitica","16", "bold"), foreground = 'white', bg = '#c09891', highlightbackground = 'black', width = 18, highlightthickness = 2)
      self.description_label.place(x = 370, y = 130)


      #Scoreboard label.
      self.scoreboard_label = Label(self.results_frame, text = "scores", font =("Helvitica","14", "bold"), foreground = 'white', bg = '#c09891', highlightbackground = 'white', width = 18, highlightthickness = 8)
      self.scoreboard_label.place(x = 380, y = 180)

      #Exit to menu button.
      self.exitquiz_button = Button(self.results_frame, text = "EXIT QUIZ", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#F07470', pady=10, width = 15, highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit)
      self.exitquiz_button.place(x = 20, y = 530)

    def exit(self):
      base.destroy()



#Run Programe.

if __name__== "__main__": #If this is the file name then it will be able to run.
  base = Tk() #Creates Window.
  base.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(base) #Making an instance of the class QuizMenu (instantation).
  base.mainloop() #Shows window until user closes it.