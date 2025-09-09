from email.mime.text import MIMEText
import smtplib

def send_test_email():
    smtp_server="smtp.gmail.com"
    port=587  
    sender="ishah332006@gmail.com"
    receiver="sarikashah2019@gmail.com"
    password="cyvt dkgn bzuv kynk" 

    # Composing the email message
    message=MIMEText("Hi! Isha here")
    message["Subject"]="Test Email"
    message["From"]=sender
    message["To"]=receiver

    try:
        # Connect to the SMTP server and secure the connection
        server=smtplib.SMTP(smtp_server, port)
        server.starttls()

        # Login to the email account
        server.login(sender, password)
        
        # Send the email
        server.sendmail(sender, receiver, message.as_string())
        
        print("Email sent successfully!")
        
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the connection to the SMTP server
        server.quit()

send_test_email()
