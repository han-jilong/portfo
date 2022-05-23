from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
    with open('database.txt','a') as database:
        email = data['mail']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_csv_file(data):
    with open('database.csv','a') as database:
        email = data['mail']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv_file(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to db'
    else:
        return 'something wrong'