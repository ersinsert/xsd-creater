import tkinter as tk
from tkinter import filedialog
import openpyxl

class ExcelRow:
    def __init__(self, **kwargs):
        for column, value in kwargs.items():
            setattr(self, str(column), value)

class module_class:
    def __init__(self, name):
        self.name = name
        self.tables = []



class parameter_class:
    def __init__(self,parameter_name, display_name, parameter_type,
                 mandatory_range, gui_value, actual_value, enumeration_type, default_value,
                 initial_value, description, version, access_mode, parameter, service_affect,
                 rules, notlar):
        self.parameter_name = parameter_name
        self.display_name = display_name
        self.parameter_type = parameter_type
        self.mandatory_range = mandatory_range
        self.gui_value = gui_value
        self.actual_value = actual_value
        self.enumeration_type = enumeration_type
        self.default_value = default_value
        self.initial_value = initial_value
        self.description = description
        self.version = version
        self.access_mode = access_mode
        self.parameter = parameter
        self.service_affect = service_affect
        self.rules = rules
        self.notlar = notlar


class main_table_class():
    def __init__(self, name):
        self.name = name
        self.inside_table = []
        self.parameter = []



def dot_check(my_string):
    dot_index = my_string.find(".")
    return dot_index

module_names =[]
modules = []
table_names =[]
tables = []
def read_excel_file(file_path):
    try:
        # Opening Excel file
        workbook = openpyxl.load_workbook(file_path, data_only=True)

        excel_data = {}  # Dict to store sheets

        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]

            #print("max row " + sheet.max_row)
            #print("max column " + sheet.max_column)

            # Get the column names from the first row
            columns = [cell.value for cell in sheet[1]]

            # Create a list to store the data from the current sheet
            sheet_data = []
            module = []

            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column, values_only=True):

                i = 0
                for cell in row:
                    if row[0] is None and i == 0:
                        v=0

                    else:
                        if i == 10:
                            break
                        item = module_class(row[0])
                        module.append(item)
                    i = i + 1


            for col in sheet.iter_cols(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column,values_only=True):
                for cell in col:
                    if cell:
                        if v == 0:
                            module_names.append(cell)

                        if v == 1:
                            table_names.append(cell)

                    else:
                        continue

                v = v + 1

            excel_data[sheet_name] = sheet_data  # Store the sheet data in the dictionary

        # Close the Excel file
        workbook.close()
        print("*********")
        print(module_names)
        print("^^^^^^^^")
        print(table_names)

        return excel_data

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def print_excel_data(excel_data):
    if excel_data is not None:
        for sheet_name, sheet_data in excel_data.items():
            print(f"Sheet: {sheet_name}")
            for row in sheet_data:
                # Access data using attribute names (e.g., row.modules)
                print(vars(row))
            print()
    else:
        print("No file selected.")

def open_excel_file():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])

    excel_data = read_excel_file(file_path)
    # print_excel_data(excel_data)

if __name__ == "__main__":
    open_excel_file()
