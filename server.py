from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def home(page_name=None):
    return render_template(page_name)


# post is saving info, get is getting info from server
@app.route('/submit_form', methods=['POST', 'GET'])
def submitting():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Try again.'


def write_to_textfile(data):
    with open('data.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(
            f'Email: {email}, Subject: {subject}, Message: {message}\n')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
