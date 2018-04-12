from tkinter import *
import smtplib,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import font



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


	try:
	        attachments = open(c,'rb')
	        part = MIMEBase('application','octet-stream')
	        part.set_payload((attachments).read())
	        encoders.encode_base64(part)
	        part.add_header('Content-Disposition',"attachment;filename=%s" %d)
	        msg.attach(part)
	except:
	        pass
	try:
		username = a
		obj = smtplib.SMTP('smtp.gmail.com',587)
		obj.starttls()
		obj.login(username,p)
		obj.sendmail(a,b,msg.as_string())
		obj.quit()

		i.set("Email sent successfully")
	except:
		i.set("Mail Not send!!")
    
    

i = StringVar()
sender = StringVar()
password = StringVar()
receiver = StringVar()
subject = StringVar()
message = StringVar()
attachment = StringVar()
filename1 = StringVar()




font_label = font.Font(family="Fixedsys", size=16)
Label(frame,text="SENDER`s Email",fg= "green",font=font_label).grid(column = 0,row =1)
Label(frame,text="PASSWORD",fg= "green",font=font_label).grid(column = 0,row =5)
Label(frame,text="RECIEVER`s Email",fg= "green",font=font_label).grid(column = 0,row =7)
Label(frame,text="SUBJECT",fg= "green",font=font_label).grid(column =0,row =9)
Label(frame,text="MESSAGE",fg= "green",font=font_label).grid(column = 0,row =11)
Label(frame,textvariable = i,fg= "green",bg="orange",font=font_label).grid(column = 6,row =19)
Label(frame,text="FILENAME",fg= "green",font=font_label).grid(column = 0,row =13)
Label(frame,text="ATTACHMENTS",fg= "green",font=font_label).grid(column = 0,row =15)


font_entry = font.Font(family="Arial", size=16)
Entry(frame,textvariable = sender,fg= "red",font=font_entry).grid(column=6,row=1)#sender
Entry(frame,textvariable = password,fg= "red",show="*",font=font_entry).grid(column=6,row=5)#password
Entry(frame,textvariable = receiver,fg= "red",font=font_entry).grid(column=6,row=7)#reciever
Entry(frame,textvariable = subject,fg= "red",font=font_entry).grid(column=6,row=9)#subject
Entry(frame,textvariable = message,fg= "red",font=font_entry).grid(column=6,row=11)#message
Entry(frame,textvariable = attachment,fg= "red",font=font_entry).grid(column=6,row=15)#attachments
Entry(frame,textvariable = filename1,fg= "red",font=font_entry).grid(column=6,row=13)


Button(frame,text = "Send",command = emailsend,font=font_entry).grid(column=6,row=17)






#root.resizable(0,0)
root.mainloop()
