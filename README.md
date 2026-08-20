# Flask Forms

A web application developed with **Python and Flask** to work with web forms, data validation, and HTML pages using Jinja2 templates.

## About the Project

This project was developed as part of my studies in web development with Flask.

The application uses an organized structure with:

* **Flask** for web application development
* **Flask-WTF** for form creation and validation
* **Jinja2** for HTML templates
* **Bootstrap** for page styling
* **Git and GitHub** for version control

## Features

* Web form display
* Form field validation
* User input processing
* Feedback messages
* Reusable HTML templates
* Custom `404` and `500` error pages
* Bootstrap-based interface

## Technologies

* Python
* Flask
* Flask-WTF
* Flask-Bootstrap
* Jinja2
* HTML5
* CSS3
* Git
* GitHub

## Project Structure

```text
flask-forms/
│
├── app.py
├── forms.py
├── routes.py
├── requirements.txt
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

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jhon0498/flask-forms.git
```

### 2. Navigate to the project directory

```bash
cd flask-forms
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Then open the following address in your browser:

```text
http://127.0.0.1:5000
```

## Purpose

The purpose of this project is to practice the main concepts of web application development using Flask, especially the creation, validation, and processing of web forms.

## Author

**Jhonatan Mendes Morão**

This project was developed for academic and learning purposes.
