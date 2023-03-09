from email.message import EmailMessage
import smtplib
import getpass
m=input("Mail server : ")
mail_server = smtplib.SMTP_SSL('smtp.'+m)
sender = str(input("Enter sender: "))
recipient = str(input("Enter recipient: "))
mail_pass = getpass.getpass("Password? ")
message = EmailMessage()
message['From'] = sender
message['To'] = recipient
message['Subject'] = str(input("Subject :"))
body = str(input("Body: "))
message.set_content(body)
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()
