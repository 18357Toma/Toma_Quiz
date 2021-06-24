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
score = 0

#Global
global question_answer

question_answer = {
  1: ["It doesn’t matter how much sleep you get, you can always function your best.", "True", "False. 8 - 10 hours is recommended.", "It depends on the day.", "Any amount of sleep is okay as long as you have naps in the day.", "Varied age groups have different times recommended but from 13 - 18 years old, 8 - 10 hours sleep is suggested." , 2],

  2: [" What is the difference between mental health and mental illness?" , "There isn’t a difference." , "Mental illnesses are untreatable whereas mental health can be cared for." , "Illness is branched from mental health  and can affect a person’s performance, mental health is the state of your emotional well being." , "Mental health is physical wellbeing whereas mental illnesses affect the brain’s ability to function." , "Although the terms are misunderstood a lot, it is good to understand that mental health doesn’t only refer to disorders, and mental illnesses aren’t only associated with feelings." , 3],

  3: ["What type of people are affected by mental health issues?" , "Usually teenagers." , "People who get bullied at school." , "Depressed kids." , "All of the above.", "Everyone endures life challenges and therefore anybody can be affected by issues of mental health for different problems." , 4],

  4: ["How should you approach someone that looks upset?" , "Be sincere and ask if there’s anything you can do for them, show your sympathy and let them have space." , "Punch them, pull their hair and push them to the ground saying “Stop being a cry baby!”." , "Insist on helping them with anything you think you can, even if they say no." , "Avoid approaching them, give them their space and let them deal with it on their own.", "(Although we should be kind, we need to respect the boundaries of someone who is feeling unwell)." , 1],

  5: ["How many people have been affected by mental health in New Zealand?" , "10." , "50%" , "1 in 4 people" , "Everyone" , "(Everyone has had a point in time where they felt like they had no energy :, as well as a time when they had all the energy in the world." , 4],

  6: ["What is a good way to cope with poor mental health?" , "Eat, eat, eat and eat the feelings away." , "Take time to enjoy things such as hobbies, things you are good at and talk to someone if you feel it would help release the stress." , "Try to stay occupied by school work and join lots of social clubs." , "Involve yourself more in class or sports and push yourself to the limits to distract you from the problem." , "Distracting yourself by over involving in activities is more stressful to handle than the problem itself. Taking a break from everything and having someone by your side will surely calm the tension of the problem." , 2],

  7: ["Which Mental health issue affects people the most?" , "Paranoia (distrust of others or feeling like someone is after you)." , "Depression (persistent upset emotions or lack of interest in things, significantly affecting life activities)." , "Eating disorder (abnormal/unusual and unhealthy eating habits)." , "OCD (Obsessive compulsive disorder, repeating behavioural habits due to immoderate thoughts)." , "These mental issues may be familiar to you and depression is probably the most common issue which is most commonly suffered by people." , 2],

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
    self.quiz_frame = Frame(parent)
    self.quiz_frame.grid() #Grid/table structure window.
    base.geometry("980x600")

    self.bg_image1 = Image.open("lightbackground.png") 
    self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
    base.configure(bg = background_color) 
    #Setting up the frame.

    self.image_label= Label(self.quiz_frame, image=self.bg_image1)
    self.image_label.place(x=0, y=0) # make label fit the parent window always


    self.bg_image = Image.open("quiztitle.png")
    #need to use Image if need to resize
    self.bg_image = self.bg_image.resize((500, 100), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
    #Label widget for heading.
    self.heading_label = Label(self.quiz_frame, image=self.bg_image, borderwidth = 0) #The label is text.
    self.heading_label.grid(row = 1, column = 1, padx = 10)

    #Subtitle text.
    self.user_label = Label(self.quiz_frame, text="Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), bg = background_color)
    self.user_label.grid(row = 2, column = 1, padx = 20, pady = 20)

    #Enter name box.
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 80, ipady = 10)


    #Dark theme button.
    self.theme1_button = Button(self.quiz_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'black', activebackground = 'light gray', padx=10, pady=10, relief = RAISED, command = self.dark_theme)
    self.theme1_button.grid(row = 0, column = 0, pady = 20, padx = 20)

    #Light theme button.
    self.theme2_button = Button(self.quiz_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'black',  activebackground = 'light gray', padx=10, pady=10, relief = RAISED)
    self.theme2_button.grid(row = 0, column = 2, pady = 20, padx = 20)

    #Start button.
    self.start_button = Button(self.quiz_frame, text = "START", font = ("Helvetica", "18", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.name_collection)
    self.start_button.grid(row = 4, column = 1, padx = 20, pady = 40, ipadx = 30, ipady = 10)
  

  def dark_theme(self):
      self.quiz_frame.destroy()
      DarkMenuPage(base)

  #Name Colection.
  def name_collection(self):
      name=self.entry_box.get()
      if str.isalpha(name) == True and len(name) >0 and len(name) <=10:
        username_list.append(name)
        self.quiz_frame.destroy() #destroy the starter
        QuizPage(base)
      elif str.isalpha(name) == False :
        messagebox.showerror("Name error:", "Please check that you are only using letters and no other characters or numerals.")
      elif len(name) <0:
        messagebox.showerror("Name error:", "Please check that you have entered a name.")
      elif len(name) >10:
        messagebox.showerror("Name error:", "Please check that you have entered a name up to 10 characters.")


class DarkMenuPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      self.quiz_frame.grid() #Grid/table structure window.
      base.geometry("980x600") #Geometry used to create a fixed window size/window dimensions.

      self.bg_image1 = Image.open("darkbackground.png")
      self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
      base.configure(bg = background_color2)
      self.image_label= Label(self.quiz_frame, image = self.bg_image1)
      self.image_label.place(x=0, y=0) # make label l to fit the parent window always

      #Label widget for heading.
      self.bg_image = Image.open("darkquiztitle.png") #need to use Image if need to resize
      self.bg_image = self.bg_image.resize((500, 100), Image.ANTIALIAS)
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      #Label widget for heading.
      self.heading_label = Label(self.quiz_frame, image=self.bg_image, borderwidth = 0) #The label is text.
      self.heading_label.grid(row = 1, column = 1, padx = 10)

      #Subtitle text.
      self.user_label = Label(self.quiz_frame, text = "Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), foreground = 'white', bg = background_color2)
      self.user_label.grid(row = 2, column = 1, padx = 20, pady = 20)

      #Enter name box.
      self.entry_box = Entry(self.quiz_frame)
      self.entry_box.grid(row = 3, column = 1, padx = 20, pady = 20, ipadx = 80, ipady = 10)
      self.value = IntVar() #Holds the value of radio buttons.

      #Dark theme button.
      self.theme1_button = Button(self.quiz_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'white', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'white', activebackground = 'light gray',  padx=10, pady=10, relief = RAISED)
      self.theme1_button.grid(row = 0, column = 0, pady = 20, padx = 20)

      #Light theme button.
      self.theme2_button = Button(self.quiz_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'white',  activebackground = 'light gray',  padx=10, pady=10, relief = RAISED, command = self.light_theme)
      self.theme2_button.grid(row = 0, column = 2, pady = 20, padx = 20)
    
      #Start button.
      self.start_button = Button(self.quiz_frame, text = "START", font = ("Helvetica", "16", 'bold'), foreground = 'white', bg = '#775144', highlightthickness = 2, highlightbackground = 'white',  activebackground = '#60100B', activeforeground = 'white', relief = RAISED, command = self.name_collection)
      self.start_button.grid(row = 4, column = 1, padx = 20, pady = 40, ipadx = 30, ipady = 10)


  def light_theme(self):
      self.quiz_frame.destroy()
      MenuPage(base)

  #Name Colection.
  def name_collection(self):
      name = self.entry_box.get()
      if str.isalpha(name) == True and len(name) >0 and len(name) <=10:
        username_list.append(name)
        self.quiz_frame.destroy() #destroy the starter
        DarkQuizPage(base)
      elif str.isalpha(name) == False :
        messagebox.showerror("Name error:", "Please check that you are only using letters and no other characters or numerals.")
      elif len(name) <0:
        messagebox.showerror("Name error:", "Please check that you have entered a name.")
      elif len(name) >10:
        messagebox.showerror("Name error:", "Please check that you have entered a name up to 10 characters.")


class QuizPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent, bg = background_color)
      self.quiz_frame.grid()
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      shuffle()

      self.value=IntVar() #Holds the value of radio buttons.

      #Label widget for title logo.
      #self.logo_image = Image.open("titlelogo.png") #need to use Image if need to resize
      #self.logo_image = self.logo_image.resize((140, 120), Image.ANTIALIAS)
      #self.logo_image = ImageTk.PhotoImage(self.logo_image)
      #self.image_label= Label(self.quiz_frame, image=self.logo_image, borderwidth = 0)
      #self.image_label.grid(column = 0, row = 0)

      #question
      self.question_label = Label(self.quiz_frame, text = question_answer[qnum][0], font =("Helvitica","16", "bold"), foreground = 'black', bg = '#d8e9da', highlightbackground = 'black', highlightthickness = 2, wraplength = 600)
      self.question_label.grid(column = 1, row = 0, pady=10, padx=10)

      #radio button 1.
      self.option1= Radiobutton(self.quiz_frame, text=question_answer[qnum][1], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=1, variable = self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option1.grid(row = 2, column = 1, sticky = W, padx=10, pady = 10, ipady = 10)

      #radio button 2
      self.option2 = Radiobutton(self.quiz_frame, text=question_answer[qnum][2], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=2, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option2.grid(row=3, column = 1, sticky=W, padx=10, pady = 10, ipady = 10, ipadx = 10)

      #radio button 3
      self.option3=Radiobutton(self.quiz_frame, text=question_answer[qnum][3], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=3, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option3.grid(row=4, column = 1, sticky=W, padx=10, pady = 10, ipady = 10)

      #radio button 4
      self.option4=Radiobutton(self.quiz_frame, text=question_answer[qnum][4], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=4, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option4.grid(row=5, column = 1, sticky=W, padx=10, pady = 10, ipady = 10)

      #Score label.
      self.score_label=Label(self.quiz_frame, text="TOTAL SCORE", font=("Helvetica", "14", "bold"), bg = background_color)
      self.score_label.grid(row=6, column=1)

      #Exit to menu button.
      self.exit_button = Button(self.quiz_frame, text = "EXIT TO MENU", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#F07470', highlightthickness = 2, highlightbackground = 'black',  activebackground = '#DC1C13', command = self.exit)
      self.exit_button.grid(row = 7, column = 0, padx = 20, pady = 20, ipady = 10, ipadx = 10)


      #Next button.
      self.next_button = Button(self.quiz_frame, text = "NEXT", font = ("Helvetica", "14", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness = 2, highlightbackground = 'black',  activebackground = '#649568', command = self.score_calculations)
      self.next_button.grid(row = 7, column = 2, padx = 20, pady = 20, ipady = 10)

  def exit(self):
    self.quiz_frame.destroy()
    MenuPage(base)

  #Question setup.
  def question_change(self):
    shuffle()
    self.value.set(0)
    self.question_label.config(text=question_answer[qnum][0])
    self.option1.config(text = question_answer[qnum][1])
    self.option2.config(text = question_answer[qnum][2])
    self.option3.config(text = question_answer[qnum][3])
    self.option4.config(text = question_answer[qnum][4])

  #Score calculations.
  def score_calculations(self):
    global score
    total_score = self.score_label
    option_choice = self.value.get()
    if len(asked)>9:
      if choice == question_answer[qnum][6]: #If last question is right answer.
        score +=1
        total_score.configure(text= "Score :" + score)
        self.next_button.config(text="Next")
      else: #If last question was wrong answer.
        score +=0
        option_choice.configure(text= "Incorrect:" + question_answer[qnum][5], wraplength = 300)
        self.next_button.config(text="Next")
    else:
      if option_choice == 0: #Check if user made a choice.
        self.next_button.config(text="Sorry you didn't select anything, please retry")
        option_choice=self.value.get()
      else: #If they made choice that isn't last question.
        if option_choice == question_answer[qnum][6]: #If user is right.
          score+=1
          total_score.configure(text=score)
          self.next_button.config(text="Next")
          self.question_change() #Run method for next question to come up.
        else: #If the user chooses wrong answer.
          score +=0
          total_score.configure(text="Incorrect:" + question_answer[qnum][5], wraplength = 300)
          self.next_button.configure(text="Next")
          self.question_change()


class DarkQuizPage:
  def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent, bg = background_color2)
      self.quiz_frame.grid()
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      shuffle()

      self.value=IntVar() #Holds the value of radio buttons.

      #Label widget for title logo.
      #self.logo_image = Image.open("titlelogo.png")
      #self.logo_image = ImageTk.PhotoImage(self.logo_image)
      #self.image_label= Label(self.quiz_frame, image=self.logo_image, borderwidth = 0)
      #self.image_label.grid(column = 0, row = 0)

      #question
      self.question_label = Label(self.quiz_frame, text = question_answer[qnum][0], font =("Helvitica","16", "bold"), foreground = 'white', bg = '#co9891', highlightbackground = 'white', highlightthickness = 2, wraplength = 600)
      self.question_label.grid(column = 1, row = 0, pady=10, padx=10)

      #radio button 1.
      self.option1= Radiobutton(self.quiz_frame, text=question_answer[qnum][1], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=1, variable = self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option1.grid(row = 2, column = 1, sticky = W, padx=10, pady = 10, ipady = 10)

      #radio button 2
      self.option2 = Radiobutton(self.quiz_frame, text=question_answer[qnum][2], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=2, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option2.grid(row=3, column = 1, sticky=W, padx=10, pady = 10, ipady = 10)

      #radio button 3
      self.option3=Radiobutton(self.quiz_frame, text=question_answer[qnum][3], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=3, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option3.grid(row=4, column = 1, sticky=W, padx=10, pady = 10, ipady = 10)

      #radio button 4
      self.option4=Radiobutton(self.quiz_frame, text=question_answer[qnum][4], font=("Helvetica","12"), foreground = 'black', bg=background_color, value=4, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left", width = 35, wraplength = 300)
      self.option4.grid(row=5, column = 1, sticky=W, padx=10, pady = 10, ipady = 10)


      #Exit to menu button.
      self.exit_button = Button(self.quiz_frame, text = "EXIT TO MENU", font = ("Helvetica", "14", 'bold'), foreground = 'white', bg= '#F07470', highlightthickness = 2, highlightbackground = 'white',  activebackground = '#DC1C13', command = self.exit)
      self.exit_button.grid(row = 6, column = 0, padx = 20, pady = 20, ipadx = 20, ipady = 10)

      #Score label.
      self.score_label=Label(self.quiz_frame, text="TOTAL SCORE", font=("Helvetica", "14", "bold"), bg = background_color2)
      self.score_label.grid(row=6, column=1)

      #Next button.
      self.next_button = Button(self.quiz_frame, text = "NEXT", font = ("Helvetica", "14", 'bold'), foreground = 'white', bg= '#D9EAD3', highlightthickness = 2, highlightbackground = 'white',  activebackground = '#649568', command = self.score_calculations)
      self.next_button.grid(row = 6, column = 2, padx = 20, pady = 20, ipadx = 20, ipady = 10)
    
    
  def exit(self):
    self.quiz_frame.destroy()
    DarkMenuPage(base)


#Question setup.
  def question_change(self):
    shuffle()
    self.value.set(0)
    self.question_label.config(text=question_answer[qnum][0])
    self.option1.config(text = question_answer[qnum][1])
    self.option2.config(text = question_answer[qnum][2])
    self.option3.config(text = question_answer[qnum][3])
    self.option4.config(text = question_answer[qnum][4])

  #Score calculations.
  def score_calculations(self):
    global score
    total_score = self.score_label
    option_choice = self.value.get()
    if len(asked)>9:
      if choice == question_answer[qnum][6]: #If last question is right answer.
        score +=1
        total_score.configure(text= "Score :" + score)
        self.next_button.config(text="Next")
      else: #If last question was wrong answer.
        score +=0
        option_choice.configure(text= "Incorrect:" + question_answer[qnum][5])
        self.next_button.config(text="Next")
    else:
      if option_choice == 0: #Check if user made a choice.
        self.next_button.config(text="Sorry you didn't select anything, please retry")
        option_choice=self.value.get()
      else: #If they made choice that isn't last question.
        if option_choice == question_answer[qnum][6]: #If user is right.
          score+=1
          total_score.configure(text=score)
          self.next_button.config(text="Next")
          self.question_change() #Run method for next question to come up.
        else: #If the user chooses wrong answer.
          score +=0
          total_score.configure(text="Incorrect:" + question_answer[qnum][5])
          self.next_button.configure(text="Next")
          self.question_change()


#Run Programe.

if __name__== "__main__": #If this is the file name then it will be able to run.
  base = Tk() #Creates Window.
  base.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(base) #Making an instance of the class QuizMenu (instantation).
  base.mainloop() #Shows window until user closes it.