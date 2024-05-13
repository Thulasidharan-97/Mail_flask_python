from flask import *

from flask_mail import Mail,Message
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "vishalshankar105@gmail.com" #own mail id
app.config['MAIL_PASSWORD'] = 'xwgj ykmj hjdx csix ' #app password in mail
app.config['MAIL_USE_TLS'] = True
mail = Mail(app)
@app.route('/')
def index():
    msg = Message('subject',sender='vishalshankar105@gmail.com',recipients=['udhay060402@gmail.com'])
    msg.body = 'Hello Madam, Hope everything is going well and good.i am eagerly waiting to work for our company to show my skills and we can grow togeather.....'
    mail.send(msg)
    return "Mail sent Sucessfully Kindly check it in your Inbox....."
if __name__ == '__main__':
    app.run(debug=True)


