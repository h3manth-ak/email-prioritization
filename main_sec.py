import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer

model_name = './model/'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('./model/')
df = pd.read_csv("email_data.csv")
def email_send():
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
    
    # return high_priority_emails, medium_priority_emails, low_priority_emails


email_send()
