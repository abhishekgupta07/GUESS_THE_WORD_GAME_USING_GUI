#Importing Required Libraries
from tkinter import *
import random
from tkinter import messagebox


root = Tk()
root.geometry("580x350")
root.title("Word Guessing Game")


#Initializing Empty List 
mywords=[]
file1 = open("commonword.txt","r")

#Appending words from file to the list (mywords)
for x in file1:
    mywords.append(x.replace('\n', ''))   #to replace 'new line' character of file to 'space' in list

#choosing random word from the list
word=random.choice(mywords)
random_word=list(word)
p=[]
s='_ '*len(random_word)
p=s.split(' ')              #it makes a list of the character in the empty list
p.pop(len(random_word))     #to update the length after guessing the correct character
actual=random_word.copy()

class guessWord:
    def __init__(self,master):      #master is the tk root widget
        self.count=0
        self.structure(master)      #for packing the widgets   !!!!!!!!!!
        self.rr=master              #to display the blank underline for putting the right guessed character 
        
    #structure() is also a member function of the guessWord class, it defines the structure of GUI.    
    def structure(self,master):
 
        """ Instruction Label """
        # Create instruction label for Program
        self.inst_lbl = Label(master, text = "Welcome to Word Guessing Game!")
        self.inst_lbl.grid(row = 0, column = 1, columnspan = 2, sticky = W)  #columnspan used to cover column for displaying a single message

        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 1, column = 0, sticky = W)

        """ Guess Input """ 
        # Create label for entering Guess  
        self.guess_lbl = Label(master, text = "Enter your Guess:")
        self.guess_lbl.grid(row = 2, column = 0, sticky = W)
 
        # Create entry widget to accept Guess  
        self.guess_ent = Entry(master)
        self.guess_ent.grid(row = 2, column = 1, sticky = W)

        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 3, column = 0, sticky = W)

        # Creating a submit button
        self.submit_bttn = Button(master, text = "Submit",command=self.submit,height=1, width=17)
        self.submit_bttn.grid(row = 4, column =1, sticky = W)
 
        master.bind('<Return>',self.submit)   #bind is to bind the submit button with the master widget
        
        # Create a space  
        self.gap2_lbl = Label(master, text = " ")
        self.gap2_lbl.grid(row = 5, column = 0, sticky = W)
 
         
        self.inst_lb2 = Label(master, text ='Chance:10')
        self.inst_lb2.grid(row = 2, column = 2, columnspan = 2, sticky = W)

        #Creating Label to Display Message
        self.inst_lb3 = Label(master, text ='')
        self.inst_lb3.grid(row = 7, column = 2, columnspan = 2, sticky = W)

        #CReating label to display current Guessed Status of Word
        self.curr_char1 = Label(master, text =p)
        self.curr_char1.place(x=102,y=130)
        self.curr_char = Label(master, text ="Current Status:")
        self.curr_char.place(x=0,y=130)

      
    #to show the corectly guessed character infront of "current guess"    
    def current_status(self,char):
        self.curr_char1 = Label(self.rr, text =char)
        self.curr_char1.place(x=102,y=130)

    #submit is member function of class guessWord. it checks whether the character is present or not. 
    # If present it calls current_status and changes it accordingly
    def submit(self,*args):

        #Taking Entry From Entry Field as a charcter and save it in 'char'
        char=self.guess_ent.get()

        #Checking whether Entry Field is empty or not
        if(len(char)==0):
            messagebox.showwarning("Warning","Entry field is Empty")
        
        #checks whether entry field has only one character or not
        if(len(char)>1):
            messagebox.showwarning("Warning","Enter character of length 1")   
        
        #If the character is in the randomly picked word, then it inserts in the list 'P' at coreect position
        if char in actual and len(char)==1:
            l=actual.count(char)
            for j in range(l):
                i=actual.index(char)
                p.insert(i,char)
                p.pop(i+1)
                actual.insert(i,'_')
                actual.pop(i+1)

            self.inst_lb2.config(text='Chance:'+ str(10-self.count))
            self.inst_lb3.config(text='Right Guessed!')
            self.guess_ent.delete(0, 'end')
            self.current_status(p)

        #If the character is not in the randomly picked word then it will increment the 
        # count and decrement the chance and shows wrong guessed message
        elif(len(char)==1):
            self.count=self.count+1
            self.inst_lb2.config(text='Chance:'+str(10-self.count))
            self.inst_lb3.config(text='Wrong Guessed!')
            self.guess_ent.delete(0, 'end')
            

        #Condition if Player Won
        if( p==random_word):
            self.inst_lb3.config(text='You perfectly guessed the word!')
            messagebox.showinfo("Congratulations!!!", "You Won")
            self.rr.destroy()  #to destroy the popped up window

        #Condition if player Loose
        elif(self.count>=10):
            self.inst_lb3.config(text='You lost... the word is: '+word)
            messagebox.showinfo("Sorry!!!", "You lost please try again!")
            self.rr.destroy()



app = guessWord(root)
print(word)
root.mainloop()







