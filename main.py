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


#geometry #fixed window size dimensions.
#messagebox.showinfo() #error prevention/error messages.

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
    self.value=IntVar() #Holds the value of radio buttons.


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

class QuizPage:
  def __init__(self, parent):
      self.quiz_frame = Frame(parent)
      self.quiz_frame.grid()


class DarkMenuPage:
  def __init__(self, parent):
      self.bg_image1 = Image.open("darkbackground.png") 
      self.bg_image1 = ImageTk.PhotoImage(self.bg_image1)
      base.configure(bg = background_color2) 
      #Setting up the frame.
      self.quiz_frame = Frame(parent)
      self.quiz_frame.grid() #Grid/table structure window.
      base.geometry("1050x600") #Geometry used to create a fixed window size/window dimensions.

      self.image_label= Label(self.quiz_frame, image=self.bg_image1)
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


class DarkQuizPage:
  pass


#Run Programe.

if __name__== "__main__": #If this is the file name then it will be able to run.
  base = Tk() #Creates Window.
  base.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(base) #Making an instance of the class QuizMenu (instantation).
  base.mainloop() #Shows window until user closes it.

