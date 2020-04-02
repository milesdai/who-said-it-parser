import mailbox
import email.header
from datetime import datetime

def decode_subject(enc_subject):
    # MIME header decoding for some subject lines with Windows 1252 and utf-8 encodings
    text, encoding = email.header.decode_header(enc_subject)[0]
    return text.decode(encoding) if encoding else text

def parse_email(email):
    email_data = dict()
    email_data['Date'] = datetime.strptime(email.get('Date', 'ERROR'), '%a, %d %b %Y %H:%M:%S %z')
    email_data['From'] = email.get('From', 'ERROR')
    email_data['To'] = email.get('To', 'ERROR')
    email_data['Subject'] = decode_subject(email.get('Subject', 'ERROR'))
    return email_data

def parse(mailbox_name):
    mbox = mailbox.mbox(mailbox_name)
    emails = list()
    for email in mbox:
        emails.append(parse_email(email))
    return emails

def filter_email(emails, dtr_only=True, ignore_replies=True):
    def filter_func(e):
        return (not dtr_only or 'danger-third' in e['To']) and (not ignore_replies or 'RE: ' not in e['Subject'].upper())
    return list(filter(filter_func, emails))

def print_emails(emails):
    for e in emails:
        print('------------')
        print('From: {}'.format(e['From']))
        # print('To: {}'.format(e['To']))
        print('Date: {}'.format(e['Date']))
        print('Subject: {}'.format(e['Subject']))

    print('Total emails: {}'.format(len(emails)))
    
if __name__ == "__main__":
    emails = parse('whosaidit.mbox')
    emails = filter_email(emails)
    emails.sort(key=lambda e: e['Date'])
    print_emails(emails)