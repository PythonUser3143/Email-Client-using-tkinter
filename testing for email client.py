from tkinter import *
import tkinter as tk
from email.message import EmailMessage
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

window=Tk()
window.title('Email Client')
window.geometry('450x380')
window.iconbitmap('D:\PYTHON\IMAGES\icon_for_email_clien_Jy16u.ico')

label5=Label(window,text='Receiver\'s Email Address')
textbox4=Text(window,width=50,height=1,bg='light grey')
textbox2=Text(window,width=50,height=10,bg='light grey')
label2=Label(window,text='Message')
textbox1=Text(window,width=50,height=1,bg='light grey')
textbox3=Text(window,width=50,height=1,bg='light grey')
label4=Label(window,text='Directory of File Attachment')
label1=Label(window,text='Subject')
label3=Label(window,text='')

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "school.homework.automated.email@gmail.com"
    msg['from'] = user
    password = "stereohi$3"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.ehlo()

    server.quit()

if __name__ == '__main__':
    def Send():
        gd = textbox3.get('1.0','end-1c')
        dialog = textbox2.get('1.0','end-1c')
        subject = textbox1.get('1.0','end-1c')
        body = dialog
        toto = textbox4.get('1.0', 'end-1c')
        try:
            fromaddr = "school.homework.automated.email@gmail.com"
            toaddr = toto

            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = subject
            body = dialog

            msg.attach(MIMEText(body, 'plain'))

            filename = "Homework Attachment"
            attachment = open(gd, "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.ehlo()
            s.login(fromaddr, "stereohi$3")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            Reset()

            s.quit()
        except:
            email_alert(subject, dialog, toto)


def Reset():
    textbox1.delete('1.0', 'end-1c')
    textbox2.delete('1.0', 'end-1c')
    textbox3.delete('1.0', 'end-1c')
    textbox4.delete('1.0', 'end-1c')

label5.pack()
textbox4.pack()
label1.pack()
textbox1.pack()
label4.pack()
textbox3.pack()
label2.pack()
textbox2.pack()
all_commands = lambda: [Send(), Reset()]
button1=Button(window,text='Send Email',width=15,height=1, command=all_commands)
button1.pack(padx=22, side='left', anchor='e', expand=True)
button3=Button(window,text='Exit',width=15,height=1, command=window.destroy)
button3.pack(padx=24, side='right', anchor='w', expand=True)

window.mainloop()
