"""
Practice Q3: Use Pandas to load and analyze a CSV file.
"""

import pandas as pd


def main():
    print("=== Pandas CSV Analyzer ===")
    filename = input("Enter path to CSV file (e.g. employees.csv): ").strip()

    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    print("\n--- First 5 rows ---")
    print(df.head())

    print("\n--- Summary statistics ---")
    print(df.describe())

    if "salary" in df.columns:
        print(f"\nAverage salary: {df['salary'].mean():.2f}")
        print(f"Highest salary: {df['salary'].max()}")
        print(f"Lowest salary: {df['salary'].min()}")

    if "department" in df.columns:
        print("\n--- Count by department ---")
        print(df["department"].value_counts())


if __name__ == "__main__":
    main()
