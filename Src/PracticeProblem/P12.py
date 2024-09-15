# Code to sum column A and B and print result in column C

import pandas as pd

# Load the Excel file
file_path = 'your_excel_file.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different
df = pd.read_excel(file_path, sheet_name=sheet_name)

print("Columns in the DataFrame:", df.columns)

# Assuming column names are 'A' and 'B'
# Add a new column 'C' by summing columns 'A' and 'B'


df['C'] = df['A'] + df['B']

# Save the updated DataFrame back to Excel
df.to_excel(file_path, sheet_name=sheet_name, index=False)

print("Column C has been added to the Excel sheet with the sum of A and B.")
