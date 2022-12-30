from tkinter import *
import tkinter.scrolledtext as tkscrolled
import tkinter.messagebox as messagebox
from Services.FileService import FileService

class FormHandler:

    def __init__(self):
        base = Tk()
        width = 1000
        height = 800
        base.title("Remote file reader")
        screen_width = base.winfo_screenwidth()
        screen_height = base.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        base.geometry('%dx%d+%d+%d' % (width, height, x, y))
        Label(base, text="Remote host configuration", width=20, font=("bold", 16)).place(x=40, y=10)

        Label(base, text="Host", width=18, font=("bold", 10), anchor="e").place(x=0, y=43)

        hostInput = Entry(base)
        self.hostInput = hostInput
        hostInput.place(x=150, y=40)

        Label(base, text="User", width=18, font=("bold", 10), anchor="e").place(x=0, y=73)

        userInput = Entry(base)
        self.userInput = userInput
        userInput.place(x=150, y=70)

        Label(base, text="Password", width=18, font=("bold", 10), anchor="e").place(x=0, y=103)

        passwordInput = Entry(base, show="*")
        self.passwordInput = passwordInput
        passwordInput.place(x=150, y=100)

        Label(base, text="Port", width=18, font=("bold", 10), anchor="e").place(x=0, y=133)

        portInput = Entry(base)
        self.portInput = portInput
        portInput.place(x=150, y=130)

        Label(base, text="File (absolute path)", width=18, font=("bold", 10), anchor="e").place(x=0, y=163)

        filePathInput = Entry(base)
        self.filePathInput = filePathInput
        filePathInput.place(x=150, y=160)

        Button(
            base,
            text='Read file',
            width=20,
            command=self.seeFileContent
        ).place(x=80, y=200)

        fileText = tkscrolled.ScrolledText(base, width=90, wrap='word', font=("bold", 12))
        self.fileText = fileText
        fileText.configure(state='disabled')

        self.messagebox = messagebox
        base.resizable(False, False)
        base.mainloop()

        self.base = base

    def seeFileContent(self):
        host = self.hostInput.get()
        user = self.userInput.get()
        secret = self.passwordInput.get()
        port = self.portInput.get()
        filePath = self.filePathInput.get()

        try:
            response = FileService.getFileContentAsArray(host, user, secret, port, filePath)
            self.printFileContent(response)
        except Exception as e:
            self.cleanTextField()
            self.messagebox.showerror('Error', str(e))

    def printFileContent(self, lines):
        self.cleanTextField()
        fileText = self.fileText

        if type(lines) in (tuple, list):
            fileText.configure(state='normal')

            for line in lines:
                fileText.insert('end', line.strip() + '\n')

            fileText.configure(state='disabled')
            fileText.place(x=50, y=300)
        else:
            self.cleanTextField()
            self.messagebox.showerror('Error', 'Wrong data format')

        self.fileText = fileText

    def cleanTextField(self):
        self.fileText.configure(state='normal')
        self.fileText.delete('1.0', END)
        self.fileText.configure(state='disabled')