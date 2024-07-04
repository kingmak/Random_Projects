from Tkinter import *
import tkMessageBox

def buttonEvent(event):
	tkMessageBox.showinfo('Error', 'Access Denied!\nUsername or Password wrong')

root = Tk()
root.config(cursor = 'plus')
root.option_add('*Font', 'Courier 24') # global font
root.option_add('*Background', 'grey30') #grey30
root.configure(bg = 'grey30') #grey63

root.bind('<Return>', buttonEvent)

w, h = 604, 300
x = (root.winfo_screenwidth() / 2) - (w / 2)
y = (root.winfo_screenheight() / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

userNameLbl = Label(root, width = 10, fg = 'orange', text = 'UserName: ', anchor = 'w')
userNameLbl.place(x = 50, y = 50)
#userNameLbl.config(font = ('Courier', 24))

userNameInput = Entry(root, relief = RIDGE, width = 35, fg = 'light green', selectbackground = 'black')
userNameInput.place(x = 50, y = 85)
#userNameInput.config(font = ('Courier', 24))

passWordLbl = Label(root, width = 10, fg = 'orange', text = 'PassWord: ', anchor = 'w')
passWordLbl.place(x = 50, y = 140)
#passWordLbl.config(font = ('Courier', 24))

passWordInput = Entry(root, relief = RIDGE, width = 35, fg = 'light green', selectbackground = 'black', show = '*')
passWordInput.place(x = 50, y = 175)
#passWordInput.config(font = ('Courier', 24))

submitBtn = Button(root, text = 'Submit', highlightbackground = 'white', command = lambda: buttonEvent(None))
submitBtn.place(x = 250, y = 240)
submitBtn.config(font = ('Courier', 28))

root.title('Pass Man by KingMak')
root.resizable(0, 0)
root.mainloop()
