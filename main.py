# The learning objective of this exercise is to practice creating instances of custom types that you defined with class, establishing the relationships between them, and practicing basic data structures in Python.

# 1. Once you have defined all of your custom types, go to main.py, import the classes you need, ...

from exercise import Exercise
from student import Student
from cohort import Cohort
from instructor import Instructor

# ...and implement the following logic:

# 2. Create 4, or more, exercises.
Web_Design = Exercise("Web Design", "CSS")
Flexbox = Exercise("Flexbox", "CSS")
Intro_to_JavaScript = Exercise("Intro to JavaScript", "JavaScript")
Intro_to_React = Exercise("Intro to React", "React")
Intro_to_Python = Exercise("Intro to Python", "Python")

# 3. Create 3, or more, cohorts.
Cohort_34 = Cohort("Cohort_34")
Cohort_35 = Cohort("Cohort 35")
Cohort_36 = Cohort("Cohort 36")

# 4. Create 4, or more, students and assign them to one of the cohorts.
Caroline_Brownlee = Student("Caroline", "Brownlee", "@Caroline", 36)
Joseph_Brownlee = Student("Joseph", "Brownlee", "@Joseph", 36)
Molly_Brownlee = Student("Molly", "Brownlee", "@Molly", 34)
Scooby_Doo = Student("Scooby", "Doo", "@Scooby", 35)

Cohort_36.join_cohort(36, Caroline_Brownlee)
Cohort_36.join_cohort(36, Joseph_Brownlee)
Cohort_34.join_cohort(34, Molly_Brownlee)
Cohort_35.join_cohort(35, Scooby_Doo)

# 5. Create 3, or more, instructors and assign them to one of the cohorts.
Sponge_Bob_Squarepants = Instructor("Sponge Bob", "Squarepants", "@Spongebob", 34, "Wearing square pants.")
Dexter_Lab = Instructor("Dexter", "Lab", "@DextersLab", 36, "Building things in his laboratory.")
Bill_Gates = Instructor("Bill", "Gates", "@billGates", 35, "Mastermind of Microsoft")

Cohort_34.teach_cohort(Sponge_Bob_Squarepants)
Cohort_36.teach_cohort(Dexter_Lab)
Cohort_35.teach_cohort(Bill_Gates)

# 6. Have each instructor assign 2 exercises to each of the students.

