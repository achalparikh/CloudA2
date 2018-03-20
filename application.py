import smtplib
from flask import Flask, render_template, request

def sendEmail(subject, msg, email): 
	try: 
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo
		server.starttls()
		server.login("achal.parikh13@gmail.com", "achubinu")
		message = 'Subject:{}\n\n{}'.format(subject, msg)
		server.sendmail(email, email, message)
		server.quit()
		return ("Success Sent")
	except: 
		return ("Failed to send Email")

application = app = Flask (__name__)

@app.route("/")
def home(): 
	return render_template("form.html")

@app.route("/send", methods=['POST'])
def send():
	email = request.form['email']
	subject1 = "Cloud Assignment Demo App"
	msg1 = "How are you today?"
	
	return sendEmail(subject1, msg1, email)
	

if __name__ == "__main__":
	app.run(debug=True)

