Booksy: A Flask Application
Introduction
Booksy is a Flask-based web application that displays a list of ten books fetched from the Open Library API. This application demonstrates basic Flask functionality such as routing, template rendering, and making API calls. Visit the live site: https://booksy-e420566edb07.herokuapp.com/.

Features

List Display: Shows a list of the first ten books based on a predefined query from the Open Library API.
Book Details: Each book title is clickable and leads to a detailed view of the book.
Prerequisites
Ensure you have the following installed on your system before you begin:

Python 3.6 or higher

pip (Python package installer)

Git (Version control system)

Heroku CLI (for deploying the application)

# Getting Started
Clone the Repository
Clone the repository to your local machine to get started with Booksy:


git clone https://github.com/Atinos31/Booksy.git
cd Booksy
Set Up a Virtual Environment
It is recommended to use a virtual environment to manage the project's dependencies separately:


# Create a virtual environment
python3 -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate     # On Windows
Install Dependencies
Install all required packages using pip:

pip install -r requirements.txt
Running the Application Locally
Run the application on your local machine with the following command:


python app.py
This starts a local server. Access the application by navigating to http://localhost:5000 in your web browser.

Deploying to Heroku
Prepare the App for Deployment
Ensure your app is ready for Heroku deployment by confirming the presence of the following files:

Procfile: Contains the command to run your app, should be in the root directory:

web: gunicorn app:app
requirements.txt: Lists all your app’s dependencies.

runtime.txt (optional): Specifies the Python version to use.

Deploying
Deploy your application to Heroku with these steps:


heroku login
heroku create your-app-name
git push heroku master
Once deployed, open your application:


heroku open
Additional Resources
Open Library API Documentation
Flask Documentation
Heroku Python Support


Contributing
We welcome contributions! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file in the repository for more information



