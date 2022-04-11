from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Error: the data was not saved'
    else:
        return 'Something went wrong'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{firstname},{lastname},{email},{subject},{message}\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname, lastname, email, subject, message])
