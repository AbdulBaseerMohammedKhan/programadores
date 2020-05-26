import smtplib
import os.path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def SendMail(message = 'hacked Hackathon Programadores'):
    email = 'ismailuzma72@gmail.com' # Your email
    password = 'Ismail*17' # Your email account password
    send_to_email = 'shahbaaz23khan@gmail.com' # Who you are sending the message to
    subject='File attachment'
      # The message in the email
    file_location='C:/Users/dell/Documents/RESIDENCE CERTIFICATE.pdf'

    msg=MIMEMultipart()
    msg['From']=email
    msg['To']=send_to_email
    msg['Subject']=subject

    msg.attach(MIMEText(message,'plain'))

    # filename=os.path.basename(file_location)
    # attachment=open(file_location,"rb")
    # part=MIMEBase('application','octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition',"attachment;filename=%s"%filename)

    # msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
    server.starttls() # Use TLS
    server.login(email, password)
    text=msg.as_string()
    server.sendmail(email, send_to_email , message) # Send the email
    server.quit() # Logout of the email server


import pickle
import pandas as pd
import tkinter as tk
from tkinter import filedialog, Text


# from  import MailSender
# **********************MailSendingStuff*************************************************

# *************************************************************************************************

def add():
    filename = 'finalized_model.sav'
    train = pd.read_csv(filedialog.askopenfilename(initialdir="/", title="Select .csv files",
                                                   filetypes=(("CSV FILES", "*.csv"), ("All Files", "*.*"))))

    train_copy = train.groupby('Patient_id').mean().fillna(train.mean())
    train_copy['SepsisLabel'][train_copy['SepsisLabel'] != 0] = 1
    x = train_copy.drop(['SepsisLabel'], axis=1)
    y = train_copy['SepsisLabel']

    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(x, y)
    print(result)
    print(y)
    #SendMail()
    # result = loaded_model.
    # print(result)
    l = tk.Tk()
    l.title("Predicted Score")
    l.geometry("500x500")
    l.configure(bg='azure')
    la = tk.Label(l, text=("Accuracy: "), bg='palegreen', fg='black')
    la.place(relx=0.5, rely=0.5, anchor='c')
    la1 = tk.Label(l, text=result, bg='palegreen', fg='black')
    la1.place(relx=0.6, rely=0.5, anchor='c')
    lb = tk.Label(l, text=(y), bg='palegreen', fg='black')
    lb.place(relx=0.5, rely=0.7, anchor='c')

    mailbox = tk.Entry(l, width=20)

    mailbox.place(relx=0.2, rely=0.2, anchor='c')
    sendToMail = str(mailbox.get())
    mailButton = tk.Button(l, text="Send Mail", command=SendMail(sendToMail))

    print(sendToMail)
    mailButton.place(relx=0.7, rely=0.2, anchor='c')

    l.mainloop()


root = tk.Tk()
root.title("SEPSIS DETECTION")
root.geometry("500x500")
root.configure(bg='bisque')
root.resizable(0, 0)


# root.iconbitmap(default='favicon.ico')
def sym():
    a = tk.Tk()
    a.title("SYMPTOMS")
    a.geometry("300x300")
    a.configure(bg='azure')
    w = tk.Label(a, text="THE SYMPTOMS OF SEPSIS ARE .........", bg='azure')
    w.place(anchor='nw')
    a.mainloop()


def gL():
    b = tk.Tk()
    b.title("GUIDELINES")
    b.geometry("300x300")
    b.configure(bg='azure')
    g = tk.Label(b, text="THE GUIDELINES TO AVOID SEPSIS ARE .........", bg='azure')
    g.place(anchor='nw')
    b.mainloop()


b = tk.Button(root, text="PREDICT", height=5, width=15, font=('cooperblack', 10, 'bold'), bg='MediumPurple3',
              fg='white', command=add)
b.place(relx=0.2, rely=0.5, anchor='c')
a = tk.Button(root, text="SYMPTOMS", height=5, width=15, font=('cooperblack', 10, 'bold'), bg='MediumPurple3',
              fg='white', command=sym)
a.place(relx=0.5, rely=0.5, anchor='c')
c = tk.Button(root, text="GUIDELINES", height=5, width=15, font=('cooperblack', 10, 'bold'), bg='MediumPurple3',
              fg='white', command=gL)
c.place(relx=0.8, rely=0.5, anchor='c')
d = tk.Label(root, text="Welcome to Sepsis Detection App", bg='bisque', fg='blue', font=('TimesNewRoman', 18, 'bold'))
d.place(relx=0.5, rely=0.1, anchor='c')
tk.mainloop()

