Booksy: A Flask Application
Introduction
Booksy is a Flask-based web application that displays a list of ten books fetched from the Open Library API. This simple application is designed to show basic Flask functionality, including routing, template rendering, and making API calls. Check out the live site: Booksy Live.

Features
List Display: Shows a list of the first ten books based on a predefined query from the Open Library API.
Book Details: Each book title is clickable and leads to a detailed view of the book.
Prerequisites
Before you begin, make sure you have the following installed on your system:

Python 3.6 or higher
pip (Python package installer)
Git (Version control system)
Heroku CLI (for deploying the application)
Getting Started
Clone the Repository
To get started with Booksy, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Atinos31/Booksy.git
cd Booksy
Set Up a Virtual Environment
Using a virtual environment is recommended to manage the project's dependencies separately:

bash
Copy code
# Create a virtual environment
python3 -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # On macOS and Linux
venv\Scripts\activate     # On Windows
Install Dependencies
Install all the required packages using pip:

bash
Copy code
pip install -r requirements.txt
Running the Application Locally
To run the application on your local machine, execute:

bash
Copy code
python app.py
This will start a local server. You can access the application by navigating to http://localhost:5000 in your web browser.

Deploying to Heroku
Prepare the App for Deployment
Make sure your app is ready for Heroku deployment by confirming the following files are set up:

Procfile: Contains the command to run your app. Should be in the root directory:

makefile
Copy code
web: gunicorn app:app
requirements.txt: Lists all your app’s dependencies.

runtime.txt (optional): Specifies the Python version to use.

Deploying
With Heroku CLI installed, log in to your Heroku account and create a new app:

bash
Copy code
heroku login
heroku create your-app-name
Deploy your application by pushing it to Heroku:

bash
Copy code
git push heroku master
Once deployed, you can open your application:

bash
Copy code
heroku open
Additional Resources
Open Library API Documentation
Flask Documentation
Heroku Python Support
Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file in the repository for more information.



