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
  1: ["It doesn’t matter how much sleep you get, you can always function your best.", "True", "False. 8 - 10 hours is recommended.", "It depends on the day.", "Any amount of sleep is okay as long as you have naps in the day.", "False. 8 - 10 hours is recommended." , 2],

  2: [" What is the difference between mental health and mental illness?" , "There isn’t a difference." , "Mental illnesses are untreatable whereas mental health can be cared for." , "Illness is branched from mental health \n and can affect a person’s performance, \n mental health is the state of your emotional well being." , "Mental health is physical wellbeing whereas mental illnesses affect the brain’s ability to function." , "Illness is branched from mental health and can affect a person’s performance, \n mental health is the state of your emotional well being." , 3],

  3: ["What type of people are affected by mental health issues?" , "Usually teenagers." , "People who get bullied at school." , "Depressed kids." , "A person of any age with any reason." , "A person of any age with any reason." , 4],

  4: ["How should you approach someone that looks upset?" , "Be sincere and ask if there’s anything you can do for them, \n show your sympathy and let them have space." , "Punch them, pull their hair and push them to the ground \n saying “Stop being a cry baby!”." , "Insist on helping them with anything you think you can, \n even if they say no." , "Avoid approaching them, give them their space \n and let them deal with it on their own.", "Be sincere and ask if there’s anything you can do for them, \n show your sympathy and let them have space." , 1],

  5: ["How many people have been affected by mental health in New Zealand?" , "10." , "50%" , "1 in 4 people" , "Everyone" , "Everyone" , 4],

  6: ["What is a good way to cope with poor mental health?" , "Eat, eat, eat and eat the feelings away." , "Take time to enjoy things such as hobbies, \n things you are good at and talk to someone if you \n feel it would help release the stress." , "Try to stay occupied by school work and join lots of social clubs." , "Involve yourself more in class or sports and push yourself to the limits to distract you from the problem." , "Take time to enjoy things such as hobbies, \n things you are good at and talk to someone if you \n feel it would help release the stress.", 2],

  7: ["Which Mental health issue affects people the most?" , "Paranoia (distrust of others or feeling like someone is after you)." , "Depression \n (persistent upset emotions or lack of interest in things, significantly affecting life activities)." , "Eating disorder \n (abnormal/unusual and unhealthy eating habits)." , "OCD \n (Obsessive compulsive disorder, repeating behavioural habits due to immoderate thoughts)." , "Depression \n (persistent upset emotions or lack of interest in things, significantly affecting life activities)." , 2],

  8: ["What is the best thing to do when you see someone enjoying their day?" , "Nothing, or vibe with them." , "Ruin their day." , "Punch them." , "Make jokes and laugh at them with friends.", "Nothing, or vibe with them.", 1],

  9: ["Do people who suffer from serious mental issues deserve special treatment?" , "No, I think we should punch them.", "Yes, it’s nearly impossible to live through life with such difficult problems." , "Acknowledge that they have struggles and don’t persist in bringing them up. \n Sometimes it’s best to treat them like you should treat anyone, \n with respect and not like a child.", "Treat them with anything you can such as helping \n them grab their food at lunch or helping out with school work. Never let them be on their own to do things because they need help." , "Acknowledge that they have struggles and don’t persist in bringing them up. \n Sometimes it’s best to treat them like you should treat anyone, \n with respect and not like a child." , 3],

  10: ["What shouldn’t you do to someone who is having a rough time with their mental wellbeing?" , "Give them coffee." , "Suggest different ways of distractions such as  colouring a book." , "Offer them to go out into a better space or even go for a run with them." , "Punch them." , "Punch them." , 4],
}

