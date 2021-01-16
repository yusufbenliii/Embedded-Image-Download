from bs4 import BeautifulSoup
from simplegmail import Gmail
import requests

gmail = Gmail()

messages = gmail.get_unread_inbox()


for message in messages:
    print("To: " + message.recipient)
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Date: " + message.date)
    print("Preview: " + message.snippet)

    print("Message Body: " + message.plain) 
msg = messages[0]

soup = BeautifulSoup(msg.html, 'html.parser')

imgs = soup.find_all('img')

urls = [img['src'] for img in imgs]



for i in range(1,len(urls)):
    url = urls[i]
    name = f"image{i}.png"
    res = requests.get(url)
    file = open(name, "wb")
    file.write(res.content)
