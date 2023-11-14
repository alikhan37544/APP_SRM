from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin",
    database="attendance_db"
)
cursor = db.cursor()

# Routes
@app.route('/')
def index():
    # Fetch attendance data from the database
    cursor.execute("SELECT * FROM attendance")
    attendance_data = cursor.fetchall()
    return render_template('index.html', attendance_data=attendance_data)

@app.route('/add_attendance', methods=['POST'])
def add_attendance():
    student_name = request.form['student_name']
    status = request.form['status']
    
    # Insert attendance data into the database
    cursor.execute("INSERT INTO attendance (student_name, date, status) VALUES (%s, CURDATE(), %s)", (student_name, status))
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
