# Team 7 Movie Database Flask Application

## Description

This Flask web application provides an interface to interact with the Team 7 Movie Database. Users can view various data sets, such as Movies, Employees, Genres, etc., and access detailed reports generated from the database.

## Requirements

- Python 3.x
- Flask
- SQLite3

## Setup and Installation

1. **Clone or Download the Repository:**
   - Clone the repository using:
     ```
     git clone https://github.com/Zracano/MIS380
     ```
   - Or download the repository as a ZIP file and extract it.

2. **Install Dependencies:**
   - Navigate to the project directory in your terminal or command prompt.
   - Ensure Python 3 is installed on your system. Check using `python --version` (or `python3 --version` on some systems).
   - Install Flask using pip:
     ```
     pip install Flask
     ```

3. **Set Up the Database:**
   - Ensure the SQLite database file (`MIS380.db`) is in the project directory.
   - Include any specific setup instructions for the database here.

4. **Running the Application:**
   - In the terminal, navigate to the project directory.
   - Run the application using:
     ```
     python main.py
     ```
   - The server should start and be accessible at `http://127.0.0.1:5000/`.

5. **Accessing the Application:**
   - Open a web browser and visit `http://127.0.0.1:5000/`.
   - Interact with the Team 7 Movie Database web application.

## Usage

- Use the dropdown menu on the homepage to select and view different data sets.
- Click on "View Reports" to access various database reports.
- Use the "Back to Home" button on the reports page to return to the main menu.
