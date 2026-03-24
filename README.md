# Data_cleaning
Assignment
Objective - Analyze customer purchases and extract total item quantities for customers aged 18–35.

Soln Immplemented - 
SQL-based aggregation 
Pandas-based transformation

Run command:
python scripts/sql_solution.py
python scripts/pandas_solution.py

Filtered:
NULL quantities represent no purchase and are excluded.
Only items with total quantity > 0 are included

Output :
CSV files generated in folder = output/ with format:
Customer;Age;Item;Quantity

