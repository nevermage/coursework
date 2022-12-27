import paramiko
from tkinter import *
import tkinter.scrolledtext as tkscrolled

class FormHandler:
    def initForm(self):
        base = Tk()
        base.geometry('1000x800')
        base.title("Registration Form")

        labl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))
        labl_0.place(x=90, y=53)

        labl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
        labl_1.place(x=80, y=130)

        entry_1 = Entry(base)
        entry_1.place(x=240, y=130)

        labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
        labl_2.place(x=68, y=180)

        entry_02 = Entry(base)
        entry_02.place(x=240, y=180)

        labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
        labl_3.place(x=70, y=230)

        labl_4 = Label(base, text="Age:", width=20, font=("bold", 10))
        labl_4.place(x=70, y=280)

        entry_02 = Entry(base)
        entry_02.place(x=240, y=280)

        Button(base, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)
        # it will be used for displaying the registration form onto the window

        # fileText = Text(base, width=50, state=DISABLED, font=("bold", 12))
        fileText = tkscrolled.ScrolledText(base, width=90, wrap='word', font=("bold", 12))
        fileText.configure(state='normal')



        # @todo move to .env
        host = '0.0.0.0'
        user = 'root'
        secret = 'secret'
        port = 20022
        logPath = '/var/www/logs/error.log'

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=user, password=secret, port=port)
        sftp_client = client.open_sftp()
        file = sftp_client.open(logPath)
        lines = file.readlines()

        for line in lines:
            fileText.insert('end', line.strip() + '\n')
        client.close()



        fileText.configure(state='disabled')
        fileText.place(x=50, y=300)

        base.mainloop()
