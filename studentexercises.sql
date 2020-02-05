--Use the INSERT INTO SQL statement to create...
--3 cohorts
--5 exercises
--3 instructors
--7 students (don't put all students in the same cohort)
--Assign 2 exercises to each student

--example
-- INSERT INTO Affiliation VALUES (null, 'Justice League');
-- INSERT INTO Affiliation VALUES (null, 'X-Men');
-- INSERT INTO Superhero
--     SELECT null, 'Super Dude', 'M', 'Bubba Farlo', Affiliation_Id
--     FROM Affiliation
--     WHERE Name = 'Justice League';
-- SELECT * FROM Affiliation;

INSERT INTO Cohort (name)
VALUES ('36');

INSERT INTO Cohort (name)
VALUES ('34');

INSERT INTO Cohort (name)
VALUES ('35');

INSERT INTO Exercises (name, language)
VALUES ('Intro to React', 'React');

INSERT INTO Exercises (name, language)
VALUES ('Intro to Python', 'Python');

INSERT INTO Exercises (name, language)
VALUES ('Intro to C#', 'C#');

INSERT INTO Exercises (name, language)
VALUES ('Intro to JavaScript', 'JavaScript');

INSERT INTO Exercises (name, language)
VALUES ('How to Survive a Bootcamp', 'English');

INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id)
VALUES ('James', 'Smith', '@James', 1);

INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id)
VALUES ('John', 'Long', '@john', 2),
	('Joseph', 'Brown', '@joseph', 3);

INSERT INTO Instructor (first_name, last_name, slack_handle, cohort_id)
VALUES ('Georgia', 'Lane', '@georgia', 3),
	('Lelia', 'Grant', '@lelia', 3);

INSERT INTO Student (first_name, last_name, slack_handle, cohort_id)
VALUES ('Jane', 'Brownlee', '@jane', 2),
('Annie', 'Lee', '@anne', 1),
('Sam', 'Grant', '@sam', 3),
('James', 'Sacrey', '@james', 1),
('Mary', 'Rose', '@mary', 3),
('Jorge', 'Villalobos', '@jorge', 2),
('Russell', 'Kincade', '@russell', 2);

INSERT INTO Student_Exercises (student_id, exercises_id)
VALUES (1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 1),
(4, 1),
(4, 2),
(5, 3),
(5, 4),
(6, 5),
(6, 1),
(7, 2),
(7, 3);