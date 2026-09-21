# Form Email Notifications

A web application developed with **Python and Flask** that processes a web form, validates user input, and sends email notifications using the **Mailgun API**.

This project was developed as part of my studies in web development with Flask, with a focus on form handling, validation, environment variables, API integration, and email notifications.

## About the Project

The application allows a user to enter their username through a web form.

When the submitted user is found in the application's temporary user registry, the system:

1. Validates the submitted form.
2. Identifies the registered user.
3. Retrieves the user's registration information.
4. Builds an email notification.
5. Sends the email through the Mailgun API.
6. Displays a success or error message.

The project also includes error handling for invalid users, Mailgun authentication errors, and connection failures.

## Features

* Web form creation and validation
* User input processing
* Temporary user registration
* Email notification through Mailgun API
* Environment variable configuration
* Success and error feedback
* Flask templates using Jinja2
* Bootstrap integration
* Flask-Moment integration
* Custom `404` and `500` error pages
* Git and GitHub version control
* Deployment on PythonAnywhere

## Technologies

* **Python**
* **Flask**
* **Flask-WTF**
* **Flask-Bootstrap**
* **Flask-Moment**
* **Jinja2**
* **Requests**
* **Python-dotenv**
* **Mailgun API**
* **HTML5**
* **CSS3**
* **Git**
* **GitHub**
* **PythonAnywhere**

## Project Structure

```text
form-email-notifications/
│
├── app.py
├── forms.py
├── routes.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── favicon.ico
│
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── 404.html
    └── 500.html
```

## How It Works

The application starts in `app.py`, where Flask is initialized and the application configuration is loaded.

Environment variables are used for sensitive and configurable information such as the Mailgun API key, domain, and recipient email.

The routes are registered through:

```python
from routes import registrar_rotas

registrar_rotas(app)
```

The main route is responsible for processing the form submission.

After validation, the application checks whether the submitted username exists in the temporary user registry.

If the user exists, the application creates the email data and sends the request to Mailgun using the `requests` library.

## Mailgun Integration

The application uses the Mailgun API to send email notifications.

The request is authenticated using the Mailgun API key:

```python
auth=('api', mailgun_api_key)
```

The message is sent through the Mailgun endpoint:

```text
https://api.mailgun.net/v3/<MAILGUN_DOMAIN>/messages
```

The application checks the HTTP response returned by Mailgun.

A status code of `200` indicates that the request was successfully accepted.

## Environment Variables

The project uses a `.env` file for local configuration.

Example:

```env
FLASKY_ADMIN=your-email@example.com
FLASK_APP=app.py
MAILGUN_API_KEY=your-mailgun-api-key
MAILGUN_DOMAIN=your-mailgun-domain
MAILGUN_BASE_URL=https://api.mailgun.net
```

### Security

The `.env` file contains sensitive information and **must not be committed to GitHub**.

Make sure `.gitignore` contains:

```text
.env
```

Never publish your Mailgun API key in the repository.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jhon0498/form-email-notifications.git
```

### 2. Enter the project directory

```bash
cd form-email-notifications
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the vi
