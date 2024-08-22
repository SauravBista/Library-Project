Library Management System

A simple library management system built with Flask and SQLAlchemy. This web application allows users to manage a collection of books, including adding new books, editing book ratings, and deleting books.
Features

    View Books: Displays a list of all books in the library.
    Add New Books: Allows users to add new books to the collection.
    Edit Book Ratings: Users can update the rating of a book.
    Delete Books: Remove books from the library.

Requirements

    Python 3.x
    Flask
    Flask-SQLAlchemy

Installation

    Clone the Repository

    bash

git clone https://github.com/yourusername/repository.git
cd repository

Create a Virtual Environment

bash

python -m venv venv

Activate the Virtual Environment

    On Windows:

    bash

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the Required Packages

bash

    pip install -r requirements.txt

    Configure the Database

    Ensure the database path in app.config["SQLALCHEMY_DATABASE_URI"] is correct. If needed, modify it to match your environment.

Running the Application

    Run the Flask Application

    bash

    python app.py

    Access the Application

    Open your browser and navigate to http://127.0.0.1:5000/ to view the application.

Application Structure

    app.py: Contains the main Flask application and route definitions.
    templates/: Directory for HTML templates:
        index.html: Displays the list of books.
        add.html: Form for adding new books.
        edit_rating.html: Form for editing book ratings.
    requirements.txt: List of Python packages required for the project.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Feel free to submit issues or pull requests to improve the project.
Contact

For any questions or comments, please reach out to sauravbista10@gmail.com.
