import openpyxl
import tkinter as tk
from tkinter import filedialog

def create_dynamic_class(num_variables):
    class_name = f'DynamicClassWith{num_variables}Strings'
    dynamic_class = type(class_name, (object,), {f'var{i}': '' for i in range(1, num_variables + 1)})

    return dynamic_class

# Create a tkinter root window (it won't be displayed)
root = tk.Tk()
root.withdraw()

# Open a file dialog to select an Excel file
file_path = filedialog.askopenfilename(title="Select an Excel file", filetypes=[("Excel Files", "*.xlsx")])

if file_path:
    try:
        # Load the Excel file
        workbook = openpyxl.load_workbook(file_path)

        # Select the desired worksheet (you can change the sheet name)
        sheet = workbook.active  # or specify the sheet name like sheet = workbook['Sheet1']

        # Create a list to store the data
        data = []

        # Iterate through the rows and columns to read cell values
        for row in sheet.iter_rows(values_only=True):
            row_data = []
            for cell_value in row:
                row_data.append(cell_value)
            data.append(row_data)

        # Print the data or do whatever you want with it
        for row in data:
            print(row)
        # Close the Excel file
        workbook.close()

    except Exception as e:
        print(f"An error occurred: {e}")


else:
    print("No file selected.")
