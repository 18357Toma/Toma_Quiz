#Imports.
from tkinter import * #Importing tkinter so I can use the widgets.
import random
from tkinter import messagebox

#Defining Variables.
background_color = "mint cream"
background_color2 = "black"
username_list = []
asked = []
score = 0

#Global
global question_answer


#geometry #fixed window size dimensions.
#messagebox.showinfo() #error prevention/error messages.

#Classes.

class MenuPage:
  def __init__(self, parent):
    #Setting up the frame.
    self.quiz_frame = Frame(parent, padx=80, pady=80, bg = background_color)
    self.quiz_frame.grid() #Grid/table structure window.
    base.geometry("1050x600")

    #Label widget for heading.
    self.heading_label=Label(self.quiz_frame, text="Mental Health Quiz", font=("Helvetica", "30", "bold"), foreground = 'black', bg= '#D9EAD3', highlightthickness=2, highlightbackground='black') #The label is text.
    self.heading_label.grid(row=1, column=2, padx=10)

    #Subtitle text.
    self.user_label=Label(self.quiz_frame, text="Hi there! Welcome to the mental health quiz. \n Please enter your name below and press start to begin:", font=("Helvetica","16"),bg=background_color)
    self.user_label.grid(row=2, column=2, padx=60, pady=40)

    #Enter name box.
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=3, column = 2, padx=20, pady=20, ipadx=60, ipady=10)
    self.value=IntVar() #Holds the value of radio buttons.


    #Dark theme button.
    self.theme1_button = Button(self.quiz_frame, text="Dark theme", font=("Helvetica","14", 'bold'), foreground = 'black', bg=background_color, padx=10, pady=10, background = "dark gray", highlightthickness=2, highlightbackground='black', activebackground='light gray', relief= FLAT, command=self.dark_theme)
    self.theme1_button.grid(row=0, column=1)

    #Light theme button.
    self.theme2_button = Button(self.quiz_frame, text="Light theme", font=("Helvetica","14", 'bold'), foreground = 'black', bg=background_color, padx=10, pady=10, background = "white", highlightthickness=2, highlightbackground='black',  activebackground='light gray', relief= FLAT)
    self.theme2_button.grid(row=0, column=3)

    #Start button.
    self.start_button = Button(self.quiz_frame, text="START", font=("Helvetica", "18", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness=2, highlightbackground='black',  activebackground='light gray', command=self.name_collection)
    self.start_button.grid(row=4, column=2, padx=20, pady=40, ipadx=30, ipady=10)
  

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



      
    #messagebox



class QuizPage:
  def __init__(self, parent):
    self.quiz_frame=Frame(parent , bg=background_color , padx=80, pady=80)
    self.quiz_frame.grid()


class DarkMenuPage:
  def __init__(self, parent):
    #Setting up the frame.
    self.quiz_frame = Frame(parent, padx=80, pady=80, bg = background_color2)
    self.quiz_frame.grid() #Grid/table structure window.
    base.geometry("1050x600")

    #Label widget for heading.
    self.heading_label=Label(self.quiz_frame, text="Mental Health Quiz", font=("Helvetica", "30", "bold"), foreground = 'white', bg = background_color2, highlightthickness=2, highlightbackground='white') #The label is text.
    self.heading_label.grid(row=1, column=2, padx=10)

    #Subtitle text.
    self.user_label=Label(self.quiz_frame, text="Hi there! Welcome to the mental health quiz. \n Please enter your name below and press start to begin:", font=("Helvetica","16"), foreground = 'white', bg=background_color2)
    self.user_label.grid(row=2, column=2, padx=60, pady=40)

    #Enter name box.
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=3, column = 2, padx=20, pady=20, ipadx=60, ipady=10)
    self.value=IntVar() #Holds the value of radio buttons.

    #Dark theme button.
    self.theme1_button = Button(self.quiz_frame, text="Dark theme", font=("Helvetica","14", 'bold'), foreground = 'white', bg=background_color, padx=10, pady=10, background = "dark gray", highlightthickness=2, highlightbackground='white', activebackground='light gray', relief= FLAT)
    self.theme1_button.grid(row=0, column=1)

    #Light theme button.
    self.theme2_button = Button(self.quiz_frame, text="Light theme", font=("Helvetica","14", 'bold'), foreground = 'black', bg=background_color, padx=10, pady=10, background = "white", highlightthickness=2, highlightbackground='white',  activebackground='light gray', relief= FLAT, command=self.light_theme)
    self.theme2_button.grid(row=0, column=3)
  
    #Start button.
    self.start_button = Button(self.quiz_frame, text="START", font=("Helvetica", "18", 'bold'), foreground = 'white', bg= '#775144', highlightthickness=2, highlightbackground='white',  activebackground='light gray', command=self.name_collection)
    self.start_button.grid(row=4, column=2, padx=20, pady=40, ipadx=30, ipady=10)


  def light_theme(self):
    self.quiz_frame.destroy()
    MenuPage(base)

  #Name Colection.
  def name_collection(self):
    name=self.entry_box.get()
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


class DarkQuizPage:
  pass


#Run Programe.

if __name__== "__main__": #If this is the file name then it will be able to run.
  base = Tk() #Creates Window.
  base.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(base) #Making an instance of the class QuizMenu (instantation).
  base.mainloop() #Shows window until user closes it.

