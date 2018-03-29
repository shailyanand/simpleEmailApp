from tkinter import *
import smtplib,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



root = Tk()
root.title("EMAIL_APP")

frame = Frame(root)
frame.grid(column = 10, row = 10)


def emailsend(*args):
	a=sender.get()
	b=receiver.get()
	p=password.get()
	d=filename1.get()
	c=attachment.get()
	
	
	msg = MIMEMultipart()
	msg["Subject"] = subject.get()

	body= message.get()
    #    txt = MIMEText(body,'plain')
	msg.attach(MIMEText(body,'plain'))
	attachments = open(c,'rb')
	part = MIMEBase('application','octet-stream')
	part.set_payload((attachments).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment;filename=%s" %d)
	msg.attach(part)

	
	username = a
	obj = smtplib.SMTP('smtp.gmail.com',587)
	obj.starttls()
	obj.login(username,p)
	obj.sendmail(a,b,msg.as_string())
	obj.quit()

	i.set("Email sent successfully")
   
    
    

i = StringVar()
sender = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
message = StringVar()
attachment = StringVar()
filename1 = StringVar()

Label(frame,text="SENDER`s Email",fg= "green").grid(column = 0,row =1)
Label(frame,text="PASSWORD",fg= "green").grid(column = 0,row =2)
Label(frame,text="RECIEVER`s Email",fg= "green").grid(column = 0,row =3)
Label(frame,text="SUBJECT",fg= "green").grid(column =0,row =4)
Label(frame,text="MESSAGE",fg= "green").grid(column = 0,row =5)
Label(frame,textvariable = i,fg= "green",bg="orange").grid(column = 2,row =8)
Label(frame,text="FILENAME",fg= "green").grid(column = 0,row =9)
Label(frame,text="ATTACHMENTS",fg= "green").grid(column = 0,row =10)

Entry(frame,textvariable = sender,fg= "red").grid(column=2,row=1)#sender
Entry(frame,textvariable = password,fg= "red",show="*").grid(column=2,row=2)#password
Entry(frame,textvariable = receiver,fg= "red").grid(column=2,row=3)#reciever
Entry(frame,textvariable = subject,fg= "red").grid(column=2,row=4)#subject
Entry(frame,textvariable = message,fg= "red").grid(column=1,row=6)#message
Entry(frame,textvariable = attachment,fg= "red").grid(column=2,row=10)#attachments
Entry(frame,textvariable = filename1,fg= "red").grid(column=2,row=9)

Button(frame,text = "Send",command = emailsend).grid(column=2,row=7)






#root.resizable(0,0)
root.mainloop()
