# You must define a type for representing an instructor in code.

# First name
# Last name
# Slack handle
# The instructor's cohort
# The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
# A method to assign an exercise to a student
from NSSPerson import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def assign_exercise(self, student, new_exercise):
        student.exercises.append(new_exercise)