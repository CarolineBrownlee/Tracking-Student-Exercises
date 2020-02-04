import sqlite3

class Student_Exercise_Reports():

    #  """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/caroline/workspace/python/Tracking_Student_Exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.student_id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from Student s
            join Cohort c on s.cohort_id = c.cohort_id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                # The index numbers correspond to the position of values in the query result
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = Student_Exercise_Reports()
reports.all_students()