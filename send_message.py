import os
from twilio.rest import Client
import datetime

client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

now = datetime.datetime.now().strftime("%A, %d %B %Y")

client.messages.create(
    from_=os.environ['TWILIO_FROM'],
    to=os.environ['TWILIO_TO'],
    body=f"Good morning, love ❤️ — hope you have a beautiful day! ({now})"
)
