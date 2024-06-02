import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def make_otp():
    otp = ''.join([random.choice('1234567890') for _ in range(6)])
    return otp

def send_otp(receiver_email):
    # Email account credentials
    sender_email = "spallapu2@gitam.in"
    sender_password = "atwv gywk wioa pwit"  # Use an app-specific password if using Gmail or similar
    otp = make_otp()
    # Email content
    subject = f"Your OTP is : {otp} "
    body = f"The OTP for your login is : {otp}"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"  # Example for Gmail, change as needed
    smtp_port = 587  # Standard port for TLS

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
            return otp
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None

if __name__ == '__main__':
    send_otp("example@gmail.com")