# -*- coding: utf-8 -*-

'''
TODO: fix root quit
TODO: self resizing widgets, self place widges
'''

import os, sys, time, tkFont, urllib2, linecache, tkFileDialog, tkMessageBox
from Tkinter import *

def InsertTimeStamp():
    TimeStamp = time.strftime('%a %b %d %I:%M') + time.strftime('%p').lower()
    Body.insert(INSERT, TimeStamp)

def InsertUserBio():
    Comment = ("'''\nProgram Name:\nAuthor:\nDescription:\n" +
                  time.strftime('%a %b %d %I:%M') +
                  time.strftime('%p').lower() + "\n'''\n") 
    Body.insert(INSERT, Comment)

def EntrySelectAll(event, ObjectName):
    end = len(ObjectName.get())
    ObjectName.select_range (0, end)
    return 'break'

def BodySelectAll(event):
    Body.tag_add(SEL, "1.0", END)
    Body.mark_set(INSERT, "1.0")
    Body.see(INSERT)
    return 'break'

def EntryPopupMenu(event, Determiner):
    FileMenu = Menu(root, tearoff = 0)
    FileMenu.add_command(label = 'Cut', command = lambda: Determiner.event_generate('<<Cut>>'))
    FileMenu.add_command(label = 'Copy', command = lambda: Determiner.event_generate('<<Copy>>'))
    FileMenu.add_command(label = 'Paste', command = lambda: Determiner.event_generate('<<Paste>>'))
    FileMenu.add_command(label = 'Undo', command = lambda: Determiner.event_generate('<<Undo>>'))
    FileMenu.post(event.x_root, event.y_root)
    
def MainMenus():
    FileName = ''    
    def OpenFile():
        Count = 1
        File = str(tkFileDialog.askopenfilename(initialdir = os.getcwd(), title = 'Browse to a File to Open'))#if File == '': error
        if File != '':
            FileName = File
            InserFileName = FileName.split('/')
            DocName.insert(0, InserFileName[len(InserFileName) - 1])
            OpenFile = open(File)
            LenFile = len(OpenFile.readlines())
            while Count <= LenFile:
                Body.insert(INSERT, linecache.getline(File, Count))
                Count += 1

    def SaveFile():
        if FileName == '':
            SaveFileAs()
        else:
            File = open(FileName, 'w')
            File.write(Body.get(1.0, END)[:-1])
            File.close()

    def SaveFileAs():
        if DocName.get() == '':
            Name = 'Untitled.makn'
        elif '.' not in DocName.get():
            Name = DocName.get() + '.makn'            
        else:
            Name = DocName.get()
            
        FilePlace = str(tkFileDialog.askdirectory(initialdir = os.getcwd(), title = 'Where do u wanna save this File?'))
        File = open(os.path.join(FilePlace, Name), 'w')
        File.write(Body.get(1.0, END)[:-1])
        File.close()
          
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text = 'Still Working on This One :D')
        button.pack()

    def quitRoot():
        window = Toplevel(root)
        window.destroy()
          
    Menubar = Menu(root)
    Filemenu = Menu(Menubar, tearoff = 0)
    Menubar.add_cascade(label = 'File', menu = Filemenu)
    Filemenu.add_command(label = 'Open', command = OpenFile)
    Filemenu.add_command(label = 'Save', command = SaveFile)
    Filemenu.add_command(label = 'Save As', command = SaveFileAs)
    Filemenu.add_separator()
    Filemenu.add_command(label = 'Exit', command = root.quit)
    Editmenu = Menu(Menubar, tearoff = 0)
    Menubar.add_cascade(label = 'Edit', menu = Editmenu)
    Editmenu.add_command(label = 'Cut', command = lambda: Body.event_generate('<<Cut>>'))
    Editmenu.add_command(label = 'Copy', command = lambda: Body.event_generate('<<Copy>>'))
    Editmenu.add_command(label = 'Paste', command = lambda: Body.event_generate('<<Paste>>'))
    Editmenu.add_separator()
    Editmenu.add_command(label = 'Undo', command = lambda: Body.event_generate('<<Undo>>'))
    Editmenu.add_command(label = 'Delete', command = donothing)
    Editmenu.add_separator()
    Editmenu.add_command(label = 'Exit', command = quitRoot)
    root.config(menu = Menubar)

root = Tk()
root.config(cursor = 'plus')
root.option_add('*Font', 'Courier 14 bold')
root.option_add('*Background', 'grey30')#grey30
root.configure(bg = 'grey30')#grey63
MainMenus()

w, h = (root.winfo_screenwidth()), (root.winfo_screenheight())
root.geometry("{0}x{1}+0+0".format(w, h - 118))

DocNameLab = Label(root, width = 14, fg = 'orange', text = 'Document Name:', anchor = 'w').place(x = 15, y = 10)
DocName = Entry(root, relief = RIDGE, width = 50, fg = 'orange', selectbackground = 'black')
DocName.bind('<Control-Key-a>', lambda event: EntrySelectAll(event, DocName))
DocName.bind('<Control-Key-A>', lambda event: EntrySelectAll(event, DocName))
DocName.bind('<Button-3>', lambda event: EntryPopupMenu(event, DocName))
DocName.place(x = 230, y = 12)

TimeStampInsert = Button(root, fg = 'orange', text = 'Insert Time Stamp', command = InsertTimeStamp).place(x = 800, y = 4)
CommentInsert = Button(root, fg = 'orange', text = 'Insert Comment Lines', command = InsertUserBio).place(x = 1014, y = 4)

RightScrollbar = Scrollbar(root)
RightScrollbar.pack(side = RIGHT, fill = Y)

Body = Text(root, width = 112, height = 25, fg = 'orange', selectbackground = 'white', highlightcolor = 'red', wrap = WORD, undo = True, yscrollcommand = RightScrollbar.set)
Body.bind('<Button-3>', lambda event: EntryPopupMenu(event, Body))
Body.bind('<Control-Key-a>', lambda event: BodySelectAll(event))
Body.bind('<Control-Key-A>', lambda event: BodySelectAll(event))
RightScrollbar.config(command = Body.yview)
Body.place(x = 14, y = 55)

root.title('MakPad')
root.state('zoomed') # launch full screen
root.mainloop()