#Functions.

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
    self.bg_image1 = Image.open("lightbackground.png") 
    self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
    base.configure(bg = background_color) 
    #Setting up the frame.
    self.quiz_frame = Frame(parent)
    self.quiz_frame.grid() #Grid/table structure window.
    base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

    self.image_label= Label(self.quiz_frame, image=self.bg_image1)
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always


    self.bg_image = Image.open("quiztitle.png") #need to use Image if need to resize
    self.bg_image = self.bg_image.resize((500, 100), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
    #Label widget for heading.
    self.heading_label = Label(self.quiz_frame, image=self.bg_image, borderwidth = 0) #The label is text.
    self.heading_label.grid(row = 1, column = 2, padx = 10)

    #Subtitle text.
    self.user_label = Label(self.quiz_frame, text="Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), bg = background_color)
    self.user_label.grid(row = 2, column = 2, padx = 60, pady = 40)

    #Enter name box.
    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 3, column = 2, padx = 20, pady = 20, ipadx = 80, ipady = 10)


    #Dark theme button.
    self.theme1_button = Button(self.quiz_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'black', activebackground = 'light gray', relief = RAISED, pady = 10, padx = 10, command = self.dark_theme)
    self.theme1_button.grid(row = 0, column = 1, pady = 20, padx = 20)

    #Light theme button.
    self.theme2_button = Button(self.quiz_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'black',  activebackground = 'light gray', relief = RAISED, pady = 10, padx = 10)
    self.theme2_button.grid(row = 0, column = 3, pady = 20, padx = 20)

    #Start button.
    self.start_button = Button(self.quiz_frame, text = "START", font = ("Helvetica", "18", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness = 2, highlightbackground = 'black',  activebackground = 'light gray', command = self.name_collection)
    self.start_button.grid(row = 4, column = 2, padx = 20, pady = 40, ipadx = 30, ipady = 10)
  

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
      self.bg_image1 = Image.open("darkbackground.png") 
      self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
      base.configure(bg = background_color2) 
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      self.quiz_frame.grid() #Grid/table structure window.
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      self.image_label= Label(self.quiz_frame, image = self.bg_image1)
      self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always

      #Label widget for heading.
      self.bg_image = Image.open("darkquiztitle.png") #need to use Image if need to resize
      self.bg_image = self.bg_image.resize((500, 100), Image.ANTIALIAS)
      self.bg_image = ImageTk.PhotoImage(self.bg_image)
      #Label widget for heading.
      self.heading_label = Label(self.quiz_frame, image=self.bg_image, borderwidth = 0) #The label is text.
      self.heading_label.grid(row = 1, column = 2, padx = 10)

      #Subtitle text.
      self.user_label = Label(self.quiz_frame, text = "Hi there! \n \n Enter your name below and press start to begin:", font = ("Helvetica","16"), foreground = 'white', bg = background_color2)
      self.user_label.grid(row = 2, column = 2, padx = 60, pady = 40)

      #Enter name box.
      self.entry_box = Entry(self.quiz_frame)
      self.entry_box.grid(row = 3, column = 2, padx = 20, pady = 20, ipadx = 80, ipady = 10)
      self.value = IntVar() #Holds the value of radio buttons.

      #Dark theme button.
      self.theme1_button = Button(self.quiz_frame, text = "Dark theme", font = ("Helvetica","14", 'bold'), foreground = 'white', bg = background_color, background = "dark gray", highlightthickness = 2, highlightbackground = 'white', activebackground = 'light gray', relief = RAISED, padx = 10, pady = 10)
      self.theme1_button.grid(row = 0, column = 1, pady = 20, padx = 20)

      #Light theme button.
      self.theme2_button = Button(self.quiz_frame, text = "Light theme", font = ("Helvetica","14", 'bold'), foreground = 'black', bg = background_color, background = "white", highlightthickness = 2, highlightbackground = 'white',  activebackground = 'light gray', relief = RAISED, padx = 10, pady = 10, command = self.light_theme)
      self.theme2_button.grid(row = 0, column = 3, pady = 20, padx = 20)
    
      #Start button.
      self.start_button = Button(self.quiz_frame, text = "START", font = ("Helvetica", "18", 'bold'), foreground = 'white', bg = '#775144', highlightthickness = 2, highlightbackground = 'white',  activebackground = 'light gray', relief = RAISED, command = self.name_collection)
      self.start_button.grid(row = 4, column = 2, padx = 20, pady = 40, ipadx = 30, ipady = 10)


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
      self.quiz_frame.grid() #Grid/table structure window.
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      shuffle()

      self.value=IntVar() #Holds the value of radio buttons.

      #question
      self.question_label = Label(self.quiz_frame, text = question_answer[qnum][0], font =("Helvitica","16", "bold"), foreground = 'black', bg = '#d8e9da', highlightbackground = 'black', highlightthickness = 2)
      self.question_label.grid(row = 1, column = 2, padx = 20 , pady = 20, ipady = 10, ipadx = 10)

      #radio button 1.
      self.option1= Radiobutton(self.quiz_frame, text=question_answer[qnum][1], font=("Helvetica","14"), foreground = 'black', bg=background_color, value=1, padx=10, pady = 10, variable = self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left")
      self.option1.grid(row = 2, column = 1, sticky = W, ipady = 10, ipadx = 10)

      #radio button 2
      self.option2 = Radiobutton(self.quiz_frame, text=question_answer[qnum][2], font=("Helvetica","14"), foreground = 'black', bg=background_color, value=2, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left")
      self.option2.grid(row=2, column = 2, sticky=W, ipady = 10, ipadx = 10)

      #radio button 3
      self.option3=Radiobutton(self.quiz_frame, text=question_answer[qnum][3], font=("Helvetica","14"), foreground = 'black', bg=background_color, value=3, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left")
      self.option3.grid(row=3, column = 1, sticky=W, ipady = 10, ipadx = 10)

      #radio button 4
      self.option4=Radiobutton(self.quiz_frame, text=question_answer[qnum][4], font=("Helvetica","14"), foreground = 'black', bg=background_color, value=4, padx=10, pady=10, variable=self.value, background = "white", activebackground='mint cream',  indicatoron = 0, highlightbackground = 'black', highlightthickness = 2, relief = RAISED, justify="left")
      self.option4.grid(row=3, column = 2, sticky=W, ipady = 10, ipadx = 10)

class DarkQuizPage:
  def __init__(self, parent):
      self.bg_image1 = Image.open("darkbackground.png") 
      self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
      base.configure(bg = background_color2) 
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      self.quiz_frame.grid() #Grid/table structure window.
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.


#Run Programe.

if __name__== "__main__": #If this is the file name then it will be able to run.
  base = Tk() #Creates Window.
  base.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(base) #Making an instance of the class QuizMenu (instantation).
  base.mainloop() #Shows window until user closes it.

