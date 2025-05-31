import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from crewai.tools import BaseTool
import base64
from datetime import date
from PyPDF2 import PdfReader
import pymupdf   # PyMuPDF

today = date.today()


def GetAttachments(service, user_id, msg_id):
    """Get and store attachment from Message with given id.

    :param service: Authorized Gmail API service instance.
    :param user_id: User's email address. The special value "me" can be used to indicate the authenticated user.
    :param msg_id: ID of Message containing attachment.
"""
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
        if part['filename']:
            if 'data' in part['body']:
                data = part['body']['data']
            else:
                att_id = part['body']['attachmentId']
                att = service.users().messages().attachments().get(userId=user_id, messageId=msg_id,id=att_id).execute()
                data = att['data']
            print('downloading.......')
            file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
            os.makedirs('Resumes', exist_ok=True)
            path = 'Resumes/'+part['filename']

            with open(path, 'wb') as f:
                f.write(file_data)


class GmailTool(BaseTool):
    name:str = "gmail_tool"
    
    description :str = "A tool to connect to Gmail and list emails."
    
    def _run(self) -> str:

        creds = None
        SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
        flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES)
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
                )
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            service = build("gmail", "v1", credentials=creds)
            results = service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])
            # if not labels:
            #     print("No labels found.")
            # else:
            #     print("Labels:")
            #     for label in labels:
            #         print(f"{label['name']} ({label['id']})")

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")

        # results = service.users().messages().list(userId='me', q = f'resume after:{today}').execute()
        results = service.users().messages().list(userId='me', q = f'resume after:2025-05-31').execute()

        messages = results.get("messages")
        for msg in messages:
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            try:
                GetAttachments(service,'me',msg['id'])
            except KeyError:
                pass
        files = os.listdir('Resumes')
        return "Gmail tool executed successfully, attachments downloaded if available. Check the 'Resumes' folder for files. file names: " + ", ".join(files) if files else "No resumes found in the inbox."
    
    
class Read_Pdf(BaseTool):
    name: str = "read_pdf"
    
    description: str = "A tool to read PDF files and extract text."

    
    def _run(self, file_path: str) -> str:
        try:
            text = self._extract_text_from_pdf(file_path)
            # with open(file_path, 'r',encoding='latin-1') as file:
            #     text = file.read()
            return text if text else "No text found in the PDF file."
        except Exception as e:
            return f"Error occurred while reading the PDF file: {str(e)}"
    
    def _extract_text_from_pdf(self, file_path: str) -> str:
        
        text=''
        # Open the PDF file
        doc = pymupdf.open(file_path)

        # Iterate through each page
        for page_num in range(len(doc)):
            page = doc[page_num]
            links = page.get_links()
            for link in links:
                if 'uri' in link:
                    text+=link['uri']

        pdf= PdfReader(file_path)
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        return text.strip() if text else "No text found in the PDF file."
        