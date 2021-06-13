from app import app, mail
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_mail import Message
from app.forms import ContactForm
import boto3
from botocore.exceptions import ClientError


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/ceremony', methods=['GET'])
def ceremony():
    return render_template('ceremony.html', title='Ceremony')

@app.route('/party', methods=['GET'])
def party():
    return render_template('party.html', title='Party')

@app.route('/hotel', methods=['GET'])
def hotel():
    return render_template('hotel.html', title='Hotel')

@app.route('/around-town', methods=['GET'])
def around_town():
    return render_template('around_town.html', title='Things to do in Lexington')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    CHARSET = "UTF-8"

    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        # recipient = form.email.data
        SENDER = 'us@liz-and-meg.com'
        RECIPIENT = form.email.data
        AWS_REGION = "us-east-2"
        SUBJECT = f"A Message from {fname} {lname}!"
        BODY_TEXT = form.greeting.data
        # client = boto3.client('ses',region_name=AWS_REGION)
        # Try to send the email.
        try:
            #Provide the contents of the email.
            client = boto3.client('ses',region_name=AWS_REGION)
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
            
        return redirect(url_for('index'))
    return render_template('contact.html', title='Contact', form=form)


