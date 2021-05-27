#Imports.
from tkinter import * #Importing tkinter so I can use the widgets.

#Defining Variables.
background_color = "mint cream"

#Functions.


#Classes.

class MenuPage:
    def __init__(self, parent):
      #Setting up the frame.
      self.quiz_frame = Frame(parent, bg=background_color, padx=80, pady=80)
      self.quiz_frame.grid() #Grid/table structure window.

      #Label widget for heading.
      self.heading_label=Label(self.quiz_frame, text="Mental Health Quiz", font=("Helvetica", "22", "bold"), foreground = 'black', bg= '#D9EAD3', highlightthickness=2, highlightbackground='black') #The label is text.
      self.heading_label.grid(row=1, column=2, padx=10)

      #Subtitle text.
      self.user_label=Label(self.quiz_frame, text="Hi there! Welcome to the mental health quiz. \n Please enter your name below and press start to begin:", font=("Helvetica","14"),bg=background_color)
      self.user_label.grid(row=2, column=2, padx=60, pady=20)

      #Enter name box.
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=3, column = 2, padx=20, pady=20, ipadx=60, ipady=10)
      self.var1=IntVar() #Holds the value of radio buttons.

      #Start button.
      self.start_button = Button(self.quiz_frame, text="START", font=("Helvetica", "14", 'bold'), foreground = 'black', bg= '#D9EAD3', highlightthickness=2, highlightbackground='black',  activebackground='light cyan')
      self.start_button.grid(row=4, column=2, padx=20, pady=30, ipadx=30, ipady=10)

      #Dark theme button.
      self.theme1_button = Button(self.quiz_frame, text="Dark theme", font=("Helvetica","12", 'bold'), foreground = 'black', bg=background_color, padx=10, pady=10, background = "dark gray", highlightthickness=2, highlightbackground='black', activebackground='light gray', relief= FLAT)
      self.theme1_button.grid(row=0, column=1)

      #Light theme button.
      self.theme2_button = Button(self.quiz_frame, text="Light theme", font=("Helvetica","12", 'bold'), foreground = 'black', bg=background_color, padx=10, pady=10, background = "white", highlightthickness=2, highlightbackground='black',  activebackground='light gray', relief= FLAT)
      self.theme2_button.grid(row=0, column=3)




#Run Programe.
if __name__== "__main__": #If this is the file name then it will be able to run.
  root = Tk() #Creates Window.
  root.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(root) #Making an instance of the class QuizMenu (instantation).
  root.mainloop() #Shows window until user closes it.


