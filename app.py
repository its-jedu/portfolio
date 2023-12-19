from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        email_subject = request.form['email_subject']
        message = request.form['message']

        # Set up the email server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        email_address = 'olajide.adebanjo06@gmail.com'
        email_password = 'Jedu1122'
        server.login(email_address, email_password)

        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = 'olajide.adebanjo06@gmail.com'
        msg['Subject'] = f'New message from {full_name}'

        body = f"Name: {full_name}\nEmail: {email}\nPhone Number: {phone_number}\nSubject: {email_subject}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(email_address, 'olajide.adebanjo06@gmail.com', msg.as_string())
        server.quit()

        success_message = "Message sent successfully!"
        return f'<script>alert("{success_message}"); window.location.replace("/");</script>'

    except Exception as e:
        error_message = "Error occurred while sending the message. Please try again later."
        print(str(e))
        return f'<script>alert("{error_message}"); window.location.replace("/");</script>'


if __name__ == '__main__':
    app.run(debug=True)
