import os.path
import base64
import re
from email import message_from_bytes

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# If modifying these, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_last_email():
    creds = None

    # Load or create token.json
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Connect to Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Get the latest message
    results = service.users().messages().list(userId='me', maxResults=1, labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
        return

    msg_id = messages[0]['id']
    message = service.users().messages().get(userId='me', id=msg_id, format='full').execute()

    headers = message['payload']['headers']
    subject = sender = snippet = ""

    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        elif header['name'] == 'From':
            sender = header['value']

    snippet = message.get('snippet', '')

    print("\n📬 Last Email:")
    print("From   :", sender)
    print("Subject:", subject)
    print("Snippet:", snippet)

if __name__ == '__main__':
    get_last_email()
