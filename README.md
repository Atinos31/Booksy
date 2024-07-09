# Booksy
My Book App
Description
My Book App is a simple Flask web application designed to display a list of books fetched from the Open Library API. Users can view basic details about the books, including titles, authors, and publication years on the home page. Each book title is a hyperlink that leads to a more detailed page where further information about the book is displayed.

Features
Display a list of the first 10 books based on a predefined query.
Individual book details page with more extensive information.
Installation
Prerequisites
Python 3.x
pip
Flask
requests
Setup and Activation
To get started, clone this repository and set up a virtual environment:

bash
Copy code
git clone <repository-url>
cd mybookapp
python3 -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows
Install Dependencies
Install the required Python packages using pip:

bash
Copy code
pip install flask requests
Usage
To run the application, execute the following command in the terminal:

bash
Copy code
python app.py
Navigate to http://localhost:5000 in your web browser to view the app.

Project Structure
app.py: Main application file where routes and API interactions are defined.
templates/: Folder containing HTML templates for the application views.
index.html: Home page template displaying the list of books.
details.html: Template for individual book details.
Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

