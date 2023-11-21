import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_emails_and_names, smtp_server, smtp_port, from_email, password):
    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the email account
        server.starttls()
        server.login(from_email, password)

        for to_email, name in to_emails_and_names:
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            body_with_name = body.replace("[name]", name)
            msg.attach(MIMEText(body_with_name, 'plain'))

            # Send the email
            server.sendmail(from_email, to_email, msg.as_string())

# Replace these values with your own
subject = "Video Editing Service"
body = """Dear [name], 

I have stumbled upon your channel and I wanted to say that I really like your content! 😄

I am Luka, a video editor with 3+ years of experience in long-form and short-form videos!

Here are some of my most recent edits: https://drive.google.com/drive/folders/1sO-6-KyckZ7_UrPB7y5DQpH3W7kLuuk9?usp=sharing

Also, I have helped many great YouTubers, including a channel called FitFrHome, and I helped him gain over 20,000 subscribers in less than two weeks! Here is the link to their channel: https://youtube.com/@FitFrHome?si=vszsdO1Qx4JwGRlm

With my editing skills, we can elevate the quality of your content, resulting in increased viewership and a stronger subscriber base. Also, you will have more time to produce better quality content, which will also help you grow!

I will give you one FREE short video edit (up to 60 seconds long), and then you can see if you are satisfied with my editing!

If you are looking forward to seeing what I can do with your content, reply to this email, and we can go from there! 😄

Warm regards,

Luka

Phone Number: +38267412466
Instagram: @dukicc.m
Discord: matijadukic
"""

# List of recipients with names
to_emails_and_names = [('bosfinesse@gmail.com', 'BoSFinesse'), ('features@bestofbristol.co', 'BestOfBristol'), ('bristol@milkbun.co.uk', 'MilkBun'), ('lvkeliu@gmail.com', 'Luke'), ('cestclau@gmail.com', 'Friend'), ('fakeifys@gmail.com', 'Jake'), ('sm6239@nyu.edu', 'Friend'), ('nathaniel1232@outlook.com', 'Nathaniel'), ('nightrider1178@hotmail.com', 'Night Rider'), ('zenithgarage@gmail.com', 'Zenith'), ('Motovlogsniagara@gmail.com', 'MotovlogsNiagara')]

smtp_server = "smtp.gmail.com"
smtp_port = 587

from_email = "YourEmail"
password = "app password"

# Send the email
send_email(subject, body, to_emails_and_names, smtp_server, smtp_port, from_email, password)
