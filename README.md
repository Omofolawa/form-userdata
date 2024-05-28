# form-userdata
### Project Description: Web Form with Excel Backend Using Python

Overview
This project is a simple web form designed to collect user information, including first name, last name, password (hashed for security), and email address. The form data is stored in an Excel file, functioning as the backend database. Python is used for the server-side logic, handling form submissions and data processing.

This solution is ideal for small to medium-sized organizations for managing employee databases and more. It is both user-friendly and cost-effective.

Features
- User-Friendly Form: A clean and responsive web form built using HTML, CSS, and Bootstrap for a modern and accessible user interface.
- Secure Password Handling: Passwords are hashed using the `hashlib` library in Python to ensure user data security.
- Excel Backend: Data is stored in an Excel file, making it easy to manage and review collected information without needing a complex database setup.
- Python Server-Side Logic: The backend is powered by Python, utilizing the Flask framework for handling HTTP requests and openpyxl for Excel file operations.

Technologies Used
- Frontend: HTML, CSS, Bootstrap
- Backend: Python, Flask, openpyxl, hashlib
- Data Storage: Excel file

Key Components
1. HTML Form: Collects user information with fields for first name, last name, password, and email. All fields are required to ensure complete data collection.
2. CSS Styling: External stylesheet for a consistent and visually appealing design, including a dark-themed background, colored form container, and a styled footer with links to email and GitHub.
3. Python Script: Handles form submissions, hashes passwords, and saves data to an Excel file.

How It Works
1. User Submission: Users fill out the form and submit their information.
2. Data Processing: The Python server receives the data, hashes the password, and appends the information to an Excel file.
3. Data Storage: The Excel file acts as a simple, yet effective database to store and manage user data.

Project Structure
- index.html: The HTML file containing the form structure and linked CSS for styling.
- styles.css: The CSS file providing styling rules for the form and other elements.
- app.py: The Python script using Flask to handle HTTP requests and openpyxl to interact with the Excel file.

This project provides a straightforward and secure way to collect and manage user data using a web form, with minimal setup and ease of use provided by Python and Excel integration. This solution can easily be used for small to medium based organizations for employee database management and so on.
