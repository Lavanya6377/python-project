from textblob import TextBlob
from tkinter import *


# Function to check the spelling and show the corrected spelling
def checkSpelling():
    a = text.get()
    b = TextBlob(a)
    correctedText.set("Now the corrected word is:" +str(b.correct()))


# Creating the window
wn = Tk()
wn.title("Spell Checker")
wn.geometry('500x250')
wn.config(bg='light green')

# Creating the variables to get the word and set the correct word
text = StringVar(wn)

correctedText = StringVar(wn)

# The main label
Label(wn, text='DataFlair Spell Checker', bg='light green',
      fg='gray30', font=('Time New Roman', 20, 'bold')).place(x=100, y=10)

Label(wn, text='Please enter the word', bg='light green', font=('Time New Roman', 13, 'normal'),
      justify=LEFT).place(x=20, y=70)

Entry(wn, textvariable=text, width=35, font=('calibre', 13, 'normal')).place(x=20, y=110)

#correct word
opLabel = Label(wn, textvariable=correctedText, bg='light green', font=('Time New Roman', 13, 'normal'),
                justify=LEFT).place(x=20, y=130)


Button(wn, text="Click Me", bg='dark green', font=('Time New Roman', 13),
       command=checkSpelling).place(x=230, y=190)


wn.mainloop()

