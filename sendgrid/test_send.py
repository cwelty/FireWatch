# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

api_key = "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"

sg = sendgrid.SendGridAPIClient(api_key)
from_email = Email("DonaldTrump@whitehouse.gov")
to_email = Email("cwelt001@ucr.edu")
subject = "Gg so far"
content = Content("text/plain", "Looking great so far, keep up the AWESSSSOOOMMEE work. - The Donald")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

print(response.status_code)
print(response.body)
print(response.headers)

