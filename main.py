from tkinter import *
from math import *

notvalidexp="res.configure(text = 'not valid calc')"

def evaluateEvent(event):
    evaluateValue()

def evaluateValue():
    try:
    	res.configure(text = "Result: " + str(eval(entry.get())))
    except:
    	eval(notvalidexp)

def set_text(text):
    ind = len(entry.get())+1
    entry.insert(ind,text)
    return

def delete_text():
    entry.delete(0,END)
    res.configure(text = "Result: 0")
    return

def displayNumButtons(root):
	bottomFrame = Frame(root)
	bottomFrame.pack(side=BOTTOM)

	zero = Button(bottomFrame, text="0", command=lambda:set_text(str(0))).grid(row="0",column="1")
	multi = Button(bottomFrame, text="*", command=lambda:set_text("*")).grid(row="0",column="2")
	div = Button(bottomFrame, text="/", command=lambda:set_text("/")).grid(row="0",column="3")
	
	numButtons = []
	for i in range(9):
		numButtons.append("Button(bottomFrame, text=str("+str(int(i+1))+"), command).grid(row="+str(int(1+i//3))+", column="+str(int(1+i%3))+")")

	for i in range(9):
		buttoncommand = "command=lambda:set_text("+str(int(i+1))+")"
		numButtons[i] = numButtons[i].replace('command', buttoncommand)
		eval(numButtons[i])

	## print(numButtons)

def stylingMethod(root):
	root.geometry('190x200+550+200')
	root.iconbitmap('calculator.ico')
	root.title('Calculator')
	root.option_add('*Text*background', '#FFFFFF')
	root.option_add('*Button*foreground', '#FFFFFF')
	root.option_add('*Button*background', '#52809C')
	root.option_add('*Button*relief', 'raised')
	root.option_add('*Button*width', '7')
	root.resizable(width=False, height=False)


root = Tk()

stylingMethod(root)


displayFrame = Frame(root)
displayFrame.pack()

entry = Entry(displayFrame)
entry.bind("<Return>", evaluateEvent)
entry.pack(side=TOP, fill=X)
res = Label(displayFrame)
res.pack(side=LEFT, fill=NONE)
closeButton = Button(displayFrame, text="Quit",command=displayFrame.quit).pack(side=RIGHT, fill=Y)


topFrame = Frame(root)
topFrame.pack()


delButton = Button(topFrame, text="DEL",command=delete_text).pack(side=LEFT, fill=Y)
equalButton = Button(topFrame, text="=",command=evaluateValue).pack(side=TOP, fill=X)
addButton = Button(topFrame, text="+",command=lambda:set_text("+")).pack(side=LEFT, fill=BOTH)
subButton = Button(topFrame, text="-",command=lambda:set_text("-")).pack(side=TOP, fill=NONE)

displayNumButtons(root)

root.mainloop()