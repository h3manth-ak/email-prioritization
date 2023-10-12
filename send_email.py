# import csv
# import smtplib
# import email.message

# # Open the CSV file and read its contents into a list
# with open('path/to/csv/file.csv', 'r') as file:
#     reader = csv.reader(file)
#     data = list(reader)

# # Loop through the list and check for a match with the target email address
# for row in data:
#     if row[0] == 'openwork98@gmail.com':
#         # Extract the message and subject from the CSV file
#         message = row[1]
#         subject = row[2]
        
#         # Create an email message
#         email_message = email.message.EmailMessage()
#         email_message['To'] = 'openwork98@gmail.com'
#         email_message['From'] = 'myphoto049@gmail.com'
#         email_message['Subject'] = subject
#         email_message.set_content(message)
        
#         # Connect to an SMTP server and send the email message
#         with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#             smtp.starttls()
#             smtp.login('myphoto049@gmail.com', 'gjqr pctp pgpe iysb')
#             smtp.send_message(email_message)
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read the spam.csv file into a DataFrame
df = pd.read_csv("spam.csv")

# Email configuration
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
smtp_port = 587  # Replace with your SMTP server port (587 is for TLS)
sender_email = "myphoto049@gmail.com"  # Replace with your email address
sender_password = "gjqr pctp pgpe iysb"  # Replace with your email password
receiver_email = "openwork98@gmail.com"  # Replace with the recipient's email address
email_data = pd.read_csv('spam.csv')

# Connect to the SMTP server
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    print("Successfully connected to the SMTP server")
    for index, row in email_data.iterrows():
        category = row['Category']
        message = row['Message']

        subject = "Spam" if category == "spam" else "Ham"  # Use "Spam" or "Ham" as the subject

        # Construct the email message
        msg = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(sender_email, 'openwork98@gmail.com', msg)
        print(f"Email sent for category: {category}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    server.quit()
    print("Disconnected from the SMTP server")
