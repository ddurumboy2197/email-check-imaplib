import imaplib
import email
from email.parser import BytesParser

# Gmail serveri uchun ma'lumotlar
server = 'imap.gmail.com'
port = 993
username = 'your_email@gmail.com'
password = 'your_password'

# Imap server bilan ulanish
mail = imaplib.IMAP4_SSL(server)
mail.login(username, password)

# Oxirgi 5 ta xatni o'qish uchun
mail.select('inbox')
status, messages = mail.search(None, 'ALL')
ids = messages[0].split()
ids = ids[-5:]

# Oxirgi 5 ta xatning sarlavhalari
for id in ids:
    status, data = mail.fetch(id, '(RFC822)')
    raw_email = data[0][1]
    email_message = BytesParser().parsebytes(raw_email)
    print(email_message['Subject'])
```

Kodni ishlatish uchun, `your_email@gmail.com` va `your_password` o'rniga o'zingizning Gmail emaili va parolini kiritishingiz kerak.
