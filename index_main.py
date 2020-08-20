from tkinter import *
from translate import Translator  # pip install translate


def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())  # using the Translator() as a variable
    translation = translator.translate(var.get())
    var1.set(translation)

# creating a window
root = Tk()
root.title("Dubey's Translator")

# designing the window
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=10, padx=10)

lan1 = StringVar(root)
lan2 = StringVar(root)

# providing the dropdown list
choices = {'English', 'Hindi', 'Gujarati', 'Spanish', 'German', 'French'}
lan1.set('English')  # intial input language - default
lan2.set('Hindi')  # language to translate - default

# this will be displayed in the window
Label(mainframe, text="*******************************************\n"
                      "***** Welcome to Dubey's Translator *****\n"
                      "*******************************************").grid(row=0, column=2)

lan1menu = OptionMenu(mainframe, lan1, *choices)
Label(mainframe, text="Select a language to type").grid(row=1, column=1)
lan1menu.grid(row=2, column=1)

lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="Select a language to translate").grid(row=1, column=2)
lan2menu.grid(row=2, column=2)

Label(mainframe, text="Enter text").grid(row=3, column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=3, column=1)

Label(mainframe, text="Output").grid(row=3, column=2)
var1 = StringVar()
textbox1 = Entry(mainframe, textvariable=var1).grid(row=3, column=3)

b = Button(mainframe, text='Translate', command=translate).grid(row=4, column=1, columnspan=2)

root.mainloop()
