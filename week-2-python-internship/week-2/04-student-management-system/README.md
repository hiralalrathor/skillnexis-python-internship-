# Mini Project (W2): Student Management System

**Skill Gain:** Data storage, file I/O, CRUD logic.

A command-line student management system that stores student
records (roll number, name, marks) permanently in a CSV file
(`students.csv`), which is created automatically on first run.

## Features
- Add a new student
- Delete a student by roll number
- Search for a student by roll number
- View all students
- All changes are saved permanently to the CSV file

## Concepts Used
- File I/O with the `csv` module
- Functions (modular programming — one function per operation)
- Loops and menus
- Conditional statements and input validation

## How to Run
```bash
python student_management.py
```
A `students.csv` file will be created in the same folder the first
time you run the program, and will persist between runs.

## Example
```
=== Welcome to the Student Management System ===

=== Student Management System ===
1. Add Student
2. Delete Student
3. Search Student
4. View All Students
5. Exit
Choose an option (1-5): 1
Enter roll number: 101
Enter name: Aarav
Enter marks: 88
Student 'Aarav' added and saved.
```
