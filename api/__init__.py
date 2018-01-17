import os
from flask import Flask, g, render_template, request, jsonify
from flask_pymongo import PyMongo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/')
app = Flask(__name__, static_folder = '../static', template_folder=tmpl_dir,static_url_path='')
import smtplib
# CONFIGURATIONS
app.config.from_object('config')

# Add database
mongo = PyMongo(app)
@app.before_request
def before_request():

    # add this thing at some point
	# mongo.db.add_son_manipulator(UTF8Encoder())
	# mongo.db.add_son_manipulator(IDtoString())
	# mongo.db.add_son_manipulator(StringtoID())
	g.db = mongo.db

@app.route('/')
def root():
  return render_template('index.html')

#Route for resume download

@app.route('/download-resume')
def download_resume():
  return app.send_static_file('resume/vishwa_ML.pdf')

# Fix this on refering to Arun's code
@app.route('/feedback', methods=['POST'])
def feedback():
  name = request.form['contactName']
  email = request.form['contactEmail']
  subject = request.form['contactSubject']
  message = request.form['contactMessage']
  customer_message = {
    'name': name,
    'email': email,
    'subject': subject,
    'message': message,
  }
  # print(customer_message)
  g.db.feedback.insert_one(customer_message)



  emailAlerts(email,message)
  response = {
    'message': name+", Thanks for your interest and reaching out to us. Really appreciate it. We'll get back to you soon."}
  return jsonify(response), 200
  # return
def emailAlerts(email,message):
  contact_emails = app.config['CONTACT_EMAILS']

  msg = MIMEMultipart()
  msg['From'] = 'vishwanathavin@gmail.com'
  msg['Subject'] = "Message from VizAV"

  body = "Thanks for your interest and reaching out to me. Really appreciate it. I'll get back to you soon."
  msg.attach(MIMEText(body, 'plain'))
  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # ...send emails
  except:
    print('Something went wrong...')

  # for email in contact_emails:
  msg['To'] = email
  server.login("vishwanathavin@gmail.com", "*******")
  text = msg.as_string()
  server.sendmail("vishwanathavin@gmail.com", email, text)
  server.quit()

  return

# Get all the info from the database instead of hardcoding