Booksy: A Flask Application
Introduction
Booksy is a Flask-based web application that displays a list of ten books fetched from the Open Library API. This simple application is designed to demonstrate basic Flask functionality, including routing, template rendering, and making API calls.

Features
Displays a list of the first ten books based on a predefined query from the Open Library API.
Each book title is clickable and leads to a detailed view of the book.
Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.6 or higher
pip (Python package installer)
Git (Version control system)
Installation
Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Atinos31/Booksy.git
cd Booksy
Set Up a Virtual Environment
Setting up a virtual environment is recommended to manage dependencies:

bash
Copy code
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment on macOS/Linux
# For Windows use: venv\Scripts\activate
Install Dependencies
Install all required packages using pip:

bash
Copy code
pip install -r requirements.txt
Running the Application
To run the application, execute:

bash
Copy code
python app.py
This command starts a local server. You can access the application by navigating to http://localhost:5000 in your web browser.

Application Structure
app.py: The main Python file with Flask routes.
templates/: This directory contains HTML files for the application.
index.html: Displays the list of books.
details.html: Displays detailed information about a specific book.
Usage
Upon launching the application, you will see a list of books on the homepage. Each book's title is a hyperlink. Clicking on a title will take you to a page displaying more detailed information about the book.

Additional Information
For more details about the APIs used and the Flask framework, you can refer to:

Open Library API Documentation
Flask Documentation
Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file in the repository for more information.

