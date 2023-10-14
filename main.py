import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import imaplib
import email
from email.header import decode_header
import html2text
# import uvicorn  # Import uvicorn


model_name = './model/'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('./model/')
# df = pd.read_csv("email_data.csv")

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000/"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load your trained BERT model and tokenizer



# Load the email dataset from email.csv
# df = pd.read_csv("email_data.csv")

@app.get("/")
# Create empty lists to store classified results
def email_send():
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
    
    ham_messages = []
    spam_messages = []
    
    def classify_store(message):
    # Tokenize the message
        encoded_message = tokenizer([message], padding=True, truncation=True, max_length=128, return_tensors='tf')
        # Ensure that the input tensors have the correct shape
        input_ids = encoded_message['input_ids']
        attention_mask = encoded_message['attention_mask']
        token_type_ids = encoded_message['token_type_ids']
        # Make predictions
        pred_label = model.predict({'input_ids': input_ids, 'attention_mask': attention_mask, 'token_type_ids': token_type_ids})
        print(pred_label.logits)
        if pred_label.logits[0][0] > pred_label.logits[0][1]:
            ham_messages.append({"Subject": generate_random_subject(), "Message": message})
        else:
            spam_messages.append({"Subject": generate_random_subject(), "Message": message})


    def generate_random_subject():
        letters = string.ascii_letters
        subject = ''.join(random.choice(letters) for _ in range(10))
        return subject
    for message in df["Message"]:
        if not isinstance(message, str):
            print(message)
            message = str(message)
        # print(type(message))
        classify_store(str(message))
        
    
    ham_df = pd.DataFrame(ham_messages)
    spam_df = pd.DataFrame(spam_messages)
    print(f"Total ham messages: {len(ham_messages)}")
    print(f"Total spam messages: {len(spam_messages)}")
    
    print("Calculating TF-IDF scores...")
    df1= pd.read_csv("ham_messages.csv")
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(df1["Message"])
    max_tfidf_scores = tfidf_matrix.max(axis=1).toarray().flatten()
    print(max_tfidf_scores)
    df1["Priority"] = max_tfidf_scores
    print(df1.head())
    df1 = df1.sort_values(by="Priority", ascending=False)
    df1 = df1.reset_index(drop=True)
    high_priority_emails = df1[df1["Priority"] > 0.7]
    medium_priority_emails = df1[(df1["Priority"] >= 0.4) & (df1["Priority"] <= 0.7)]
    low_priority_emails = df1[df1["Priority"] < 0.4]
    print(f"Total high priority emails: {len(high_priority_emails)}")
    print(f"Total medium priority emails: {len(medium_priority_emails)}")
    print(f"Total low priority emails: {len(low_priority_emails)}")
    print(low_priority_emails["Priority"])
    
    return high_priority_emails, medium_priority_emails, low_priority_emails,spam_df

email_send()