from flask import Flask, request, render_template
import pandas as pd
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    first_name = request.form['fname']
    last_name = request.form['lname']
    raw_password = request.form['password']
    email = request.form['email']

    # Hash the password
    hashed_password = hashlib.sha256(raw_password.encode()).hexdigest()

    # Create DataFrame with the form data
    df = pd.DataFrame({
        'First Name': [first_name],
        'Last Name': [last_name],
        'Password': [hashed_password],
        'Email': [email]
    })

    # Append DataFrame to Excel file
    file_path = 'form_data.xlsx'
    try:
        existing_data = pd.read_excel(file_path)
        updated_data = pd.concat([existing_data, df], ignore_index=True)
        updated_data.to_excel(file_path, index=False)
    except FileNotFoundError:
        df.to_excel(file_path, index=False)

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
