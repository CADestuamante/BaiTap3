import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, receiver, subject, body, password):
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    
    message.attach(MIMEText(body,'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender, password) 
        text = message.as_string()
        server.sendmail(sender, receiver, text)
        print(f"Email đã được gửi đến{receiver}")
        
        server.quit()
    except Exception as e:
        print(f"Lỗi khi gửi email:{e}")

if __name__ == "__main__":
    sender_email = "123@gmail.com"
    app_password = "123"
    receiver_email = "321@gmail.com"
    subject = "thông báo tự động"
    body = " đây là email tự động được gửi từ Python. Không cần trả lời email này."
    
    send_email(sender_email, receiver_email, subject, body, app_password)