from tkinter import * #Importing tkinter so I can use the widgets.

#Defining Variables.
background_color = "mint cream"
class MenuPage:
  def __init__(self, parent):
    #Setting up the frame.
    self.quiz_frame = Frame(parent, bg=background_color, padx=80, pady=80)
    self.quiz_frame.grid() #Grid/table structure window.
    #Label widget for heading.
    self.heading_label=Label(self.quiz_frame, text="Mental Health Quiz", font=("Helvetica", "22", "bold"), foreground = 'black', bg= '#D9EAD3', highlightthickness=2, highlightbackground='black') #The label is text.
    self.heading_label.grid(row=0, column=0, padx=10)
    self.user_label=Label(self.quiz_frame, text="Hi there! Welcome to the mental health quiz. \n Please enter your name below and press start to begin:", font=("Helvetica","14"),bg=background_color)
    self.user_label.grid(row=1, column=0, padx=60, pady=20)


if __name__== "__main__": #If this is the file name then it will be able to run.
  root = Tk() #Creates Window.
  root.title("Mental Health Quiz") #Window Title.
  quiz_instance = MenuPage(root) #Making an instance of the class QuizMenu (instantation).
  root.mainloop() #Shows window until user closes it.


