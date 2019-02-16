# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail

api_key = "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"


def sendEmail(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key)
    from_email = Email("firewatch@fire.ca.gov")
    to_email = Email(to)
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return



