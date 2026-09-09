# Capstone Project: Employee Data Analysis

**Focus:** Full working project combining file handling, OOP, and libraries.
**Skill Gain:** Pandas, CSV handling, filtering.

A capstone project that analyzes an employee dataset using an
object-oriented design. Loads employee records from a CSV file,
computes statistics, filters high earners, and exports the results
to a new CSV file.

## Features
- Load employee data from CSV using Pandas
- Calculate average salary across all employees
- Count employees per department
- Filter employees above a chosen salary threshold
- Export filtered results to `high_earners.csv`

## Dataset
`employee_data.csv` — a sample dataset of 15 employees (name,
department, salary, years of experience), included so the script
runs immediately. You can swap in a real dataset (e.g. from Kaggle)
with the same column names.

## Concepts Used
- Object-oriented design (`EmployeeDataAnalyzer` class)
- Pandas (`read_csv`, `mean()`, `value_counts()`, filtering, `to_csv`)
- File I/O

## Setup
```bash
pip install pandas
```

## How to Run
```bash
python employee_analysis.py
```

## Example
```
=== Employee Data Analysis ===

Loaded 15 employee records from 'employee_data.csv'.

Average Salary: ₹58666.67

Employee Count by Department:
Engineering    5
Sales          4
Marketing      3
HR             3

Enter a salary threshold to filter above: 60000

Employees earning above ₹60000.00:
          name   department  salary
   Aarav Sharma  Engineering   72000
    Kabir Singh  Engineering   68000
    Ananya Iyer  Engineering   81000
   Aditya Kumar  Engineering   75000
    Divya Joshi    Marketing   61000
    Arjun Verma  Engineering   69000

Exported 6 records to 'high_earners.csv'.
```
