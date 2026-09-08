# Practice Questions — Week 3: File Handling & Libraries

Five standalone practice scripts covering file handling, Pandas,
Matplotlib, and JSON.

| # | File | Question |
|---|------|----------|
| 1 | `q1_count_lines.py` | Read a file and count total lines |
| 2 | `q2_merge_files.py` | Write a program to merge two text files |
| 3 | `q3_pandas_csv_analysis.py` | Use Pandas to load and analyze a CSV file |
| 4 | `q4_matplotlib_line_graph.py` | Use Matplotlib to plot a line graph |
| 5 | `q5_create_read_json.py` | Create a JSON file and read data from it |

## Sample Data Files Included
- `sample.txt` — used by Q1
- `file1.txt`, `file2.txt` — used by Q2 (merges into `merged.txt`)
- `employees.csv` — used by Q3
- Q4 generates and saves `line_graph.png`
- Q5 generates `students_output.json`

## Setup
Q3 and Q4 require `pandas` and `matplotlib`:
```bash
pip install pandas matplotlib
```

## How to Run
```bash
python q1_count_lines.py        # enter: sample.txt
python q2_merge_files.py        # enter: file1.txt, file2.txt, merged.txt
python q3_pandas_csv_analysis.py  # enter: employees.csv
python q4_matplotlib_line_graph.py
python q5_create_read_json.py
```
