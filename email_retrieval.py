import imaplib
import email
from email.header import decode_header
import html2text
import pandas as pd

# Email account settings
username = "openwork98@gmail.com"
password = "wrwd mqut ftqk ckth"
imap_server = "imap.gmail.com"

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)

# Select the mailbox you want to retrieve emails from (e.g., "inbox")
mailbox = "inbox"
mail.select(mailbox)

# Search for all emails in the selected mailbox
status, email_ids = mail.search(None, "ALL")
email_ids = email_ids[0].split()

# Initialize the HTML to text converter
html_converter = html2text.HTML2Text()
html_converter.ignore_links = True  # Ignore hyperlinks

# Create a list to store email data
email_data = []

# Iterate through email IDs and retrieve the email content
for email_id in email_ids:
    status, email_data_raw = mail.fetch(email_id, "(RFC822)")
    raw_email = email_data_raw[0][1]
    email_message = email.message_from_bytes(raw_email)
    
    # Extract email subject
    subject, encoding = decode_header(email_message["Subject"])[0]
    
    # Initialize an empty message variable
    message = ""

    # Process email parts (can include plain text, HTML, attachments, etc.)
    for part in email_message.walk():
        content_type = part.get_content_type()
        content_disposition = str(part.get("Content-Disposition"))
        
        if "attachment" not in content_disposition:
            # Check if the part has content
            if part.get_payload(decode=True) is not None:
                # Extract and decode the message body
                if content_type == "text/plain":
                    # Plain text content
                    body = part.get_payload(decode=True).decode()
                elif content_type == "text/html":
                    # HTML content (convert to plain text)
                    body = html_converter.handle(part.get_payload(decode=True).decode())
                else:
                    # Handle other content types as needed
                    body = "Content type not supported"
                message += body
    
    # Append subject and message to the list
    email_data.append([subject, message])
    
# Close the mailbox and log out
mail.close()
mail.logout()

# Create a Pandas DataFrame from the email data
df = pd.DataFrame(email_data, columns=["Subject", "Message"])
df.to_csv("email_data.csv")


# Display the DataFrame
print("completed")

