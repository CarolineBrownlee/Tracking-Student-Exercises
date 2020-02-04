# You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# The collection of exercises that the student is currently working on
from NSSPerson import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercises = list()  

    def list_assignments(self):
        for exercise in self.exercises:
            print(exercise.name)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'