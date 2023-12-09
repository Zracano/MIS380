from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    selection = request.form['selection']
    valid_tables = ["Movie", "Employee", "Genre", "Theater_Rooms", "Location", "Attendee", "Seat", "Actor", "Directors",
                    "Job_Post"]

    # Check if selection is valid
    if selection not in valid_tables:
        return "Invalid selection"

    query_mappings = {
        "Movie": "SELECT * FROM Movie",
        "Employee": "SELECT * FROM Employee",
        "Genre": "SELECT * FROM Genre",
        "Theater_Rooms": "SELECT * FROM Theater_Rooms",
        "Location": "SELECT * FROM Location",
        "Seat": "SELECT * FROM Seat",
        "Attendee": "SELECT * FROM Attendee",
        "Actor": "SELECT * FROM Actor",
        "Directors": "SELECT * FROM Directors",
        "Job_Post": "SELECT * FROM Job_Post"
    }
    # Get the query for the selected table or default to Movie
    query = query_mappings.get(selection, "SELECT * FROM Movie")

    conn = sqlite3.connect('MIS380.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    conn.close()

    return render_template('results.html', result=result, column_names=column_names, table_name=selection)


@app.route('/reports')
def reports():
    conn = sqlite3.connect('MIS380.db')
    cursor = conn.cursor()

    # Report 1: Average Duration of All Movies
    cursor.execute("SELECT AVG(duration) FROM Movie")
    avg_movie_duration = cursor.fetchone()[0]

    # Report 2: Total Number of Seats Available in Each Theater Room
    cursor.execute(
        "SELECT RoomNumber, SUM(Capacity) FROM Theater_Rooms GROUP BY RoomNumber")
    total_seats_each_room = cursor.fetchall()

    # Report 3: Movies with the Word “The”
    cursor.execute("SELECT title FROM Movie WHERE title LIKE '%The%'")
    movies_with_the = cursor.fetchall()

    # Report 4: Sci-Fi or Romance Movies
    # Assuming 'genre' is a column in Movie table
    cursor.execute("SELECT * FROM Movie WHERE GenreID IN (305,302,301,304)")
    scifi_romance_movies = cursor.fetchall()

    # Report 5: Movies Released Between Certain Dates
    # Replace 'start_date' and 'end_date' with actual dates
    cursor.execute("SELECT * FROM Movie WHERE ReleaseDate BETWEEN '2000-01-01' AND '2020-12-31'")
    movies_in_date_range = cursor.fetchall()

    # Report 6: Action Movies or Movies Longer than 150 Minutes
    cursor.execute("SELECT * FROM Movie WHERE GenreID = 2 OR duration > 150")
    action_or_long_movies = cursor.fetchall()

    # Report 7: Employees with Salary Greater than 70k
    # Assuming 'salary' is a column in Employee table
    cursor.execute("SELECT * FROM Employee WHERE AnnualSalary > 70000")
    high_salary_employees = cursor.fetchall()

    # Report 9: Genres with More than One Movie
    cursor.execute("SELECT GenreID, COUNT(*) AS MovieCount FROM Movie GROUP BY GenreID HAVING COUNT(*) > 1")
    genres_with_multiple_movies = cursor.fetchall()

    # Report 10: Movies Longer Than the Average Duration
    cursor.execute("SELECT * FROM Movie WHERE Duration > (SELECT AVG(Duration) FROM Movie)")
    longer_than_average_movies = cursor.fetchall()

    # Report 11: Longest Movies
    cursor.execute("SELECT * FROM Movie ORDER BY Duration DESC LIMIT 1")
    longest_movies = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Pass the results to the reports.html template
    return render_template('reports.html',
                           avg_movie_duration=avg_movie_duration,
                           total_seats_each_room=total_seats_each_room,
                           movies_with_the=movies_with_the,
                           scifi_romance_movies=scifi_romance_movies,
                           movies_in_date_range=movies_in_date_range,
                           action_or_long_movies=action_or_long_movies,
                           high_salary_employees=high_salary_employees,
                           genres_with_multiple_movies=genres_with_multiple_movies,
                           longer_than_average_movies=longer_than_average_movies,
                           longest_movies=longest_movies
                           )


if __name__ == '__main__':
    app.run(debug=True)
