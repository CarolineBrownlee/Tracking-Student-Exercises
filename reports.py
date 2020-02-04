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

            # When you instruct the sqlite3 package to fetchall(), it takes your SQL string and walks over to the database and executes it. It then takes all of the rows that the database generates, and creates a tuple out of each one. It then puts all of those tuples into a list.

            # TUPLE is a collection which is ordered and unchangeable. Allows duplicate members. Parenthesis. (W3 Schools)

            # LIST is a collection which is ordered and changeable. Allows duplicate members. Brackets. (W3 Schools)

            all_students = db_cursor.fetchall()

            for student in all_students:
                # The index numbers correspond to the position of values in the SQL string above
                print(f'{student[1]} {student[2]} is in {student[5]}')

reports = Student_Exercise_Reports()
reports.all_students()