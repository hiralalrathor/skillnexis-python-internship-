"""
Capstone Project: Employee Data Analysis
--------------------------------------------
Focus: Full working project combining file handling, OOP, and libraries.

Tasks:
- Load CSV using Pandas
- Calculate average salary, department count
- Filter employees above a salary threshold
- Export results to a new CSV

Skill Gain: Pandas, CSV handling, filtering.
"""

import pandas as pd


class EmployeeDataAnalyzer:
    """Encapsulates loading and analyzing employee data (OOP design)."""

    def __init__(self, filename):
        self.filename = filename
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filename)
        print(f"Loaded {len(self.df)} employee records from '{self.filename}'.\n")

    def average_salary(self):
        return self.df["salary"].mean()

    def department_counts(self):
        return self.df["department"].value_counts()

    def filter_above_salary(self, threshold):
        return self.df[self.df["salary"] > threshold]

    def export_to_csv(self, data, output_filename):
        data.to_csv(output_filename, index=False)
        print(f"Exported {len(data)} records to '{output_filename}'.")


def main():
    print("=== Employee Data Analysis ===\n")

    analyzer = EmployeeDataAnalyzer("employee_data.csv")
    analyzer.load_data()

    # Average salary
    avg_salary = analyzer.average_salary()
    print(f"Average Salary: ₹{avg_salary:.2f}")

    # Department count
    print("\nEmployee Count by Department:")
    print(analyzer.department_counts())

    # Filter employees above a salary threshold
    try:
        threshold = float(input("\nEnter a salary threshold to filter above: "))
    except ValueError:
        print("Invalid number, using default threshold of 60000.")
        threshold = 60000

    filtered = analyzer.filter_above_salary(threshold)
    print(f"\nEmployees earning above ₹{threshold:.2f}:")
    print(filtered[["name", "department", "salary"]].to_string(index=False))

    # Export filtered results
    output_file = "high_earners.csv"
    analyzer.export_to_csv(filtered, output_file)


if __name__ == "__main__":
    main()
